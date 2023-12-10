import utils.File_preprocessing as fp
from langchain.vectorstores import Chroma


def VDB(filepath,embeddings):
    chunk_texts=fp.file_processing(filepath)
    vector_store = Chroma.from_documents(chunk_texts, embeddings, collection_metadata={"hnsw:space": "cosine"}, persist_directory="store/vdb")
    #print('finish_saved')
    return vector_store
