#!/usr/bin/env python
# coding: utf-8^

from langchain.prompts import PromptTemplate

'''
Generates a prompt template for the AI Real Estate Agent to follow when interacting with a human.
'''
def get_prompt_template() -> PromptTemplate:
    prompt = PromptTemplate(
        template="""
        The following is a friendly conversation between a human and an AI. 
        The AI follows human instructions and provides real estate recommendations for a human based on
        the provided real estate listings and the human-provided personal personal preferences.
        The AI will first and foremost focus on the human's personal preferences and will provide real estate listings
        that reflect these preferences in order to increase their appeal. The AI shall be creative and add to the listing, 
        sticking to the original format, but it is paramount that the AI does NOT alter any factual information 
        in the real estate listings.
        
        Relevant Real Estate Listings: 
        {input_documents}

        Personal Preferences:
        {preferences}

        Human: {query}

        AI:""",
        input_variables=["input_documents", "query", "preferences"],
    )

    return prompt

'''
Generates a prompt template and also interpolates the necessary variables
'''
def get_interpolated_prompt(input_documents: str, query: str, preferences: str) -> str:
    prompt = get_prompt_template()
    return prompt.format(input_documents=input_documents, query=query, preferences=preferences)

if __name__ == "__main__":
    input_documents = "none"
    query = "I'm looking for a house that is perfect for me. Can you give me some recommendations and describe them?"
    questions_and_answers = "Q: What is the size of the house?\nA: as small as possible"
    formatted_prompt = get_interpolated_prompt(input_documents, query, questions_and_answers)
    print(formatted_prompt)