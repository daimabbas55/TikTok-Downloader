# TikSwift - Fast TikTok Downloader

A high-speed, SEO-optimized TikTok video downloader web application built with Python Flask. Download videos without watermarks and extract MP3 audio.

## 🚀 Features

- **No Watermark:** Download clean videos.
- **Audio Extraction:** Download MP3 audio.
- **Fast & Responsive:** Built with Tailwind CSS and minimal JS.
- **AdSense Ready:** Pre-configured placeholders for monetization.
- **SEO Optimized:** Meta tags, Sitemap, and Schema markup included.

## 🛠️ Installation (Local)

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-repo/tikswift.git
    cd tikswift
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the application:**
    ```bash
    python app.py
    ```

5.  Open `http://127.0.0.1:5000` in your browser.

## 🌍 Deployment

### Deploy on Vercel

1.  Install Vercel CLI: `npm i -g vercel`
2.  Create `vercel.json` (optional, but recommended for Python):
    ```json
    {
      "builds": [{"src": "app.py", "use": "@vercel/python"}],
      "routes": [{"src": "/(.*)", "dest": "app.py"}]
    }
    ```
3.  Run `vercel`.

### Deploy on Railway

1.  Create a new project on Railway.
2.  Connect your GitHub repository.
3.  Railway will automatically detect `requirements.txt` and `app.py`.
4.  Add a Start Command if needed: `gunicorn app:app`.

### Deploy on VPS (Ubuntu/Nginx)

1.  Upload files to server.
2.  Install Python & Dependencies.
3.  Run with Gunicorn: `gunicorn -w 4 -b 0.0.0.0:8000 app:app`
4.  Setup Nginx as a reverse proxy.

## 💰 AdSense Monetization

The `templates/index.html` file contains placeholders for Google AdSense.

1.  Get your Ad Client ID (e.g., `ca-pub-XXXXXXXXXXXXXXXX`).
2.  Uncomment the script tag in `<head>` of `templates/index.html`.
3.  Replace the placeholder `<div>` blocks with your actual Ad Units.

## ⚠️ Disclaimer

This project is for educational purposes only. This tool should not be used to download copyrighted content without permission. The developers are not affiliated with TikTok.
