from langchain_antropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model="claude-2",temperature=0.9,max_completion_tokens=100)
result = model.invoke("What is the capital of India?")
print(result)
