import streamlit as st
from src.extraction import load_data

st.set_page_config(layout='wide')

def main():
    file = 'data/processed/bikes_completed.csv'
    df = load_data(file)
    st.dataframe(df)

if __name__ == '__main__':
    main()