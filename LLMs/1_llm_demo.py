from langchain_openai import OpenAI
from dotenv import load_dotenv

#loading API key from .env file of openAI
load_dotenv()

#creating an instance/object of the OpenAI class and specifying the model to be used for generating responses. In this case, we are using the "gpt-3.5-turbo-instruct" model.
llm = OpenAI(model="gpt-3.5-turbo-instruct")
#invoke function to get response from the model , to communicate with the model we need to use the invoke function
result = llm.invoke("What is the capital of India?")
#this invoke will hit the model mentioned in the model parameter and will return the response for the question asked in the invoke function.
#that model will process the question and reply will be generated
print(result)