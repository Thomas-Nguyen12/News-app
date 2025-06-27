import pytest
import unittest
import pandas as pd 
import re

from news_model import load_data
from news_model import clean_data
from news_model import extract_topics

# i need to import the modules


@pytest.fixture
def load_dataset(): 
    df = pd.read_csv("scraped_news.csv")
    return df 

def test_raw_dataset_loaded(): 
    assert load_data is not None, "there should be a dataset loaded"
    



def test_column_number(load_dataset):
    
    assert clean_data(load_dataset).shape[1] == 2, "There should be two columns. Topic and text"


def test_missing_rows(load_dataset): 
    assert clean_data(load_dataset).isna().sum().sum() == 0, "There should be no missing values. Especially in the topic column"



def test_edit_history_watch(load_dataset): 
    assert re.search("edit,history,watch,", str(clean_data(load_dataset).text)) is None, "There should be no edit,history,watch at the beginning of each text"


def test_extracted_topic_year(load_dataset): 
    
    """ 
    I can check the dtypes of the columns
    
    """
    
    assert extract_topics(clean_data(load_dataset)).year.dtypes == 'int32'

# I can also check if the clean dataset also has 
def test_extracted_topic_year_month(load_dataset): 
    assert extract_topics(clean_data(load_dataset)).shape[1] == 5, "There should be 5 columns"

def test_extracted_topic_month(load_dataset):
    assert extract_topics(clean_data(load_dataset)).month.dtypes == 'int32'

def test_extracted_topic_count(load_dataset):
    assert extract_topics(clean_data(load_dataset))['count'].dtypes == 'int64', "This should be numeric"

def test_extracted_topic_topic(load_dataset): 
    
    """ 
    I can check for:
    1. trailing white spaces
    2. the first letter is a capital letter 
    3. The nuber of unique topic names
    
    """
    
    
    assert len(extract_topics(clean_data(load_dataset)).topic.unique()) == 26, "There should be 26 news categories"
    
    
def test_extracted_topic_columns(load_dataset):
    assert extract_topics(clean_data(load_dataset)).columns.is_unique == True, "The columns should be unique"

def test_extracted_topic_year_month(load_dataset):
    pass
