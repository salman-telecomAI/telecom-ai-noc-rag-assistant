from sentence_transformers import SentenceTransformer

# Lightweight local embedding model
_model = SentenceTransformer("all-MiniLM-L6-v2")


class LocalEmbeddings:
    def embed_query(self, text: str):
        return _model.encode(text, convert_to_numpy=True).tolist()

    def embed_documents(self, texts):
        return _model.encode(texts, convert_to_numpy=True).tolist()


embeddings = LocalEmbeddings()


if __name__ == "__main__":
    vector = embeddings.embed_query("Loss of Signal alarm in DWDM")

    print(f"Embedding dimensions: {len(vector)}")
    print(vector[:10])
