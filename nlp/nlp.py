import json
import re
import nltk
import string
import numpy as np
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from textblob import TextBlob
import os

if not os.path.exists('../src'):
    os.mkdir('../src')

def expand_contractions(text):
    contractions = {
        r"you're": "you are",
        r"i'm": "i am",
        r"he's": "he is",
        r"she's": "she is",
        r"it's": "it is",
        r"that's": "that is",
        r"what's": "what is",
        r"where's": "where is",
        r"there's": "there is",
        r"who's": "who is",
        r"i've": "i have",
        r"you've": "you have",
        r"we've": "we have",
        r"they've": "they have",
        r"i'd": "i would",
        r"you'd": "you would",
        r"he'd": "he would",
        r"she'd": "she would",
        r"we'd": "we would",
        r"they'd": "they would",
        r"i'll": "i will",
        r"you'll": "you will",
        r"he'll": "he will",
        r"she'll": "she will",
        r"we'll": "we will",
        r"they'll": "they will",
        r"isn't": "is not",
        r"aren't": "are not",
        r"wasn't": "was not",
        r"weren't": "were not",
        r"haven't": "have not",
        r"hasn't": "has not",
        r"hadn't": "had not",
        r"won't": "will not",
        r"wouldn't": "would not",
        r"don't": "do not",
        r"doesn't": "does not",
        r"didn't": "did not",
        r"can't": "cannot",
        r"couldn't": "could not",
        r"shouldn't": "should not",
        r"mightn't": "might not",
        r"mustn't": "must not"
    }

    for contraction, expansion in contractions.items():
        text = re.sub(contraction, expansion, text, flags=re.IGNORECASE)
    return text


def split_text(text, n=15):
    length = len(text)
    size = length // n
    start = 0
    pieces = []
    for i in range(n - 1):
        pieces.append(text[start:start + size])
        start += size
    pieces.append(text[start:])
    return pieces

n = 6  # You can set this to the number of sample files you have
file_names = [f'sample{i}.json' for i in range(1, n + 1)]

all_transcripts = []  # This will store transcripts from all files

for file_name in file_names:
    with open(file_name, 'r') as file:
        data = json.load(file)
        transcripts = [item['transcript'] for item in data['results']['transcripts']]
        for transcript in transcripts:
            transcript = expand_contractions(transcript)
            segments = split_text(transcript)
            sentiments = [TextBlob(segment).sentiment.polarity for segment in segments]
            plt.figure(figsize=(12, 6), dpi=600)
            plt.plot(sentiments, marker='o', linestyle='-', color='blue')
            plt.title(f'Sentiment Progression for Transcript in {file_name}')
            plt.xlabel('Segment')
            plt.ylabel('Sentiment Value')
            plt.grid(True, alpha=0.2)
            plt.tight_layout()
            plt.savefig(f'../src/sentiment_{file_name}.png', dpi=600)
            plt.show()
        
        transcripts = [expand_contractions(transcript) for transcript in transcripts]
        all_transcripts.extend(transcripts)

print(all_transcripts)
'''
for transcript in transcripts:
    print(transcript)
print("\n")
'''

stop_words = set(stopwords.words('english'))
stop_words.add('uh')
lemmatizer = WordNetLemmatizer()

def preprocess(text):

    words = word_tokenize(text)

    words_lower = [word.lower() for word in words]

    filtered_words = [word for word in words_lower if word not in stop_words]

    filtered_punctuation = [word for word in filtered_words if word not in string.punctuation]

    lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_punctuation]
    
    return ' '.join(lemmatized_words)

preprocessed_transcripts = [preprocess(t) for t in all_transcripts]

# TF
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(preprocessed_transcripts)

feature_names = vectorizer.get_feature_names_out()
term_frequencies = X.toarray().sum(axis=0)  

sorted_indices = np.argsort(term_frequencies)[::-1]
top_indices = sorted_indices[:7]
top_term_frequencies = term_frequencies[top_indices]
top_feature_names = [feature_names[i] for i in top_indices]

