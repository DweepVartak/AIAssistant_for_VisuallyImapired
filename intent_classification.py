from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def find_most_similar(input_text, candidate_texts):
    # Combine input text and candidate texts for TF-IDF vectorization
    texts = [input_text] + candidate_texts

    # Vectorize the texts using TF-IDF
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(texts)

    # Compute cosine similarities between the input text and candidate texts
    similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()

    # Find the most similar candidate text
    most_similar_index = similarities.argmax()
    return candidate_texts[most_similar_index], similarities

# Define your input text and candidate sentences
input_text = "what object is kept in front of me"
candidate_texts = ["Read text", "Object detection"]

# Find the most similar sentence
most_similar_sentence, similarities = find_most_similar(input_text, candidate_texts)
print(f"Input text is most similar to: {most_similar_sentence}")
print(f"Similarities: {similarities}")
