from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence

load_dotenv()

#Create a prompt template
prompt = PromptTemplate(
    template = 'Write a joke about {topic}.',
    input_variables = ['topic']
)

prompt2 = PromptTemplate(
    template = "Explain the following joke - {text}",
    input_variables = ['text']
)
model = ChatOpenAI()


parser  = StrOutputParser()

#create a chain

chain = RunnableSequence(prompt,model, parser,prompt2,model,parser)

print(chain.invoke({'topic': 'AI'}))
