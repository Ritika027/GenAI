#1.will ask prompt from user
#2.will pass the prompt to the llm and get the response
#3.get and print response


from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()



prompt = PromptTemplate(
    template = 'Generate 5 interesting facts about {topic}',
    input_variables = ['topic']
)

model = ChatOpenAI()

parser = StrOutputParser()
 #| --> pipe operator
 #chain pipeline
chain = prompt | model | parser

result = chain.invoke({'topic' : 'space'})
print(result)

chain.get_graph().print_ascii()
