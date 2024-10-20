from PyQt5 import Qt
from PyQt5.QtWidgets import QDialog
from PyQt5.uic.properties import QtCore

from ui.chat_system_ui import Ui_Form
from client.chat import ChatClient
from factory.simple_factory import SimpleFactory
from domain.Message import Message
class MainPage(QDialog, Ui_Form):
    def __init__(self, user_id):
        super(MainPage, self).__init__()
        self.setupUi(self)
        self.resize(1800, 1200)
        # set the client to call backend
        self.chat_client = ChatClient()

        # user name
        self.user_id = user_id
        self.set_user_name(user_id)

        # get chat history
        # [key : List[Message]]
        self.groups = {}
        self.groups_order = []
        self.cur_group = None

        # widget factory
        self.factory =  SimpleFactory()

         # for all buttons
        self.send_btn.clicked.connect(self.on_send_clicked)
        self.add_btn.clicked.connect(self.on_add_clicked)
        self.session_list.clicked.connect(self.on_groups_clicked)

        self.init_state()

    def init_state(self):
        # get all groups
        self.load_groups()
        # get all history messages
        self.load_history_message()
        # load all group cards
        self.load_groups_card()
        # set the current group
        self.cur_group = self.groups_order[0]
        # set chat list
        self.change_bubbles_card()

    def on_add_clicked(self):
        group_name = self.search_line.text()
        if len(group_name) == 0: return
        self.search_line.clear()
        # update local db
        self.groups[group_name] = []
        # update ui
        self.add_group_card(group_name)
        # send to the server
        self.chat_client.subscribe(self.user_id, group_name)

    def on_send_clicked(self):
        text = self.input_line.toPlainText()
        message = Message('self', text)
        rep_message = self.send_message(message)
        self.add_bubble_card(message)
        self.add_bubble_card(rep_message)

    def on_groups_clicked(self):
        group_name = self.groups_order[self.session_list.currentRow()]
        self.cur_group = group_name
        self.change_bubbles_card()

    def send_message(self, message):
        # store in the local db
        self.groups[self.cur_group].append(message)
        # send to the server
        response = self.chat_client.send_msg(name=self.user_id,
                                  group_name=self.cur_group,
                                  text=message.content)
        rep_message = Message('bot', response)
        self.groups[self.cur_group].append(rep_message)
        return rep_message

    def set_user_name(self, user_name):
        self.name_label.clear()
        self.name_label.setText(user_name)
        self.user_id = user_name

    def load_groups(self):
      groups = self.chat_client.get_groups(self.user_id)
      self.groups.clear()
      self.groups_order.clear()
      for group in groups:
           self.groups_order.append(group)
           self.groups[group] = []

    def load_history_message(self):
        for group in self.groups.keys():
            self.groups[group] = self.chat_client.get_mes(self.user_id,  group)

    def load_groups_card(self) -> None:
     self.session_list.clear()
     for group in self.groups.keys():
           self.add_group_card(group_name=group)

    def change_bubbles_card(self):
      self.chat_list.clear()
      for message in self.groups[self.cur_group]:
           self.add_bubble_card(message=message)

    '''
    add group card
    '''
    def add_group_card(self, group_name: str):
     item, widget = self.factory.create_group_card(group_name)
     self.session_list.addItem(item)
     self.session_list.setItemWidget(item, widget)

    def add_bubble_card(self, message: Message):
      if message.sender == 'self':
           item, widget = self.factory.create_self_card(self.right_frame.width(), message.content)
      else:
           item, widget = self.factory.create_friend_card(self.right_frame.width(), message.content)
      self.chat_list.addItem(item)
      self.chat_list.setItemWidget(item, widget)

