# 🧠📸 Product Image Intelligence (Multi-language)
> *"AI that sees, understands, and speaks your product—instantly."*

![Python](https://img.shields.io/badge/python-%233776AB.svg?style=for-the-badge&logo=python&logoColor=white)
![Gradio](https://img.shields.io/badge/gradio-00b4b6?style=for-the-badge&logo=gradio&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)
![NVIDIA](https://img.shields.io/badge/NVIDIA-A6E22E?style=for-the-badge&logo=nvidia&logoColor=black)
![Google Cloud](https://img.shields.io/badge/Google%20Cloud-4285F4?style=for-the-badge&logo=googlecloud&logoColor=white)
![SerpApi](https://img.shields.io/badge/SerpAPI-00B488?style=for-the-badge&logo=google&logoColor=white)
![Google Translate API](https://img.shields.io/badge/Google%20Translate-4285F4?style=for-the-badge&logo=googletranslate&logoColor=white)
![Pillow](https://img.shields.io/badge/Pillow-3076AF?style=for-the-badge&logo=python&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-005571?style=for-the-badge&logo=python&logoColor=white)
![JSON](https://img.shields.io/badge/JSON-5E5C5C?style=for-the-badge&logo=json&logoColor=white)
![VSCode](https://img.shields.io/badge/VSCode-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white)

Welcome to a powerful AI tool that analyzes product images and automatically generates:

- 🏷️ Brand  
- 📝 Title & Description  
- ✨ Key Features  
- 💲 Price Comparisons  
- 🔄 Similar Product Suggestions  
- 🌐 Translations in multiple languages

---
## 🎥 Demo Preview

See how our AI extracts product info, translates it, and compares prices — all from a single image!

![Product Image Intelligence Demo](https://github.com/alo7lika/TriwizardaThon/blob/main/Demo.gif)

---

## 🔍 What’s Inside

This application converts any product image into a detailed, multilingual product card—perfect for e-commerce, cataloging, and digital retail platforms.

---

## 🌟 Features Overview

| Feature                     | Description                                                                 |
|----------------------------|-----------------------------------------------------------------------------|
| 🖼️ Image Upload            | Upload a product image to extract all product details                       |
| 🧠 AI-Powered Metadata      | Uses NVIDIA's Janus-Pro-7B via cloud to understand product visuals          |
| 🌍 Multi-Language Support   | Translate output into English, Hindi, French, and more                      |
| 🛒 Price & Product Compare  | Uses SerpApi to fetch prices and similar products from Google Shopping      |
| 🖥️ Gradio UI                | Simple, no-code web interface for fast interaction                          |

---

## ⚙️ Tech Stack

- Python 3.7+
- Gradio (Frontend)
- Hugging Face Transformers
- DeepSeek Janus-Pro-7B (via NVIDIA cloud)
- SerpApi (Google Shopping API)
- PIL (Image Processing)
- CUDA acceleration (for local GPU inference)

---

## 🚀 Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/your-username/product-image-intelligence

# 2. Navigate to the folder
cd product-image-intelligence

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python app.py
```
## ✅ How to Use

1. Open the **Gradio link** in your browser  
2. 📤 Upload a **product image**  
3. 🌐 Select your desired **language**  
4. 👀 View the AI-generated output:  
   - Brand  
   - Title  
   - Description  
   - Features  
   - Price comparisons & similar products  

---

## 📁 Project Structure

product-image-intelligence/
├── app.py # Launches the Gradio web interface
├── core_logic.py # AI logic for image → text + translation + SerpAPI
├── config.py # Stores API keys and cloud endpoints
├── requirements.txt # All Python dependencies


---

## 🧪 Example Flow

- **Upload**: Headphones image  
- **Select**: French  
- **Output**:

Marque: Sony
Titre: Casque sans fil
Description: Son immersif avec réduction de bruit
Prix: ₹2999 (plus similar products listed)


➡️ Then try again with a **beauty product** → Output appears in **Hindi**!

---

## 📝 Notes

Make sure your `config.py` contains:

- `NVIDIA_API_KEY`  
- `SERPAPI_KEY`  
- `NVIDIA Cloud URL`  

⚠️ Images are **auto-compressed** to meet API size limits  
🌍 English is the **default output language** unless changed

---

## 🚧 Coming Soon

- 🔊 **Voice input/output**  
- 📄 **Export to Excel/PDF**  
- 🛒 **Integration with Shopify / Amazon APIs**  
- 🌐 **More language support** (Spanish, German, Bengali, etc.)

---

## 👨‍💻 Created by **Team Innova1**

Made with ❤️ for smarter, faster, and multilingual e-commerce automation.

📧 **Contact**: [your-email@example.com]  
🌐 **Live Demo**: *Coming Soon*
