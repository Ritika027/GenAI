from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='books',
    glob='*.pdf',
    #glob represents the pattern to match files, in this case, all PDF files in the directory
    loader_cls=PyPDFLoader
)

#use lazy_load to load documents one at a time, which is more memory efficient for large directories
docs = loader.lazy_load()

for document in docs:
    print(document.metadata)