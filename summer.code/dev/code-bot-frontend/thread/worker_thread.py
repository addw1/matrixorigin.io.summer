import time
from PyQt5.QtCore import pyqtSignal, QThread

from client.chat import ChatClient

GUIDE_CONVERSATION = 'I am Code Copilot. How can I assist you today? I can help by recommending opportunities, retrieving data, providing historical summaries, and more.'


class SendThread(QThread):
    # define the type of asyn result
    result_ready = pyqtSignal(str)

    def __init__(self, user_id, group_name, text, client: ChatClient):
        super().__init__()
        self.client = client
        self.user_id = user_id
        self.text = text
        self.group_name = group_name

    def run(self):
        resp = self.client.send_msg(
           name=self.user_id,
           group_name=self.group_name,
           text=self.text,
        )
        self.result_ready.emit(resp)

class UpdateThread(QThread):
    result_ready = pyqtSignal(str)

    def __init__(self, user_name, group_name, client):
        super().__init__()
        self.user_name = user_name
        self.group_name = group_name
        self.client = client
    def run(self):
        resp = self.client.check(user_name=self.user_name, group_name=self.group_name)
        self.result_ready.emit(resp)