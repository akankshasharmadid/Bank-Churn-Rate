import streamlit as st
import pandas as pd 
import pickle
import sklearn
import numpy


st.set_page_config(page_title="Bank Churn Rate", page_icon=":smiley:")

# load the model from disk
loaded_model = pickle.load(open('randomForest.sav', 'rb'))

st.header("""
Bank Churn Rate Prediction Application """)
st.header('User Input Parameters')

def user_input(loaded_model):    
    credit_score = st.slider('Select Credit Score',0,800,500)
    country = st.selectbox('Select Country',['France','Germany','Spain']) 
    gender = st.selectbox('Select Gender',['Male','Female'])
    age = st.slider('Select Age', 18,100,25)
    tenure = st.slider('Select Tenure', 0,10,4)
    balance = st.text_input('Enter your balance')
    products_number = st.selectbox('Select product number',[1,2,3,4])
    credit_card = st.selectbox('Do you have credit card',[0,1])
    active_member = st.selectbox('Is the person active member of the bank now?',[0,1]) 
    estimated_salary = st.text_input('Enter your estimated salary') 
    data = {'credit_score' : credit_score,
        'country' : country,
        'gender':gender,
        'age':age,
        'tenure' : tenure,
        'balance' : balance,
        'products_number' : products_number,
        'credit_card': credit_card,
        'active_member':active_member,
        'estimated_salary' : estimated_salary}
    df = pd.DataFrame(data ,index = [0])
    if df['country'][0] == 'France':
        df['country_France'] = 1
        df['country_Germany'] = 0
        df['country_Spain'] = 0
    elif df['country'][0] == 'Germany':
        df['country_France'] = 0
        df['country_Germany'] = 1
        df['country_Spain'] = 0
    else :
        df['country_France'] = 0
        df['country_Germany'] = 0
        df['country_Spain'] = 1
    
    if df['gender'][0] == 'Male':
        df['gender_Female'] = 0
        df['gender_Male'] = 1
    
    else:
        df['gender_Female'] = 1
        df['gender_Male'] = 0
    
    df.drop(['country', 'gender'], axis=1,inplace=True)
    
    
    return df



df = user_input(loaded_model)


st.subheader('User Input parameters')
st.write(df)
if st.button('Predict Churn rate'):
    churn = loaded_model.predict(df)
    st.success('The customer will be loyal' if churn==0 else 'The customer will churn')


