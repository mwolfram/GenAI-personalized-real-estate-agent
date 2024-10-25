#!/usr/bin/env python
# coding: utf-8

import os
from langchain.llms import OpenAI
from langchain.chains import ConversationChain

os.environ["OPENAI_API_KEY"] = "<voacareum_openai_api_key>"
os.environ["OPENAI_API_BASE"] = "https://openai.vocareum.com/v1"

MODEL_NAME = "gpt-3.5-turbo"
TEMPERATURE = 0.4
MAX_TOKENS = 1000

def create_llm():
    llm = OpenAI(model_name=MODEL_NAME, temperature=TEMPERATURE, max_tokens=MAX_TOKENS)
    return llm

def single_query_llm(input_text):
    llm = create_llm()
    prediction = llm.predict(input_text)
    return prediction

def get_real_estate_agent():
    llm = create_llm()
    real_estate_agent = ConversationChain(llm=llm, verbose=True)
    return real_estate_agent