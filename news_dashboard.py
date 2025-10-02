import streamlit as st 
import pickle
import joblib 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
from skmultilearn.problem_transform import BinaryRelevance

## importing the model. This takes one parameter: "content"
news_model = joblib.load("news_model.pkl")


# clean_df will contain the date and text 
clean_df = pd.read_csv("clean_df.csv") 
clean_df.drop(['Unnamed: 0'], axis=1, inplace=True)

# extracted topics will contain the numerical count information for topics and dates 
extracted_topics = pd.read_csv("extracted_topics.csv") 
extracted_topics.drop(['Unnamed: 0'], axis=1, inplace=True)


vectoriser = joblib.load("tfidf_vectoriser")

""" 
This script will be the main streamlit dashboard for the news classification app. 

I will need to import the dataset

I can include: 
    1. trends
    2. distributions 
    3. Predicted future trends
    4. latest news reports
    
Perhaps I can include a world map of the news reports 
"""

st.title("World News Dashboard") 


st.subheader("Sources are from Wikipedia current events portal")


# The first two columns here will be for visualisation

left, right = st.columns(2) 

# In this column, I can include the count data (extracted_topics) and its trends over itme
# I can also include a select box so that user can select the topic 
with right:
    st.header("News reports over time")
    
    topic_options = extracted_topics['topic'].unique() 
    chosen_topic = st.selectbox("Choose a news topic: " (topic_options),)
    st.write(f"You have chosen: {chosen_topic}") 
    
    # filtering data to the chosen topic
    chosen_topic_df = extracted_topics[extracted_topics.topic == chosen_topic]
    
    # visualising the data
    st.line_chart(data=chosen_topic_df, x='year_month', y='count')
    

with left: 
    # This can show the distribution of topics 
    # Alternatively, It can show the latest news reports
    
    st.header("Latest news reports")
    
    st.subheader(clean_df.tail(1).topic)
    
    st.write(clean_df.tail(1).text)  
    

with st.container: 
    # Here, I can apply the predictive model for news classification 
    # I can use an input box
    # This will be a chatGPT-style format where the model can predict the type of 
    # news report contained within the inputted text
    
    
    prompt = st.chat_input("Enter your news report!")

    if prompt: 
        st.write("Processing...") 
        
        # preprocessing the text prior to model prediction
        prompt_transformed = vectoriser.transform(prompt) 
        
        
        
        prediction = news_model.predict([prompt_transformed]) 
        
        # I need a way to convert the prediction to a word format. 
        

