# Product Image Intelligence (Multi-language)
In order to identify product details such as brand, title, description, and key features, this project uses artificial intelligence to analyze product images. Additionally, it offers comparable product recommendations and price comparisons from online retailers. Several languages can be used to translate the output.

#Features
To have a product image automatically analyzed, upload it.\
Use NVIDIA's AI model to create product details.
Use SerpApi to retrieve prices and comparable product details from Google Shopping.
Translate descriptions into multiple languages.
Gradio was used to create an intuitive web interface.

#Instructions for Setup
#Requirements
Python 3.7 or later
NVIDIA API key to access AI
Shopping data using the SerpApi key
Invoke URL for NVIDIA Cloud Function

#Installation
Download the project files or clone them.
Install Python dependencies:

#How to Use
Run the application:
python app.py

Open the displayed link in a web browser. Upload a product image and select the desired language. The app will return product details, prices, and similar products.

#Project Structure
config.py : Stores configuration variables like API keys and URLs.
core_logic.py : Contains image processing, AI querying, data fetching, and translation functions.
app.py : Launches the Gradio web interface.

#Notes
Ensure API keys and URLs are set correctly.
Image compression is automatic to stay within API size limits.
English is the default language unless another language is chosen.
