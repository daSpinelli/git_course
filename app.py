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
        | seller_type | seller type - personal or store |
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

def main():
    file = 'data/processed/bikes_completed.csv'
    df = load_data(file)
    st.dataframe(df)

if __name__ == '__main__':
    main()