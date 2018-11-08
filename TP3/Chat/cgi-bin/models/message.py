import pandas as pd
import sys, os
from http import cookies

MODEL_FILE = 'messages.csv'

class Message():

    def __init__(self, user, text):
        self.id = None
        self.text = text
        self.user = user
    
    def save(self):
        messages = pd.read_csv(MODEL_FILE)        
        self.id = len(messages)
        messages.loc[len(messages)] = [len(messages), self.user, self.text]
        messages.to_csv(MODEL_FILE, index=False)

    @classmethod
    def get_messages(cls, last_msg_id):
        
        messages = pd.read_csv(MODEL_FILE)
        return messages[last_msg_id:]

    @classmethod
    def get_last_msg_id(cls):
        messages = pd.read_csv(MODEL_FILE)
        return len(messages)-1 if len(messages) != 0 else 0 

