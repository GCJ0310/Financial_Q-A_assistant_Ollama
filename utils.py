def chunk_text(text, max_words=500):
    """
    Splits text into chunks of ~max_words each.
    """
    words = text.split()
    chunks = []
    for i in range(0, len(words), max_words):
        chunks.append(" ".join(words[i:i+max_words]))
    return chunks
