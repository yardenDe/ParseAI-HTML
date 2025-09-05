from bs4 import BeautifulSoup
from pathlib import Path

def extract_text_from_html(file_path: Path) -> str:
    html = file_path.read_text(encoding="utf-8", errors="ignore")
    soup = BeautifulSoup(html, "html.parser")
    return soup.get_text(separator="\n", strip=True)

def save_text(text: str, output_file: Path):
    output_file.write_text(text, encoding="utf-8")
    print(f"Text saved to: {output_file}")

if __name__ == "__main__":
    
    html_file = Path("downloaded_html/index.html")
    text = extract_text_from_html(html_file)
    
    print(text[:1000])
    
    # שומר את הטקסט לקובץ
    text_file = html_file.with_suffix(".txt")
    save_text(text, text_file)
