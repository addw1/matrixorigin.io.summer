from confluent_kafka import Consumer, KafkaException
import json
from app.client import DbClient
from app.routes import download_task
import concurrent.futures
from app.routes import talk

conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'my-consumer-group-1',
    'auto.offset.reset': 'earliest'
}

# create kafka consumer
consumer = Consumer(conf)

# subscribe two topics
topics = ['chat', 'subscribe']
consumer.subscribe(topics)

# create db client
db = DbClient()
# create thread pool
excutor = concurrent.futures.ThreadPoolExecutor()


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
            ans = talk(msg_json.get("groupName"), msg_json.get("senderName"), msg_json.get("content"))
            db.store_messages(
                sender_name="bot-" + msg_json.get("senderName"),
                room_name=msg_json.get("groupName"),
                content=ans
            )

        elif msg.topic() == "subscribe":
            repo_json = json.loads(msg.value().decode("utf-8"))
            repo_name = str(repo_json)
            if db.check_table_exists('code_repo', repo_name) is not True:
                repo_url = 'https://github.com/' + repo_name
                excutor.submit(download_task, repo_url)

except KeyboardInterrupt:
    print("Consumer interrupted by user")

finally:
    consumer.close()