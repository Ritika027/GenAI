from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence,RunnableParallel

load_dotenv()

prompt1 = PromptTemplate(
    template = 'Write a tweet about {topic}.',
    input_variables = ['topic']
)
prompt2 = PromptTemplate(
    template = "Write a linkedin post about {text}",
    input_variables = ['text']
)


model = ChatOpenAI()

parser = StrOutputParser()

#method 1
chain1 = RunnableSequence(prompt1,model,parser)
chain2 = RunnableSequence(prompt2,model,parser)

chain = RunnableParallel({
    "tweet":chain1,
    "linkedin":chain2
})

#method 2
parallel_chain = RunnableParallel({
    'tweet':RunnableSequence(prompt1,model,parser),
    'linkedin':RunnableSequence(prompt2,model,parser)
})
print(chain.invoke({'topic': 'AI','text':'AI'}))