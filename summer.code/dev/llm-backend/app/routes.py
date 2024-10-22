from flask import Flask, request, render_template, Blueprint, jsonify
from flask import current_app
import threading
from .client import DbClient
from .utils import *
from .config import Config
from .rag import git_clone
from .Matrixone import Matrixone
import concurrent.futures
config = Config()

main_bp = Blueprint('main', __name__)
excutor = concurrent.futures.ThreadPoolExecutor()

os.environ["OPENAI_API_KEY"] = config.OPENAI_API_KEY


def download_task(git_url):
    # download from github
    is_success, destination = git_clone(git_url)
    if not is_success:
        return False
    # load document to memory
    documents = load_documents_from_folder(destination)
    # split document
    chunked_documents = split_documents(documents, 200, 10)
    # store in mo
    from langchain.embeddings import OpenAIEmbeddings
    vectorstore = Matrixone.from_documents(
        documents=chunked_documents, # 以分块的文档
        embedding=OpenAIEmbeddings(), # 用OpenAI的Embedding Model做嵌入
        user="root",
        password="111",
        dbname="test",
        port=6001)  # 指定c+ollection_name



def subscribe():
    # Check if the request contains JSON data
    if not request.is_json:
        return jsonify({"status": "error"}), 400
    # Get JSON data
    data = request.get_json()
    repo_name = data.get('repo_name')
    db = DbClient()
    if db.check_table_exists('code_repo', repo_name):
        return jsonify({"status": "success"}), 200
    else:
        # print(repo_name)
        repo_url = 'https://github.com/' + repo_name
        excutor.submit(download_task, repo_url)
        return jsonify({"status": "downloading"}), 200

# 接收来自code-bot的提问

def talk(repoName, userID, question):
    vectorstore = get_vectorstore(repoName)
    qa_chain = generate_qa_chain(vectorstore)
    result = qa_chain({"query": request.question})    
    return result['result']