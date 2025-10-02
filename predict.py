# --- I need to make sure this script accepts arguments 



import joblib 

def main(text_input): 
    
    # --- loading the model 
    model = joblib.load("news_model.pkl") 
    prediction = model.predict(text_input) 
    
    print (f"The prediction is {prediction}")
    
if __name__ == '__main__': 
    main() 