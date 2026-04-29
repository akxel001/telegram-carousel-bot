import asyncio
from telegram import InputMediaPhoto, InputMediaVideo
from telegram.ext import Application
from .config import TELEGRAM_BOT_TOKEN

class TelegramSender:
    def __init__(self):
        self.application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    async def send_carousel(self, chat_id: int, media_files: list, captions: list = None):
        """Kirim carousel (media group) ke chat Telegram"""
        media = []
        for idx, file_path in enumerate(media_files):
            caption = captions[idx] if captions and idx < len(captions) else ""
            media.append(InputMediaPhoto(open(file_path, "rb"), caption=caption))
        
        await self.application.bot.send_media_group(chat_id=chat_id, media=media)

    def sync_send_carousel(self, chat_id: int, media_files: list, captions: list = None):
        """Wrapper sinkron untuk mengirim carousel dari CLI"""
        asyncio.run(self.send_carousel(chat_id, media_files, captions))