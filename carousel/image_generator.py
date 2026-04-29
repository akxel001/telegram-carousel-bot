from openai import OpenAI
from .config import OPENAI_API_KEY, DEFAULT_IMAGE_MODEL, IMAGE_RESOLUTION
import os
import requests

class ImageGenerator:
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)

    def generate_image(self, prompt: str, output_path: str) -> str:
        """Generate gambar dari prompt teks menggunakan OpenAI GPT-Image"""
        response = self.client.images.generate(
            model=DEFAULT_IMAGE_MODEL,
            prompt=prompt,
            size=IMAGE_RESOLUTION,
            n=1
        )
        
        # Download gambar dan simpan ke output path
        image_url = response.data[0].url
        img_data = requests.get(image_url).content
        with open(output_path, 'wb') as handler:
            handler.write(img_data)
        
        return output_path