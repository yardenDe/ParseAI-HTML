from bs4 import BeautifulSoup
from pathlib import Path

def extract_text_from_html(file_path) -> str:
    file_path = Path(file_path)  
    html = file_path.read_text(encoding="utf-8", errors="ignore")
    soup = BeautifulSoup(html, "html.parser")
    return soup.get_text(separator="\n", strip=True)

def save_text(text: str, output_file: Path):
    output_file.write_text(text, encoding="utf-8")
    print(f"Text saved to: {output_file}")