print("Feature Names : ", feature_names)
#print("\nAfter pre-process: ", preprocessed_transcripts)
print("\nTerm Frequencies : ", term_frequencies)
print("\n")

plt.figure(figsize=(12,6),dpi=600)
plt.bar(top_feature_names, top_term_frequencies, color='skyblue', width=0.4)
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.title('Top 7 Words by Frequency')
plt.savefig('../src/frequency.png', dpi=600)
plt.show()

# TF-IDF
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(preprocessed_transcripts)

feature_names = tfidf_vectorizer.get_feature_names_out()
tfidf_values = tfidf_matrix.toarray().sum(axis=0)

sorted_indices = np.argsort(tfidf_values)[::-1]
top_indices = sorted_indices[:7]  
top_tfidf_values = tfidf_values[top_indices]
top_feature_names = [feature_names[i] for i in top_indices]

plt.figure(figsize=(12, 6), dpi=600)
plt.bar(top_feature_names, top_tfidf_values, color='blue', width=0.4)
plt.xlabel('Words')
plt.ylabel('TF-IDF Score')
plt.title('Top 7 Words by TF-IDF Score')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('../src/tfidf.png', dpi=600)
plt.show()


with open('word_list.json', 'r') as file:
    emergency_word = json.load(file)
    
print("emergency_word: ",emergency_word)

filtered_indices = np.where(np.isin(feature_names, emergency_word))[0]
filtered_term_frequencies = term_frequencies[filtered_indices]
filtered_feature_names = feature_names[filtered_indices]

sorted_idx = np.argsort(filtered_term_frequencies)[::-1]
sorted_term_frequencies = filtered_term_frequencies[sorted_idx]
sorted_feature_names = filtered_feature_names[sorted_idx]

plt.figure(figsize=(12,6),dpi=600)
plt.bar(sorted_feature_names, sorted_term_frequencies, color='coral', width=0.4)  
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.title('Emergency Words by Frequency')
#plt.xticks(rotation=45)  
plt.tight_layout()  
plt.savefig('../src/emergency word.png', dpi=600)
plt.show()


# Emergency Words by TF-IDF
filtered_tfidf_indices = np.where(np.isin(feature_names, emergency_word))[0]
filtered_tfidf_values = tfidf_values[filtered_tfidf_indices]

sorted_tfidf_indices = np.argsort(filtered_tfidf_values)[::-1]
sorted_tfidf_values = filtered_tfidf_values[sorted_tfidf_indices]
sorted_feature_names_tfidf = feature_names[filtered_tfidf_indices][sorted_tfidf_indices]

plt.figure(figsize=(12,6),dpi=600)
plt.bar(sorted_feature_names_tfidf, sorted_tfidf_values, color='purple', width=0.4)  
plt.xlabel('Words')
plt.ylabel('TF-IDF Score')
plt.title('Emergency Words by TF-IDF Score')
plt.tight_layout()
plt.savefig('../src/emergency word tfidf.png', dpi=600)
plt.show()


# bigrams and trigrams analysis
ngram_ranges = [(2, 2), (3, 3)]  # Represents bi-grams and trigrams
titles = ["Top 7 Bigrams by Frequency", "Top 7 Trigrams by Frequency"]
labels = ["Bigrams", "Trigrams"]

for idx, ngram_range in enumerate(ngram_ranges):
    vectorizer = CountVectorizer(ngram_range=ngram_range)
    X = vectorizer.fit_transform(preprocessed_transcripts)
    feature_names = vectorizer.get_feature_names_out()
    term_frequencies = X.toarray().sum(axis=0)
    sorted_indices = np.argsort(term_frequencies)[::-1]
    top_indices = sorted_indices[:7]
    top_term_frequencies = term_frequencies[top_indices]
    top_feature_names = [feature_names[i] for i in top_indices]

    plt.figure(figsize=(12, 6), dpi=600)
    plt.bar(top_feature_names, top_term_frequencies, color='green', width=0.4)
    plt.xlabel(labels[idx])
    plt.ylabel('Frequency')
    plt.title(titles[idx])
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f'../src/{labels[idx]}.png', dpi=600)
    plt.show()
