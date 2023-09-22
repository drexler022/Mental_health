import json
import re
import nltk
import string
import numpy as np
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer

# 展开缩写
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

with open('asrOutput_2.json', 'r') as file:
    data = json.load(file)

transcripts = [item['transcript'] for item in data['results']['transcripts']]
transcripts = [expand_contractions(transcript) for transcript in transcripts]

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
term_frequencies = X.toarray().sum(axis=0)  


sorted_indices = np.argsort(term_frequencies)[::-1]
top_indices = sorted_indices[:7]
top_term_frequencies = term_frequencies[top_indices]
top_feature_names = [feature_names[i] for i in top_indices]


print("Feature Names : ", feature_names)
print("\nAfter pre-process: ", preprocessed_transcripts)
print("\nTerm Frequencies : ", term_frequencies)

plt.figure(figsize=(12,6),dpi=600)
plt.bar(top_feature_names, top_term_frequencies, color='skyblue')
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.title('Top 7 Words by Frequency')
plt.show()

with open('word_list.json', 'r') as file:
    emergency_word = json.load(file)
    
print(emergency_word)


filtered_indices = np.where(np.isin(feature_names, emergency_word))[0]
filtered_term_frequencies = term_frequencies[filtered_indices]
filtered_feature_names = feature_names[filtered_indices]


sorted_idx = np.argsort(filtered_term_frequencies)[::-1]
sorted_term_frequencies = filtered_term_frequencies[sorted_idx]
sorted_feature_names = filtered_feature_names[sorted_idx]


plt.figure(figsize=(12,6),dpi=600)
plt.bar(sorted_feature_names, sorted_term_frequencies, color='coral', width=0.2)  
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.title('Emergency Words by Frequency')
#plt.xticks(rotation=45)  
plt.tight_layout()  
plt.show()

# bigrams analysis
vectorizer_bigrams = CountVectorizer(ngram_range=(2, 2))
X_bigrams = vectorizer_bigrams.fit_transform(preprocessed_transcripts)
feature_names_bigrams = vectorizer_bigrams.get_feature_names_out()
term_frequencies_bigrams = X_bigrams.toarray().sum(axis=0)
sorted_indices_bigrams = np.argsort(term_frequencies_bigrams)[::-1]
top_indices_bigrams = sorted_indices_bigrams[:7]
top_term_frequencies_bigrams = term_frequencies_bigrams[top_indices_bigrams]
top_feature_names_bigrams = [feature_names_bigrams[i] for i in top_indices_bigrams]

plt.figure(figsize=(12,6),dpi=600)
plt.bar(top_feature_names_bigrams, top_term_frequencies_bigrams, color='green', width=0.4)
plt.xlabel('Bigrams')
plt.ylabel('Frequency')
plt.title('Top 7 Bigrams by Frequency')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

