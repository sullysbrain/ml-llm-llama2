# Using Python, import all the json files in the _data folder
# and merge them into a single file called data.json

import os, json
import pandas as pd

#path_to_json = '_data/'
#json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
#print(json_files)  # for me this prints ['foo.json']


#with open('data.json', 'w') as f:
#    json.dump(data, f)

# Now, we can use the data.json file to create a Streamlit app
# that will allow us to interact with the data.

import streamlit as st
import json

with open('data.json', 'r') as f:
    data = json.load(f)

st.title('SullyGPT')
input = st.text_input('Enter a prompt:')
if input:
    text = data[input]
    st.write(text)
