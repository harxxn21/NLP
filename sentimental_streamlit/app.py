import streamlit as st 
import joblib


model=joblib.load('sentimental_streamlit/sentiment-model.pkl')

sentiment_labels={1:"Positive",0:"Negative"}

st.title('Sentiment Analysis')
user_input=st.text_area('Enter your text here:')
if st.button('Predict'):
    predicted_sentiment=model.predict([user_input])[0]
    print(predicted_sentiment)
    predicted_sentiment_label=sentiment_labels[predicted_sentiment]

    st.info(f'Predicted Sentiment: {predicted_sentiment_label}')
    
