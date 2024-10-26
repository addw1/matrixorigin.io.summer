from typing import List

from domain.Message import Message
import requests


def mock(name, group_name, text):
    return group_name + '%I want to recommend M365 Business for you because it offers a comprehensive suite of tools that can significantly enhance productivity and collaboration within your team. With M365 Business, you get access to essential applications like Word, Excel, and PowerPoint, as well as powerful cloud services like OneDrive and SharePoint.'


GUIDE_CONVERSATION = 'I am Opportunity Copilot. How can I assist you today? I can help by recommending opportunities, retrieving data, providing historical summaries, and more.'


class ChatClient:
    """
    func: get the user's group
    """
    def get_groups(self, user_id:str) -> List[str]:
        # return get_groups_mock()
        try:
            url = "http://localhost:8080/codebot/repo/groups"
            params = {
                "userName": user_id
            }
            response = requests.get(url, params=params)
            response_data = response.json()
            return response_data.get("data")
        except Exception as e:
            print(e)
        return None

    """
    func: get the user's chat history
    """
    def get_mes(self, user_id: str, group_name: str, id:int, is_guide:bool) -> List[Message]:
        if is_guide:
            return get_mes_mock()
        try:
            url = "http://localhost:8080/codebot/chat/getMes"
            params = {
                "userName": user_id,
                "roomName": group_name,
                "id": id
            }
            response = requests.get(url, params=params)
            response_data = response.json()
            return response_data.get("data")
        except Exception as e:
            print(e)
        return None


    """
    func: send the message from the db
    """
    def send_msg(self, name, group_name, text):
        try:
            url = "http://localhost:8080/codebot/chat/msg"
            data = {
                "roomName": group_name,
                "senderName": name,
                "content": text,
                "msgType": 1
            }
            response = requests.post(url, json=data)
            response_data = response.json()
            response_id = response_data.get("data")
            # print(response_id)
            # print(response_data)
            return response_id['id']
        except Exception as e:
            print(e)
        return 'error'

    def subscribe(self, user_id:str, group_name:str):
        try:
            url = "http://localhost:8080/codebot/repo/upload"
            data = {
                "userName": user_id,
                "repoName": group_name,
            }
            response = requests.post(url, json=data)
            response_data = response.json()
            res = response_data.get("success")
            return res
        except Exception as e:
            print(e)
            return False

    def send_code(self, code):
        try:
            response = requests.get(f"http://localhost:8080/codebot/login/valid?code={code}")
            # Check if the request was successful
            if response.status_code == 200:
                # parse to json
                response_json = response.json()
                is_success = response_json['success']
                if is_success:
                    return response_json['data']
                else:
                    return None
            else:
                print(response)
                return None
        except Exception as e:
            print("An error occurred:", e)
            return None

    def call_api(self, name, text):
        try:
            url = "http://localhost:5000/api/chat"
            data = {
                "partner_name": name,
                "chat_history": [],
                "content": text
            }
            response = requests.post(url, json=data)
            response_data = response.json()
            response_value = response_data.get("response")
            # print(response_value)
            return response_value
        except Exception as e:
            print(e)
        return 'error'

    def get_auth_url(self):
        try:
            response = requests.get("http://localhost:8080/codebot/login/authorize")
            # Check if the request was successful
            if response.status_code == 200:
                # parse to json
                response_json = response.json()
                # 提取 data 字段
                data_url = response_json['data']
                return data_url
            else:
                print(response)
                return None
        except Exception as e:
            print("An error occurred:", e)


def get_groups_mock():
    return ['default', 'spring boot', 'matrix one']


GUIDE_CONVERSATION = 'Hi, I am code chat bot, what can I help you today'
def get_mes_mock():
    return [Message(
        sender='bot',
        content=GUIDE_CONVERSATION
    )]

