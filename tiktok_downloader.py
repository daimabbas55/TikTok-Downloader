#!/usr/bin/env python3
import requests
import json
import os
import sys
import argparse
import re

class TikTokDownloader:
    def __init__(self):
        self.api_url = "https://www.tikwm.com/api/"
        self.download_dir = "downloads"
        if not os.path.exists(self.download_dir):
            os.makedirs(self.download_dir)

    def download_video(self, url):
        print(f"Fetching details for: {url}")

        params = {
            "url": url,
            "hd": 1
        }

        try:
            response = requests.get(self.api_url, params=params)
            response.raise_for_status()
            data = response.json()

            if data.get("code") == 0:
                video_data = data["data"]
                title = video_data.get("title", "video")
                video_id = video_data.get("id", "unknown_id")

                # Prefer HD play url, fallback to play url
                download_url = video_data.get("hdplay") or video_data.get("play")

                if not download_url:
                    print("Error: No download URL found in response.")
                    return

                # Sanitize filename
                safe_title = re.sub(r'[\\/*?:"<>|]', "", title)
                # Truncate title if too long
                if len(safe_title) > 50:
                    safe_title = safe_title[:50]

                filename = f"{safe_title}_{video_id}.mp4"
                filepath = os.path.join(self.download_dir, filename)

                print(f"Downloading: {title}")
                print(f"Source URL: {download_url}")

                self._download_file(download_url, filepath)
                print(f"Successfully downloaded to: {filepath}")
            else:
                msg = data.get("msg", "Unknown error")
                print(f"Failed to fetch video details: {msg}")

        except requests.RequestException as e:
            print(f"Network error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def _download_file(self, url, filepath):
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            total_size = int(r.headers.get('content-length', 0))
            downloaded_size = 0

            with open(filepath, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
                        downloaded_size += len(chunk)
                        if total_size > 0:
                            percent = int(downloaded_size * 100 / total_size)
                            sys.stdout.write(f"\rDownloading... {percent}%")
                            sys.stdout.flush()
            print() # Newline after progress

def main():
    parser = argparse.ArgumentParser(description="TikTok Video Downloader")
    parser.add_argument("url", nargs="?", help="The TikTok video URL to download")
    args = parser.parse_args()

    downloader = TikTokDownloader()

    if args.url:
        downloader.download_video(args.url)
    else:
        print("Please enter a TikTok video URL:")
        try:
            url = input().strip()
            if url:
                downloader.download_video(url)
            else:
                print("No URL provided.")
        except KeyboardInterrupt:
            print("\nExiting...")

if __name__ == "__main__":
    main()
