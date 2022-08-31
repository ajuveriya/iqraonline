import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
#import seaborn as sns
import streamlit as st
#from sklearn.model_selection import train_test_split
#from sklearn.svm import SVC
#from tabulate import tabulate
income_df = pd.read_csv("kareemincome.csv")
expenditure_df=pd.read_csv("kareemexpenditure.csv")
st.title("IQRAA SCHOOL ONLINE INCOME 2022")
st.sidebar.title("SCHOOL INCOME DETAILS")
if st.sidebar.checkbox("Show complete details"):
    st.subheader("KAREEMUDDIN ACCOUNT DETAILS")
    df = pd.DataFrame([
    ['INCOME', 'EXPENDITURE','BALANCE'],[1576451,658179,918278]])
    st.table(df)
    #st.dataframe(school_df)
    #st.write("January Income 2022: 250630")
    #st.write("January Expenditure 2022: 242644")
    #table = [['S.NO', 'NAME','INCOME', 'EXPENDITURE','BALANCE'], [1, 'QADEER PASHA', 250630,242644,7986], [2, 'KAREEMUDDIN',60370 ,47744,12626], [3, 'ARJ',73000 ,0,73000],[4, 'TOTAL',384000,	290388,73000]]
    

st.sidebar.subheader("Income and Expenditure Details")
plot_types = st.sidebar.multiselect("Select the Month:", 
                                    ('Income', 'Expenditure'))
if 'Income' in plot_types:
    st.subheader("Income Online")
    st.dataframe(income_df)
    
    

if 'Expenditure' in plot_types:
    st.subheader("Exenditure Online")
    st.dataframe(expenditure_df)
   
