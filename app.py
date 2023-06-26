import chainlit as cl
from langchain import OpenAI,PromptTemplate,LLMChain
from constants import openai_key,serfapi_key
import os
from chainlit import langchain_factory


os.environ["OPENAI_API_KEY"]=openai_key



template = """Question: {question}

Answer: Let's think step by step."""

@cl.langchain_factory(use_async=True)
def factory():
    prompt = PromptTemplate(template=template, input_variables=["question"])
    llm_chain = LLMChain(prompt=prompt, llm=OpenAI(temperature=0), verbose=True)

    return llm_chain


