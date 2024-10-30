#!/usr/bin/env python
# coding: utf-8

from vectordb import VectorDB

from toolkit import query_real_estate_agent

# DEFINE Q&A FOR REAL ESTATE AGENT

# Sample Q&A for the real estate agent
# questions = [   
#                 "How big do you want your house to be?" 
#                 "What are 3 most important things for you in choosing this property?", 
#                 "Which amenities would you like?", 
#                 "Which transportation options are important to you?",
#                 "How urban do you want your neighborhood to be?",   
#             ]

# answers = [
#     "A comfortable three-bedroom house with a spacious kitchen and a cozy living room.",
#     "A quiet neighborhood, good local schools, and convenient shopping options.",
#     "A backyard for gardening, a two-car garage, and a modern, energy-efficient heating system.",
#     "Easy access to a reliable bus line, proximity to a major highway, and bike-friendly roads.",
#     "A balance between suburban tranquility and access to urban amenities like restaurants and theaters."
#     ]

questions = [   
                "How big do you want your house to be?" 
                "What are 3 most important things for you in choosing this property?", 
                "Which amenities would you like?", 
                "Which transportation options are important to you?",
                "How urban do you want your neighborhood to be?",   
            ]

answers = [
    "as small as possible",
    "loud neighborhood, busy streets, and no shopping options",
    "a toilet, a sink, and a shower",
    "access to trains",
    "Very urban, I want to live next to a thai restaurant"
]

# =====================================================

# Reads the listings from a file and creates a vector database
vector_db = VectorDB()

# Query the real estate agent with a user query
query = "I'm looking for a house that is perfect for me. Can you give me some recommendations and describe them?"

# Get the result from the real estate agent
result = query_real_estate_agent(questions, answers, query, vector_db)
print(result)
