#The app file that we have to exicute 

import gradio as gr
from core_logic import process

demo = gr.Interface(
    fn=process,
    inputs=[
        gr.Image(type="pil", label="Upload Product Image"),
        gr.Dropdown(
            label="Select Output Language",
            choices=["English", "Hindi", "Punjabi", "French", "German"],
            value="English"
        )
    ],
    outputs=gr.Markdown(label="Product Analysis"),
    title="🛍️ Product Image Intelligence (Multi-language)",
    description="MarketLens AI"
)

if __name__ == "__main__":
    demo.launch(share=True)
