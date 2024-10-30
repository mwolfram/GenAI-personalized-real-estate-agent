#!/usr/bin/env python
# coding: utf-8

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.schema import Document

from toolkit import read_listings
from toolkit import split_listings

'''
Vector database for storing and searching real estate listings and embeddings
'''
class VectorDB:

    def __init__(self):
        self.embeddings = OpenAIEmbeddings()

        listings = read_listings()
        listings = split_listings(listings)
        print(f"Number of listings: {len(listings)}")
        documents = [Document(page_content=listing) for listing in listings]
        print(f"Number of documents: {len(documents)}")
        self.db = Chroma.from_documents(documents, self.embeddings)

    def get_db(self):
        return self.db

    '''
    Search the database for similar documents based on user preferences
    '''
    def search_based_on_preferences(self, preferences):
        similar_docs = self.db.similarity_search(query=preferences, k=3)
        return similar_docs
