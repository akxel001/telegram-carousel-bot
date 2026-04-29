from diffusers import StableDiffusionPipeline
import torch
import os

class ImageGenerator:
    def __init__(self, model_name="runwayml/stable-diffusion-v1-5"):
        # Load model Stable Diffusion GRATIS, jalan lokal
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.pipeline = StableDiffusionPipeline.from_pretrained(
            model_name,
            torch_dtype=torch.float16 if self.device == "cuda" else torch.float32
        )
        self.pipeline = self.pipeline.to(self.device)

    def generate_image(self, prompt: str, output_path: str) -> str:
        """Generate gambar lokal dari prompt, tanpa biaya API sama sekali"""
        # Generate gambar
        image = self.pipeline(prompt).images[0]
        # Simpan ke file
        image.save(output_path)
        return output_path