from flask import Flask, render_template, request, send_file
import requests
import os
import re

app = Flask(__name__)
DOWNLOAD_DIR = "downloads"
if not os.path.exists(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR)

API_URL = "https://www.tikwm.com/api/"

def fetch_video_data(url):
    params = {"url": url, "hd": 1}
    try:
        response = requests.get(API_URL, params=params)
        response.raise_for_status()
        data = response.json()
        if data.get("code") == 0:
            return data["data"]
    except Exception as e:
        print(f"Error fetching data: {e}")
    return None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form.get('url')
        if url:
            data = fetch_video_data(url)
            if data:
                return render_template('result.html', data=data)
            else:
                return render_template('index.html', error="Could not fetch video details. Check URL.")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
