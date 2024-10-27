import os
from git import Repo
from langchain_community.document_loaders.generic import GenericLoader
from langchain_community.document_loaders.parsers import LanguageParser
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain_text_splitters import Language
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from Matrixone import Matrixone
from config import DATABASE_USER, DATABASE_PORT, DATABASE_HOST, DATABASE_PSW, DATABASE_NAME_EMBEDDED
from langchain_community.embeddings.sentence_transformer import (
    SentenceTransformerEmbeddings,
)
def store_repo(repo_name: str):
    repo_path = "./repo/" + repo_name
    
    # check whether exist
    if os.path.exists(repo_path):
        return
    repo = Repo.clone_from("https://github.com/" + repo_name, to_path=repo_path)
    print(f"success clone repo '{repo_path}'")
    # Load
    loader = GenericLoader.from_filesystem(
        repo_path,
        glob="**/*",
        suffixes=[".py"],
        parser=LanguageParser(language=Language.PYTHON, parser_threshold=500),
    )
    documents = loader.load()
    python_splitter = RecursiveCharacterTextSplitter.from_language(
        language=Language.PYTHON, chunk_size=2000, chunk_overlap=200
    )
    documents = python_splitter.split_documents(documents)
    embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    # store in vector database
    texts = [d.page_content for d in documents]
    metadatas = [d.metadata for d in documents]
    repo_name = repo_name.replace("/", "_")
    repo_name = repo_name.replace("-", "_")
    db = Matrixone.from_texts(texts = texts,
                              embedding=embedding_function,
                              user=DATABASE_USER,
                              password=DATABASE_PSW,
                              dbname=DATABASE_NAME_EMBEDDED,
                              port=DATABASE_PORT,
                              host = DATABASE_HOST,
                              table_name=repo_name,
                              metadatas=metadatas
                              )

