# BREAKDOWN: Cara Bangun Bot Telegram Carousel (Step by Step)


## Pipeline Dasar (Step 1)
Bot Telegram dengan fitur carousel yang menggunakan AI untuk generate gambar dan konten. Struktur file:
- `carousel/config.py`: Konfigurasi API keys & environment variables
- `kie_client.py`: Klien untuk mengakses Knowledge & Integration Engine
- `script_generator.py`: Generate script konten untuk carousel
- `image_generator.py`: Generate gambar menggunakan OpenAI GPT-Image
- `telegram_sender.py`: Kirim pesan & media ke Telegram
- `cli.py`: Command line interface untuk mengoperasikan bot
- `carousel.py`: Logika utama bot untuk merakit semua komponen
- `carousel/themes.py`: Preset tema visual untuk konten carousel (Step 2)

## Cara Setup
1. Salin `.env.example` jadi `.env` dan isi semua kredensial
2. Install dependensi: `pip install -r requirements.txt`
3. Jalankan bot: `python cli.py start`
