import pandas as pd 
import numpy as np
import streamlit as st
import pickle



app_mode=st.sidebar.selectbox('Select Page',['Home','Prediction'])

if app_mode=='Home':
    st.title('SMARTPHONE PRICE PREDICTOR')
    st.image("Mobile price.jpg")
    st.markdown('Dataset :')
    data=pd.read_csv('ndtv_data_final.csv')
    st.write(data.head())
    
elif app_mode=='Prediction':
    st.subheader('''Please choose the specifications you are looking for in your new Smartphone!''')
    st.sidebar.header("Specifications of the Smartphone :")
    
    
    Battery=st.sidebar.selectbox('Battery capacity (mAh)', (1000,2000,3000,4000,5000))
    Screen=st.sidebar.selectbox('Screen size (inches)', (3,4,5,6,7))
    ppi=st.sidebar.slider('Pixels per inch', 125,602,0,)
    Processor=st.sidebar.selectbox('Processor', (1,2,4,6,8,10))
    RAM=st.sidebar.selectbox('RAM (MB)', (500,1000,2000,3000,4000,5000,6000,8000,12000))
    Internal=st.sidebar.selectbox('Internal storage (GB)', (1,2,3,4,8,16,32,64,128,256,512))
    R_camera=st.sidebar.slider('Rear camera (MP)', 0,108,0,)
    F_camera=st.sidebar.slider('Front camera (MP)', 0,48,0,)
    OS=st.sidebar.selectbox('Operating system', ["Android","BlackBerry","Cyanogen","SailFish","Tizen","Windows","iOS"])
    NS=st.sidebar.selectbox('Number of SIMs', (1,2,3))
    G=1
  
    if OS=="Android":
        os=0
    elif OS=="BlackBerry":
        os=1
    elif OS=="Cyanogen":
        os=2
    elif OS=="SailFish":
        os=3
    elif OS=="Tizen":
        os=4
    elif OS=="Windows":
        os=5
    elif OS=="iOS":
        os=6

    feature_list=[Battery,Screen,ppi,Processor,RAM,Internal,R_camera,F_camera,os,NS,G]      


    single_sample = np.asarray(feature_list).reshape(1,-1)

    if st.button("Predict"):
        loaded_model = pickle.load(open('rf_model.pkl', 'rb'))
        prediction = loaded_model.predict(single_sample)
        st.write("The predicted price of your Smartphone in Rs is : ",prediction)