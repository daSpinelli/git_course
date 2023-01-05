import pandas as pd
import numpy as np
import streamlit as st

def load_data(_file):
    return pd.read_csv(_file)

def main():
    file = 'data/processed/bikes_completed.csv'
    df = load_data(file)
    st.dataframe(df)

if __name__ == '__main__':
    main()