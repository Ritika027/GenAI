from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
#Using runnables parallel chain we can run multiple chains in parallel and then combine the results using a final chain


load_dotenv()

model1 = ChatOpenAI()
model2 = ChatOpenAI()

prompt1 = PromptTemplate(
    template = 'Generate short and simple notes from the following text \n {text}',
    input_variables = ['text']
)


prompt2 = PromptTemplate(
    template = 'Generate 5 short questions from the following text \n {text}',
    input_variables = ['text']
)

prompt3 = PromptTemplate(
    template = 'merge the provides notes and quiz into single document \n {notes} and quiz {quiz}',
    input_variables = ['notes', 'quiz']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'notes' : prompt1 | model1 | parser,
    'quiz' : prompt2 | model2 | parser
})

#logic for merging the results of the parallel chains

final_chain = prompt3 | model1 | parser

chain = parallel_chain | final_chain


text = "Climate change refers to long-term shifts in temperatures and weather patterns, primarily caused by human activities such as burning fossil fuels, deforestation, and industrial processes. These activities release greenhouse gases into the atmosphere, leading to global warming and a range of environmental impacts, including rising sea levels, more frequent extreme weather events, and disruptions to ecosystems. Addressing climate change requires global cooperation and efforts to reduce emissions, transition to renewable energy sources, and implement sustainable practices across various sectors."
result = chain.invoke({"text": text})

print(result)
chain.get_graph().print_ascii()