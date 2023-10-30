import langchain_helper as lch
import streamlit as st

st.title('Pets name generator')

animal_type = st.sidebar.selectbox("What is your 
pet?",("cat","hen","dog","cow"))

if animal_type == 'cat':
  pet_color = st.sidebar.text_area("What is the color of your 
cat?",max_chars=15)
if animal_type == 'dog':
  pet_color = st.sidebar.text_area("What is the color of your 
dog?",max_chars=15)
if animal_type == 'cow':
  pet_color = st.sidebar.text_area("What is the color of your 
cow?",max_chars=15)

 
if pet_color:
  response = lch.generate_pet_name(animal_type,pet_color)
  st.text(response)
