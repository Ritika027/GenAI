from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini",temperature=0.9,max_completion_tokens=100)
#temperature is a parameter that controls the randomness of the model's output. A higher temperature (e.g., 0.9) will make the output more diverse and creative, while a lower temperature (e.g., 0.2) will make it more focused and deterministic.


result = model.invoke("What is the capital of India?")

