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
        messages.loc[self.id] = [self.id, self.user, self.text]
        messages.to_csv(MODEL_FILE, index=False)

    @classmethod
    def get_messages(cls, last_msg_id=None):
        
        messages = pd.read_csv(MODEL_FILE)

        if len(messages) > 0:
            messages_to_return = messages.loc[last_msg_id:] if last_msg_id is not None else messages.loc[0:]

            if len(messages_to_return) > 0:
                result = []
                for i in range(len(messages)):
                    result.append([messages.get_value(i,'nickname'), messages.get_value(i,'message')])

                return result
        
        return None

    @classmethod
    def get_last_msg_id(cls):
        messages = pd.read_csv(MODEL_FILE)
        return (len(messages)-1) if len(messages) != 0 else 0 

