import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nlp = spacy.load("en_core_web_sm")

def clean_text(text):
    doc = nlp(text.lower())
    tokens = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
    return ' '.join(tokens)

def rank_resumes(job_desc, resumes):
    cleaned_desc = clean_text(job_desc)
    cleaned_resumes = [clean_text(text) for text in resumes]

    corpus = [cleaned_desc] + cleaned_resumes
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)

    similarity_scores = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()
    
    return sorted(list(enumerate(similarity_scores)), key=lambda x: x[1], reverse=True)
