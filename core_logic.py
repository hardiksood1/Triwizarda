# core_logic.py

import requests
import base64
import io
from PIL import Image
from serpapi import GoogleSearch
import re
from config import NVIDIA_API_KEY, SERPAPI_KEY, INVOKE_URL

# Compatibility for Pillow
try:
    resample = Image.Resampling.LANCZOS
except AttributeError:
    resample = Image.LANCZOS


#Adjustment of the image quality

def compress_image_to_limit(image, size_limit=180_000, min_quality=10, min_width=500):
    img = image.convert("RGB")
    width, height = img.size
    quality = 95

    while quality >= min_quality:
        buffer = io.BytesIO()
        img.save(buffer, format="JPEG", quality=quality)
        image_b64 = base64.b64encode(buffer.getvalue()).decode()
        if len(image_b64) < size_limit:
            return image_b64
        quality -= 5

    while width > min_width:
        width = int(width * 0.8)
        height = int(height * 0.8)
        img = img.resize((width, height), resample)
        quality = 95
        while quality >= min_quality:
            buffer = io.BytesIO()
            img.save(buffer, format="JPEG", quality=quality)
            image_b64 = base64.b64encode(buffer.getvalue()).decode()
            if len(image_b64) < size_limit:
                return image_b64
            quality -= 5

    raise ValueError("Image remains too large even after compression.")


# querry for the multimodel main model in this project
def query_nvidia_model(image_b64):
    headers = {
        "Authorization": f"Bearer {NVIDIA_API_KEY}",
        "Accept": "application/json"
    }
    prompt = f"""
What is this product? Generate:
1. Brand
2. Title
3. Short Description
4. Key Features

<img src="data:image/jpeg;base64,{image_b64}" />
"""
    payload = {
        "model": "google/gemma-3-27b-it",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 512,
        "temperature": 0.3,
        "top_p": 0.8,
        "stream": False
    }
    response = requests.post(INVOKE_URL, headers=headers, json=payload)
    response.raise_for_status()
    content = response.json()["choices"][0]["message"]["content"]

    brand_match = re.search(r"\*\*1\. Brand:\*\*\s*(.+)", content)
    brand = brand_match.group(1).strip() if brand_match else ""

    title_match = re.search(r"\*\*2\. Title:\*\*\s*(.+)", content)
    title = title_match.group(1).strip() if title_match else ""

    key_features = ""
    key_features_match = re.search(r"\*\*4\. Key Features:\*\*\s*((?:.|\n)*?)(?:\n\n|\Z)", content)
    if key_features_match:
        features_block = key_features_match.group(1)
        features = re.findall(r"\*\*(.+?):\*\* (.+)", features_block)
        if features:
            key_features = ", ".join([f"{k}: {v}" for k, v in features])
        else:
            key_features = features_block.replace("*", "").replace("\n", ", ").strip()

    search_query = f"{brand} {title} {key_features}".strip()
    return content, search_query

#using the serpapi for the web search we also use playload but google search is restricted 
def fetch_market_data(search_query):
    search = GoogleSearch({
        "engine": "google_shopping",
        "q": search_query,
        "api_key": SERPAPI_KEY,
        "gl": "in",
        "hl": "en",
        "num": 6
    })

    results = search.get_dict()
    prices = []
    products = []
    for item in results.get("shopping_results", []):
        price_str = item.get('price', '').replace('₹', '').replace(',', '').split()[0]
        try:
            price = int(price_str)
            prices.append(price)
        except (ValueError, TypeError):
            pass

        product_info = {
            'title': item.get('title', 'No Title'),
            'price': item.get('price', 'N/A'),
            'source': item.get('source', 'Unknown'),
            'image': item.get('thumbnail', ''),
            'link': item.get('link', '#')
        }
        products.append(product_info)

    unique_prices = sorted(set(prices))[:5]
    return [f"₹{p}" for p in unique_prices], products[:5]


#Same LLM is used for the multi language 
def translate_description(original_description, language):
    if language == "English":
        return original_description

    headers = {
        "Authorization": f"Bearer {NVIDIA_API_KEY}",
        "Accept": "application/json"
    }
    prompt = f"""
Translate the following product description to {language}:

{original_description}
"""
    payload = {
        "model": "google/gemma-3-27b-it",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 512,
        "temperature": 0.3,
        "top_p": 0.8,
        "stream": False
    }
    response = requests.post(INVOKE_URL, headers=headers, json=payload)
    response.raise_for_status()
    translated = response.json()["choices"][0]["message"]["content"]
    return translated
#gradio styling 
def process(image, language, progress=None):
    try:
        if progress:
            progress(0, desc="Compressing image...")
        image_b64 = compress_image_to_limit(image)
        if progress:
            progress(0.33, desc="Generating product details...")
        description, search_query = query_nvidia_model(image_b64)
        if progress:
            progress(0.66, desc="Fetching market data...")
        prices, products = fetch_market_data(search_query)
        if progress:
            progress(0.8, desc="Translating...")
        translated_description = translate_description(description, language)
        if progress:
            progress(1.0, desc="Done")

        output = f" 🏷️ Product Details ({language})\n{translated_description}\n\n"
        output += f"🔎 Google Shopping Search Query: `{search_query}`\n\n"
        output += "💰 Price Comparison\n"
        output += "\n".join(f"- {p}" for p in prices) + "\n\n" if prices else "- No price data found.\n\n"
        output += "### 🛒 Similar Products\n"
        recommendation_links = []
        if products:
            for product in products:
                img_md = f"![Product Image]({product['image']})" if product['image'] else ""
                output += (
                    f"[{product['title']}]({product['link']})**\n"
                    f"Price: {product['price']}  \n"
                    f"Source: {product['source']}  \n"
                    f"{img_md}\n\n"
                )
                recommendation_links.append(f"[{product['title']}]({product['link']})")
        else:
            output += "- No similar products found.\n"

        if recommendation_links:
            output += "### ⭐ Recommendation Links\n"
            output += "\n".join(f"- {link}" for link in recommendation_links) + "\n"

        return output
    except Exception as e:
        return f"❌ Error: {str(e)}"
