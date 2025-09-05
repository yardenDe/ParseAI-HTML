from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def split_into_sentences(text: str):
    return [s.strip() for s in text.split('.') if s.strip()]

def create_embeddings(sentences):
    return model.encode(sentences, convert_to_tensor=True)

def semantic_search(query: str, sentences, sentence_embeddings, top_k=5):
    query_embedding = model.encode(query, convert_to_tensor=True)
    hits = util.semantic_search(query_embedding, sentence_embeddings, top_k=top_k)
    results = []
    for hit in hits[0]:
        results.append(sentences[hit['corpus_id']])
    return results
