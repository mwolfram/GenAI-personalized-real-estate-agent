#!/usr/bin/env python
# coding: utf-8

import os
import re
from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from langchain.chains import RetrievalQA
from langchain.chains.question_answering import load_qa_chain

from prompt_template import get_interpolated_prompt

os.environ["OPENAI_API_KEY"] = "<voacareum_openai_api_key>"
os.environ["OPENAI_API_BASE"] = "https://openai.vocareum.com/v1"

MODEL_NAME = "gpt-3.5-turbo"
TEMPERATURE = 0.0
MAX_TOKENS = 1000

'''
Access to an OpenAI LLM
'''
def create_llm():
    llm = OpenAI(model_name=MODEL_NAME, temperature=TEMPERATURE, max_tokens=MAX_TOKENS)
    return llm

'''
Get access to an LLM and send a single query to it
'''
def single_query_llm(input_text):
    llm = create_llm()
    prediction = llm.predict(input_text)
    return prediction

'''
Convert a list of questions and answers into a single string that can be passed to an LLM
'''
def qa_to_string(questions, answers):
    questions_and_answers = ""
    for i in range(len(questions)):
        questions_and_answers += f"Q: {questions[i]}\nA: {answers[i]}\n"
    return questions_and_answers

'''
Query the real estate agent with a user query, questions and answers, and a prepped vector database
'''
def query_real_estate_agent(questions, answers, query, vector_db):

    # Convert the questions and answers into a single string
    questions_and_answers = qa_to_string(questions, answers)

    # Use the LLM to get a comprehensible string of user preferences based on the questions and answers
    preferences = single_query_llm("""
        Take these questions and answers and reformat them into a short text that describes the user's preferences. Try not to include text from the questions (Q:), but rather focus on the answers (A:).
        {questions_and_answers}                 
    """.format(questions_and_answers=questions_and_answers))

    print(preferences)

    # Use the vector database to find similar documents based on the user's preferences
    similar_docs = vector_db.search_based_on_preferences(preferences)
    #print(similar_docs)

    # Generate a prompt for the real estate agent
    prompt = get_interpolated_prompt(
        input_documents=similar_docs, 
        query=query, 
        preferences=preferences)
    
    # Query the real estate agent with the prompt
    return single_query_llm(prompt)

'''
Read the listings from a file
'''
def read_listings():
    with open("GenAI-personalized-real-estate-agent/Listings.txt", "r") as listings_file:
        listings = listings_file.read()
    return listings

'''
Split the listings string into a list of individual listings, keep the LISTING tag at the beginning of each listing
'''
def split_listings(listings: str):
    listings = re.split(r'(?=^===LISTING)', listings, flags=re.MULTILINE)
    listings = [listing.strip() for listing in listings if listing.strip()]
    return listings

if __name__ == "__main__":
    #listings = read_listings()
    #listings = split_listings(listings)
    #print(listings)

    questions = [   
                "How big do you want your house to be?",
                "What are 3 most important things for you in choosing this property?", 
                "Do you require a home office?", 
                "Which transportation options are important to you?",
                "Which entertainment options are important to you?",
            ]

    answers = [
        "At least 2,200 sqft",
        "Access to a pool, top-rated schools and grocery stores",
        "Yes, definitely, I'd like to work from home",
        "Easy access to an airport is a must",
        "Nothing special, a friendly and safe community is enough for me"
    ]

    qastring = qa_to_string(questions, answers)
    print(qastring)