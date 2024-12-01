from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI

reflection_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a virtual twitter influecer grading a tweet. Generate critique and recomenndations for the user's tweet."
         "Always provde detailed recommendations, including requests for length, virality, style, and clarity."
         "Make sure to always respond originally by giving new ideas, rather than repeating the old post."),
         MessagesPlaceholder(variable_name="messages"),
    ]
)

generation_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a twitter techie influencer assistant tasked with writing excellent twitter posts."
         " Generate the best twitter post possible for the user's request"
         " If the user provides critique, respond with a revised version of the post that incorporates the critique and improves the post."),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

llm = ChatOpenAI(model="gpt-4o", temperature=1)

generate_chain = generation_prompt | llm
reflect_chain = reflection_prompt | llm

