
# -------------------------------------------------------------------------
# AUTHOR: your name
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 5990 (Advanced Data Mining) - Assignment #1
# TIME SPENT: how long it took you to complete the assignment
# -----------------------------------------------------------*/
# Importing some Python libraries
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
# Defining the documents
doc1 = "soccer is my favorite sport"
doc2 = "I like sports and my favorite one is soccer"
doc3 = "support soccer at the olympic games"
doc4 = "I do like soccer, my favorite sport in the olympic games"
# Use the following words as terms to create your document-term matrix
# [soccer, favorite, sport, like, one, support, olympic, games]
# --> Add your Python code here

# List of documents
docs = [doc1, doc2, doc3, doc4]

# Set of terms
terms = ('soccer', 'favorite', 'sport', 'like',
         'one', 'support', 'olympic', 'games')
# Initializing the doc_term_matrix
doc_term_matrix = pd.DataFrame([[0 for j in range(len(terms))]
                                for i in range(len(docs))],
                               columns=terms,
                               index = ['doc1', 'doc2', 'doc3', 'doc4'])

#fill in the doc_term_matrix
for row in range(len(doc_term_matrix)):
    for col in range(len(doc_term_matrix.columns)):
        docs[row] = docs[row].replace(",", "")
        doc_term_matrix.iloc[row, col] = docs[row].split().count(terms[col])

print(doc_term_matrix)
print()

# Compare the pairwise cosine similarities and store the highest one
# Use cosine_similarity([X], [Y]) to calculate the similarities between 2 vectors
# only
# Use cosine_similarity([X, Y, Z]) to calculate the pairwise similarities between
# multiple vectors
# --> Add your Python code here
cosine_similarity_matrix = cosine_similarity(doc_term_matrix, doc_term_matrix)
print(f"Cosine similarity matrix result: \n{cosine_similarity_matrix}")

# Print the highest cosine similarity following the information below
# The most similar documents are: doc1 and doc2 with cosine similarity = x
# --> Add your Python code here
max_similarity = -1
similar_docs = set()

for i in range(cosine_similarity_matrix.shape[0]):
    for j in range(i + 1, cosine_similarity_matrix.shape[1]):
      current_cosine_similarity = cosine_similarity_matrix[i][j]
      if current_cosine_similarity > max_similarity:
        max_similarity = current_cosine_similarity
        similar_docs = (i, j)

print(f"\nDocument {similar_docs[0] + 1} and Document {similar_docs[1] + 1}", end=" ")
print("has the max cosine similarity:", max_similarity)
