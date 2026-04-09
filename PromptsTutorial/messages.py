
#IT IS TO SOLVE PROBLEM THAT IN CHAT HISTORY IN CHATBOT WE WERE NOT GETTING LABELED HISTORY 
#FOR LARGE DATA IT WOULD BE DIFFICULT TO IDENTIFY WHICH MESSAGE IS FROM USER AND WHICH IS FROM AI, SO WE CAN USE THE MESSAGE CLASSES TO LABEL THE MESSAGES IN THE CHAT HISTORY. THIS WAY, WE CAN EASILY IDENTIFY THE SOURCE OF EACH MESSAGE AND MAINTAIN A CLEAR CONVERSATION FLOW.


from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

#HUMAN MESSAGE:MESSAGES THAT REPRESENT THE USER'S INPUT OR PROMPTS TO THE MODEL.
#AI MESSAGE: MESSAGES THAT REPRESENT THE MODEL'S RESPONSES OR OUTPUTS.
#SYSTEM MESSAGE: MESSAGES THAT PROVIDE CONTEXT OR INSTRUCTIONS TO THE MODEL, BUT

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

messages = [
    SystemMessage(content = "You are a helpful assistant"),
    HumanMessage(content = "What is langchain?")
]

result = model.invoke(messages)
messages.append(AIMessage(content = result.content))

print(messages)
