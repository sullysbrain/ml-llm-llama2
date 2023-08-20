import streamlit as st

from langchain.utilities import WikipediaAPIWrapper
from langchain.agents import load_tools, initialize_agent, AgentType
from langchain.llms import OpenAI 

import os
import sys
sys.path.append('_private/')
from _private import api
os.environ['OPENAI_API_KEY'] = api.API_KEY

# Init the LLM and Tools
llm = OpenAI(temperature=0)
tools = load_tools(['wikipedia'], llm=llm)
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

# collect user prompt
st.title('SullyGPT')
input = st.text_input('Enter a prompt:')

if input:
    text = agent.run(input)
    st.write(text)
