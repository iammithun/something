# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 16:58:37 2024

@author: iamrs
"""

from googlesearch import search

def get_google_results(query, num_results=5):
    try:
  
        search_results = search(query, num_results=num_results, stop=num_results, pause=2)
        return search_results
    except Exception as e:
        print("An error occurred:", str(e))
        return []

query = "What is the capital of France?"
num_results = 3
results = get_google_results(query, num_results)


for i, result in enumerate(results, start=1):
    print(f"Result {i}: {result}")
