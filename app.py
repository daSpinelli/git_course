import streamlit as st
from src.extraction import load_data

st.set_page_config(layout='wide')

def create_dataframe_section(df):
    st.title('Database Section')
    
    col_1, col_2 = st.columns(2)
    
    col_1.header('Database')
    col_1.dataframe(df, height=530)
    
    col_2.header('Data Description')
    
    data_description = '''
        | Columns | Description |
        | :------ | ----------: |
        | ID | line/record id |
        | name | manufacturer and model of the bike |
        | selling_price | selling price |
        | year | manufacturing year |
        | seller_type | seller type - personal or distributors |
        | owner | if it had only one, two three or four owners |
        | km_driven | kilometers driven with the bike |
        | ex_showroom_price | bike price without insurance and register taxes |
        | age | years os usage |
        | km_class | classification based on kilometers driven |
        | km_per_year | kilometers driven by year |
        | km_per_month | kilometer driven by month |
        | company | manufacturer |
    '''
    
    col_2.markdown(data_description)
    
    return None

def create_answers_section(df):
    st.title('Main Questions Answers')
    
    st.header('First Round')
    st.subheader('How many bikes are being sold by their owners and how many bikes are being sold by distributors?')
    st.subheader('How many bikes are being sold which has a unique owner?')
    st.subheader('Are high kilometer bikes expensiver than bikes with lower kilometer?')
    st.subheader('Are the bikes with a unique owner expensiver in average than the other bikes?')
    st.subheader('Are the bikes that have more owners also the bikes with more kilometers in average?')
    st.subheader('Which company has the most bikes registered?')
    st.subheader('Which company has the most expensive bikes in average?')
    st.subheader('Are the company that has the most expensive bikes registered also the company with the most bikes registered?')
    st.subheader('Which bikes are good for buying?')
    
    return None
    

def main():
    file = 'data/processed/bikes_completed.csv'
    df = load_data(file)
    
    create_dataframe_section(df)
    
    st.dataframe(df)

if __name__ == '__main__':
    main()