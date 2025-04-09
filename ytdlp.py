import yt_dlp
import os
from urllib.parse import urlparse

from helps import read_file_to_list
## new method to download
filename = "series_animadasss.txt"
result = read_file_to_list(filename)

for index, url in enumerate(result, start=35):
    print(f"Downloading {index}: {url}")

    parsed_url = urlparse(url)
    path_parts = parsed_url.path.strip('/').split('/')

    if len(path_parts) >= 3:
        channel_name = path_parts[0]
        folder_name = channel_name
        file_name = f"{channel_name}_{index}.mp4"

        os.makedirs(folder_name, exist_ok=True)
        output_path = os.path.join(folder_name, file_name)

        ydl_opts = {
            'outtmpl': output_path,
            'format': 'bestvideo+bestaudio/best',
            'merge_output_format': 'mp4',
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
        except Exception as e:
            print(f"Error downloading {url}: {e}")
            continue  # Sigue con el siguiente enlace
