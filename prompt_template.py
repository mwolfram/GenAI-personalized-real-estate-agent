#!/usr/bin/env python
# coding: utf-8^

from langchain.prompts import PromptTemplate

'''
Generates a prompt template for the AI Real Estate Agent to follow when interacting with a human.
'''
def get_prompt_template() -> PromptTemplate:
    prompt = PromptTemplate(
        template="""
        The following is a friendly conversation between a human and an AI Real Estate Agent. 
        The AI follows human instructions and provides real estate recommendations for a human based on
        the available real estate listings and the human-provided personal questions and answers, which
        reflect the human's preferences and focus areas. The AI Real Estate Agent will reformulate the 
        provided real estate listings to match the human's preferences and focus areas in order to increase
        the appeal for the real estate listing, but will NOT alter any factual information.
        
        Relevant Real Estate Listings: 
        {input_documents}

        Personal Questions and Answers:
        {questions_and_answers}

        Human: {query}

        AI:""",
        input_variables=["input_documents", "query", "questions_and_answers"],
    )

    return prompt

'''
Generates a prompt template and also interpolates the necessary variables
'''
def get_interpolated_prompt(input_documents: str, query: str, questions_and_answers: str) -> str:
    prompt = get_prompt_template()
    return prompt.format(input_documents=input_documents, query=query, questions_and_answers=questions_and_answers)

if __name__ == "__main__":
    input_documents = "none"
    query = "I'm looking for a house that is perfect for me. Can you give me some recommendations and describe them?"
    questions_and_answers = "Q: What is the size of the house?\nA: as small as possible"
    formatted_prompt = get_interpolated_prompt(input_documents, query, questions_and_answers)
    print(formatted_prompt)