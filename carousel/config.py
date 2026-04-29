import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Telegram Bot Configuration
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# OpenAI API Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# KIE (Knowledge & Integration Engine) Client Configuration
KIE_API_URL = os.getenv("KIE_API_URL")
KIE_API_KEY = os.getenv("KIE_API_KEY")

# Image Generation Settings
DEFAULT_IMAGE_MODEL = "gpt-4o-image"  # Sesuai tutorial di video
IMAGE_RESOLUTION = "1024x1024"
