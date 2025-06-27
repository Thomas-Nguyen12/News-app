#!/usr/bin/env python3
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
from sklearn.model_selection import train_test_split 

""" 
This program will build a model for my news data to predict
trends over time 
"""





def load_data(): 
    df = pd.read_csv("/Users/thomasnguyen/news_project/scraped_news.csv")
    # 1. checking for 
    """
    CLEANING:
    1. missing values
    2. erroeneous data
        - This can include rows that have [removed] 
    3. column names
    
    I can use the scikit-learn column transformer and pipeline modules
    
    
    ENCODING
    - for this, I should have already used PCA in my exploratory data anlaysis 
    
    
    """
    return df 


def clean_data(data): 
    
    # removing the missing row (by date) 
    data.index = pd.to_datetime(data.date) 
    
    
    # dropping the unecessary column 
    
    # removing the "edit, history, watch" 
    
    
    
    # removing the row with the missing data (June 2, 2025). I first need to identify this row. Cleaned format is year, month, day
    # I need to
    # i need to detect the rows that have missing topics or 
    
    
    row_to_remove = data[data.text == "edit,history,watch"].index
    data = data.drop(row_to_remove, axis=0)
    
    data.drop(['date'], axis=1, inplace=True)
    # 
    
    data.text = data.text.str.replace("^edit,history,watch,", "", regex=True) 
    return data 
    
    
    
def extract_topics(new_df): 
    # I can extract the topic for each row and keep the date
    # To do this, I should keep track of how many topics there are and match the number of years
    # i can use tuples to do this 
    
    new_df['topic_cleaned'] = new_df.topic.str.split(",") 

    new_df2 = new_df.drop(['text'], axis=1)
    new_df2['date'] = new_df2.index
    exploded_df = new_df2.explode('topic_cleaned')

    # Select only the date and the individual topic
    result_df = exploded_df[['date', 'topic_cleaned']].rename(columns={'topic_cleaned': 'topic'})
    print ("Result df")
    print(result_df)
    result_df = pd.DataFrame(result_df)
    result_df_grouped = result_df.groupby([result_df.index.year, result_df.index.month, result_df.topic])['topic'].count()

    result_df_grouped_df = pd.DataFrame(result_df_grouped)
    result_df_grouped_df.rename({"topic": "count"}, axis=1, inplace=True)
    # Step 1: Rename duplicate index levels (if necessary)
    result_df_grouped_df.index.set_names(['year', 'month', 'topic'], inplace=True)

    # Step 2: Reset the index
    flat_df = result_df_grouped_df.reset_index()

    # Now you have columns: 'year', 'month', 'topic', 'count'
    print(flat_df.head())
    flat_df['sep'] = '-' 

    flat_df['year_month'] = pd.concat([flat_df.year, flat_df['sep'], flat_df.month], ignore_index=True)
    flat_df['year_month'] = flat_df['year'].astype(str) + '-' + flat_df['month'].astype(str).str.zfill(2)
    flat_df.drop(['sep'], axis=1, inplace=True)
    
    return flat_df

def extract_text(data): 
    pass 

    
    


def preprocess_data(data): 
    
    """ 
    The objective is to track news data over time 
    
    """
    
    pass



def build_model(): 
    """
    1. 
    
    """
    pass
    




