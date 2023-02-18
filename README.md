# ChatGPT-simple-api

Use Firefox plugin:
https://github.com/acheong08/ChatGPT-API-agent

and api proxifier:
https://github.com/acheong08/ChatGPT-API-server

to make local ChatGPT API proxy.

When you login to chat.openai.com go here and take API token:
https://chat.openai.com/api/auth/session

Make OS environment variable:

`export CHATGPT_API_KEY="<your_api_key>"`

Then you can use this simple API:
```
from chatgpt_api import ChatGPTAPI, Conversation

api = ChatGPTAPI()
conversation = Conversation(api)
print(conversation.ask("Who you are?"))
print("====")
print(conversation.ask("Are you sure?"))
```