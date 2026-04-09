from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage


load_dotenv()

model = ChatOpenAI()

#TO KEEP THE MEMORY OF USER PROMPTS AND AI RESPONSES, WE CAN USE A LIST TO STORE THE CHAT HISTORY. THIS WAY, WE CAN PASS THE ENTIRE CHAT HISTORY TO THE MODEL EACH TIME WE INVOKE IT, ALLOWING THE MODEL TO RESPOND IN CONTEXT.
chat_history = [
    SystemMessage(content = "You are a helpful assistant")
]

while True:
    input_text = input("You: ")
    chat_history.append(HumanMessage(content = input_text)) 
    if input_text.lower() == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content = result.content))
    print("AI: " ,result.content)

print(chat_history)