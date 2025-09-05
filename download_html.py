import requests
import os
from urllib.parse import urlparse

OUTPUT_DIR = "downloaded_html"

def create_path(dir_name: str) -> str:
    path = os.path.join(os.getcwd(), dir_name)
    os.makedirs(path, exist_ok=True)
    return path

def get_filename_from_url(url: str) -> str:
    name = os.path.basename(urlparse(url).path)
    if not name or '.' not in name:
        name = "index.html"
    return name

def download_html(url: str, output_dir: str = OUTPUT_DIR) -> str:
    output_dir = create_path(output_dir)
    response = requests.get(url)
    if response.status_code != 200 or not response.text.strip():
        raise RuntimeError(f"Failed to download HTML from {url} (status {response.status_code})")

    
    filename = get_filename_from_url(url)
    output_file = os.path.join(output_dir, filename)
    
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(response.text)
    
    print(f"HTML saved to: {output_file}")
    return output_file

