from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from gitclone import store_repo
from langchain_community.embeddings.sentence_transformer import (
    SentenceTransformerEmbeddings,
)
from Matrixone import Matrixone
from config import DATABASE_USER, DATABASE_PORT, DATABASE_HOST, DATABASE_PSW, DATABASE_NAME_EMBEDDED
import os
from db_client import DbClient
if not os.environ.get("OPENAI_API_KEY"):
    os.environ["OPENAI_API_KEY"] = ""
import json
def subscribe(repo_name:str):
    store_repo(repo_name)
    repo_table_name = repo_name.replace("/", "_")
    repo_table_name = repo_table_name.replace("-", "_")
    embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    db = Matrixone(
        host=DATABASE_HOST,
        port=DATABASE_PORT,
        user=DATABASE_USER,
        password=DATABASE_PSW,
        dbname=DATABASE_NAME_EMBEDDED,
        table_name=repo_table_name,
        embedding=embedding_function
    )
    #query = "connect mqtt used for what, can you tell me"
    #docs = db.similarity_search(query)
    # print results
    # print(docs[0].page_content)

def chat(query, repo_name:str, sender_name:str):
    embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    repo_table_name = repo_name.replace("/", "_")
    repo_table_name = repo_table_name.replace("-", "_")
    db = Matrixone(
        host=DATABASE_HOST,
        port=DATABASE_PORT,
        user=DATABASE_USER,
        password=DATABASE_PSW,
        dbname=DATABASE_NAME_EMBEDDED,
        table_name=repo_table_name,
        embedding=embedding_function
    )

    retriever = db.as_retriever()
    llm = ChatOpenAI(model="gpt-4o-mini")

    prompt = ChatPromptTemplate.from_messages(
        [
            ("placeholder", "{chat_history}"),
            ("user", "{input}"),
            (
                "user",
                "Given the above conversation, generate a search query to look up to get information relevant to the conversation",
            ),
        ]
    )
    retriever_chain = create_history_aware_retriever(llm, retriever, prompt)
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "Answer the user's questions based on the below context:\n\n{context}",
            ),
            ("placeholder", "{chat_history}"),
            ("user", "{input}"),
        ]
    )
    document_chain = create_stuff_documents_chain(llm, prompt)

    qa = create_retrieval_chain(retriever_chain, document_chain)
    result = qa.invoke({"input": query})
    print(result["answer"])
    client = DbClient()
    client.store_messages(
            sender_name="bot-" + sender_name,
            room_name=repo_name,
            content=result["answer"])
# chat('can you tell me what is the funciton pf mqtt used ','addw1/Car-Monitor', 'ning')
#subscribe('addw1/Car-Monitor')



from confluent_kafka import Consumer, KafkaException

conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'my-consumer-group-1',
    'auto.offset.reset': 'earliest'
}

if __name__ == "__main__":
    # create kafka consumer
    consumer = Consumer(conf)
    # subscribe two topics
    topics = ['chat', 'subscribe']
    consumer.subscribe(topics)
    try:
        while True:
            # get the message from kafka
            msg = consumer.poll(timeout=1.0)

            if msg is None:
                continue

            if msg.error():
                raise KafkaException(msg.error())
            # print(f'Received message from topic {msg.topic()}: {msg.value().decode("utf-8")}')
            if msg.topic() == "chat":
                msg_json = json.loads(msg.value().decode("utf-8"))
                repo_path = "./repo/" + msg_json.get("groupName")
                if os.path.exists(repo_path) is not True:
                    client = DbClient()
                    client.store_messages(
                        sender_name="bot-" + msg_json.get("senderName"),
                        room_name= msg_json.get("groupName"),
                        content="I'm still learning about the warehouse, so please wait~")
                chat(
                    repo_name=msg_json.get("groupName"),
                    sender_name=msg_json.get("senderName"),
                    query=msg_json.get("content"),
                )

            elif msg.topic() == "subscribe":
                repo_json = json.loads(msg.value().decode("utf-8"))
                repo_name = str(repo_json)
                subscribe(repo_name)

    except KeyboardInterrupt:
        print("Consumer interrupted by user")

    finally:
        consumer.close()