#!/usr/bin/env python
# coding: utf-8

from toolkit import single_query_llm

print("Hello, I am your personal real estate agent. I can help you find the perfect home for you. Please tell me what you are looking for in a home.")

# Sample Q&A for the real estate agent
questions = [   
                "How big do you want your house to be?" 
                "What are 3 most important things for you in choosing this property?", 
                "Which amenities would you like?", 
                "Which transportation options are important to you?",
                "How urban do you want your neighborhood to be?",   
            ]

answers = [
    "A comfortable three-bedroom house with a spacious kitchen and a cozy living room.",
    "A quiet neighborhood, good local schools, and convenient shopping options.",
    "A backyard for gardening, a two-car garage, and a modern, energy-efficient heating system.",
    "Easy access to a reliable bus line, proximity to a major highway, and bike-friendly roads.",
    "A balance between suburban tranquility and access to urban amenities like restaurants and theaters."
    ]
# ====================================

def build_prompt_from_template(listing_file_path: str, questions: list, answers: list, input: str) -> str:
    listings_file = open(listing_file_path, "r")
    listings = listings_file.read()

    questions_and_answers = ""
    for i in range(len(questions)):
        questions_and_answers += f"Q: {questions[i]}\nA: {answers[i]}\n"

    RECOMMENDER_TEMPLATE = """The following is a friendly conversation between a human and an AI Real Estate Agent. 
                            The AI follows human instructions and provides real estate recommendations for a human based on
                            the available real estate listings and the human-provided personal questions and answers, which
                            reflect the human's preferences and focus areas. The AI Real Estate Agent will reformulate the 
                            provided real estate listings to match the human's preferences and focus areas in order to increase
                            the appeal for the real estate listing, but will NOT alter any factual information.

    Real Estate Listings:
    {listings}

    Personal Questions and Answers:
    {questions_and_answers}

    Human: {input}

    AI:"""

    return RECOMMENDER_TEMPLATE.format(listings=listings, questions_and_answers=questions_and_answers, input=input)

prompt = build_prompt_from_template("GenAI-personalized-real-estate-agent/listings", questions, answers, "I am looking for a house with a large backyard and a modern kitchen.")
recommendation = single_query_llm(prompt)
print(recommendation)

