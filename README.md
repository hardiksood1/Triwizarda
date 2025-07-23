# 🛍️ Product Image Intelligence (Multi-language)

This project uses artificial intelligence to analyze product images and extract key details such as **brand**, **title**, **description**, and **features**. It also provides **comparable product recommendations** and **price comparisons** from online retailers. Output can be translated into multiple languages for global accessibility.

---

## 🚀 Features

- 📸 **Automatic Product Analysis**: Upload a product image to extract details.
- 🧠 **AI-Powered Insights**: Uses NVIDIA's AI model to generate product metadata.
- 🛒 **Price & Product Comparison**: Retrieves prices and similar items via SerpApi from Google Shopping.
- 🌐 **Multi-language Support**: Translates product descriptions into several languages.
- 🖥️ **User-Friendly Interface**: Built with Gradio for intuitive web interaction.

---

## ⚙️ Setup Instructions

### ✅ Requirements

- Python 3.7 or later  
- NVIDIA API key (for AI Shopping data)  
- SerpApi key (for Google Shopping data)  
- Invoke URL for NVIDIA Cloud Function  

---

## 📦 Installation

Download or clone the project repository.

Install dependencies using pip:
pip install -r requirements.txt
---

## 🧑‍💻 How to Use
---

### Run the application:
---
- python app.py
#### Then:

Open the displayed link in your browser.
Upload a product image.
Select your desired output language.
View product details, pricing, and similar product recommendations.


## 📁 Project Structure
---
File	                                             Description
config.py:                	Stores configuration variables like API keys and endpoint URLs
core_logic.py:	            Handles image processing, AI queries, data fetching, and translation logic
app.py:                                	Launches the Gradio web interface
---
## 📝 Notes
---
Ensure all API keys and URLs are correctly configured in config.py.
Images are automatically compressed to meet API size requirements.
English is used by default unless another language is selected.
