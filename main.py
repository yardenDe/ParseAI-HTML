from pathlib import Path
from download_html import download_html
from parse_html import extract_text_from_html, save_text
from s_search import split_into_sentences, create_embeddings, semantic_search

if __name__ == "__main__":
    url = input("Enter the URL of the page to download: ").strip()
    output_dir = Path("downloaded_html")
    output_dir.mkdir(exist_ok=True)

    html_file = download_html(url, output_dir)
    html_file = Path(html_file)

    text = extract_text_from_html(html_file)
    txt_file = html_file.with_suffix(".txt")
    save_text(text, txt_file)

    sentences = split_into_sentences(text)
    sentence_embeddings = create_embeddings(sentences)

    print("\nYou can now ask questions about this page.")
    while True:
        query = input("\nEnter your question (or 'exit' to quit): ")
        if query.lower() == "exit":
            break
        results = semantic_search(query, sentences, sentence_embeddings, top_k=5)
        print("\n--- Top Results ---\n")
        for i, res in enumerate(results, 1):
            print(f"{i}. {res}\n")
