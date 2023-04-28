import streamlit as st
import functions
import datetime
from datetime import date
import pandas as pd

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)



st.title("Daily Task Tracker")
st.subheader("This is a work in progress.")
st.write("This app is designed to increase productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

# input the task
st.text_input(label="Add A New Task", placeholder="...",
              on_change=add_todo, key='new_todo')

start_date = st.date_input("Start Date", value=pd.to_datetime("today", format="%Y-%m-%d"))
end_date = st.date_input("End Date", value=pd.to_datetime("today", format="%Y-%m-%d"))

# convert the dates to string
start = start_date.strftime("%Y-%m-%d")
end = end_date.strftime("%Y-%m-%d")

