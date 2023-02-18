# Define enviroment variable CHATGPT_API_KEY 
# with API key from https://chat.openai.com/api/auth/session

from dataclasses import dataclass
from typing import Optional, List
import os
import requests


@dataclass
class ChatAnswer:
    id: Optional[str] = None
    response_id: Optional[str] = None
    conversation_id: Optional[str] = None
    content: Optional[str] = None
    error: Optional[str] = None


class ChatGPTAPI:

    def __init__(self):
        self.base_url = 'http://localhost:8080/api'
        self.headers = {'Authorization': os.environ['CHATGPT_API_KEY']}
        
    def _post_request(self, endpoint, payload):
        url = f"{self.base_url}/{endpoint}"
        response = requests.post(url, headers=self.headers, json=payload)
        return response.json()

    def ask(self, content, conversation_id=None, parent_id=None):
        assert conversation_id is None and parent_id is None or \
            conversation_id is not None and parent_id is not None, \
                "Указываить надо conversation_id и parent_id одновременно."

        payload = {
            "content": content,
        }
        if conversation_id is not None and parent_id is not None:
            payload.update(
                conversation_id=conversation_id,
                parent_id=parent_id
                )

        ret = self._post_request("ask", payload)
        return ChatAnswer(**ret)


class Conversation:
    def __init__(self, api, history: Optional[List[ChatAnswer]]=None):
        self.api = api
        self.history = history or []

    def ask(self, content: str)-> str:
        if not self.history:
            ans = self.api.ask(content)
        else:
            prev_ans = self.history[-1]
            ans = self.api.ask(
                content, 
                conversation_id=prev_ans.conversation_id, 
                parent_id=prev_ans.response_id
                )
        self.history.append(ans)

        return ans.content


# Define enviroment variable CHATGPT_API_KEY 
# with API key from https://chat.openai.com/api/auth/session

# api = ChatGPTAPI()
# conversation = Conversation(api)
# print(conversation.ask("Who it are?"))
