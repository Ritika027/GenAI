from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Optional,li

load_dotenv()

model = ChatOpenAI()


#schema

class Review(TypedDict):
    key_themes: Annotated[str,"The main themes or topics discussed in the review, such as performance, camera quality, battery life, etc."]
    summary: Annotated[str,"A concise summary of the review in one or two sentences."]
    sentiments: Annotated[int,"The sentiment of the review as a number between -1 and 1, where -1 is very negative, 0 is neutral, and 1 is very positive."]
    pros:Annotated[Optional[list[str]],"A list of positive aspects mentioned in the review, if any."]
    cons:Annotated[Optional[list[str]],"A list of negative aspects mentioned in the review, if any."]
 

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful
                                 
Review by Ritika Jhajharia
""")

print(result)
print(result['summary'])
print(result['sentiments'])



















