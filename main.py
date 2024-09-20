import pandas as pd

def load_data():
    global credit_cards_df, emails_df, hospitals_df, shopping_df, schools_df
    #Load datasets  
    credit_cards_df = pd.read_csv("credit_cards_full_context.csv")
    emails_df = pd.read_csv("emails_full_context.csv")
    hospitals_df = pd.read_csv("hospitals_full_context.csv")
    schools_df = pd.read_csv("schools_full_context.csv")
    shopping_df = pd.read_csv("shopping_with_context.csv")


    # #Inspect to the datasets
    # print(credit_cards_df.head(), end="\n\n")
    # print(emails_df.head(), end="\n\n")
    # print(hospitals_df.head(), end="\n\n")
    # print(schools_df.head(), end="\n\n")
    # print(shopping_df.head(), end="\n\n")

def clean_the_data():
    # Drop duplicates
    credit_cards_df.drop_duplicates(inplace=True)
    emails_df.drop_duplicates(inplace=True)
    hospitals_df.drop_duplicates(inplace=True)
    schools_df.drop_duplicates(inplace=True)
    shopping_df.drop_duplicates(inplace=True)
    
    # Handling missing values
    # credit_cards_df.fillna(credit_cards_df.median(), inplace=True)
    # emails_df.fillna({'Spam_Flag': 0, 'Read_Status': 0}, inplace=True)
    # hospitals_df.dropna(subset=['Patient_Satisfaction'], inplace=True)
    # schools_df.fillna(method='ffill', inplace=True)
    
    # B/c the null values are keys then we need to drop it instead of fill it
    shopping_df.dropna(subset=['ProductID', 'Price'], inplace=True)


    #Check df-s
    # print(credit_cards_df.info(), end="\n\n")
    # print(emails_df.info(), end="\n\n")
    # print(hospitals_df.info(), end="\n\n")
    # print(schools_df.info(), end="\n\n")
    # print(shopping_df.info())
def main():
    load_data()
    clean_the_data()
    

if __name__ == "__main__":
    main()