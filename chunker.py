def chunk_text(text, chunk_size=800, overlap=150):
    words = text.split()   # entire text of the pdf is split into words
    chunks = []
    start = 0

    while start < len(words):
        end = start + chunk_size       #a chunk is formed star 0 to end 200 for the first chunk
        chunk = " ".join(words[start:end])
        chunks.append(chunk)          #the words are inserted in it
        start = end - overlap   # after the first chunk ends at 200, to have overlap start is from 150

    return chunks