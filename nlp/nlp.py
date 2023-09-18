import json
import nltk
import string
import numpy as np
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer


with open('asrOutput_2.json', 'r') as file:
    data = json.load(file)


transcripts = [item['transcript'] for item in data['results']['transcripts']]


for transcript in transcripts:
    print(transcript)
print("\n")


stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def preprocess(text):

    words = word_tokenize(text)
    

    words_lower = [word.lower() for word in words]
    

    filtered_words = [word for word in words_lower if word not in stop_words]
    

    filtered_punctuation = [word for word in filtered_words if word not in string.punctuation]
    

    lemmatized_words = [lemmatizer.lemmatize(word, 'v') for word in filtered_punctuation]
    
    return ' '.join(lemmatized_words)


preprocessed_transcripts = [preprocess(t) for t in transcripts]


vectorizer = CountVectorizer()
X = vectorizer.fit_transform(preprocessed_transcripts)


feature_names = vectorizer.get_feature_names_out()
term_frequencies = X.toarray().sum(axis=0)  # 对所有文档进行词频汇总


sorted_indices = np.argsort(term_frequencies)[::-1]
top_indices = sorted_indices[:7]
top_term_frequencies = term_frequencies[top_indices]
top_feature_names = [feature_names[i] for i in top_indices]


print("Feature Names : ", feature_names)
print("\nAfter pre-process: ", preprocessed_transcripts)
print("\nTerm Frequencies : ", term_frequencies)


plt.figure(figsize=(12,6))
plt.bar(top_feature_names, top_term_frequencies, color='skyblue')
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.title('Top 7 Words by Frequency')
plt.show()
