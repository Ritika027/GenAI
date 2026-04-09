from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('dl-curriculum.pdf')

docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=0,
    #chunk overlap is the number of characters that will be repeated at the end of one chunk and the beginning of the next chunk. This can be useful for ensuring that important information is not lost when splitting the text into chunks.
    separator=''
    #separator is the character that will be used to split the text into chunks. In this case, we are using an empty string, which means that the text will be split into chunks of the specified size without any additional characters being added between the chunks.
)

result = splitter.split_documents(docs)

print(result[1].page_content)