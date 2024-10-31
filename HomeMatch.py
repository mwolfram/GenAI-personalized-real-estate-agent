#!/usr/bin/env python
# coding: utf-8

from vectordb import VectorDB

from toolkit import query_real_estate_agent

# DEFINE Q&A FOR REAL ESTATE AGENT ==================================
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
    "Yes, I do require a home office",
    "Access to buses, highways or airports",
    "Nothing special, a friendly and safe community is enough for me"
]
# ===== END Q&A =====================================================

# Reads the listings from a file and creates a vector database
vector_db = VectorDB()

# Query the real estate agent with a user query
query = "I'm looking for a house that meets my preferences."

# Get the result from the real estate agent
result = query_real_estate_agent(questions, answers, query, vector_db)
print(result)
