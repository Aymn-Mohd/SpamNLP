import streamlit as st
import pickle
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import string

nltk.download('stopwords')  # Download stopwords
stm = PorterStemmer()
stopwords_set = set(stopwords.words('english'))

tfidf = pickle.load(open('Vectorizer.pkl', 'rb'))
model = pickle.load(open('Model.pkl', 'rb'))

st.title('Spam/Ham Classifier using NLP')
st.header('Enter the mail text to check if it is Spam or Ham')
email = st.text_area('Enter the mail text')


def preprocessvector(email_input):
    email_text = email_input.lower().translate(str.maketrans('', '', string.punctuation)).split()
    email_text = [stm.stem(word) for word in email_text if word not in stopwords_set]
    email_text = ' '.join(email_text)
    email_corpus = [email_text]
    print(email_corpus)
    email_transformed = tfidf.transform(email_corpus)
    return email_transformed


if st.button('Predict'):
    print('Button clicked')
    X_email = preprocessvector(email)
    result = model.predict(X_email)
    print(result[0])
    if result[0] == 1:
        st.header('Spam')
    else:
        st.header('Ham')
