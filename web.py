import streamlit as st
import functions

todos = functions.get_todos()

st.set_page_config(layout="wide") #method to configure page.

def add_todo():# get user inputed value and add to the list of todo on the interface
    todo = st.session_state['new_todo'] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title('My Todo App')
st.subheader('This is my todo app')
st.write('<h1>This app would increase your <b>productivity</b>.</h1>', unsafe_allow_html=True) #html only allowed for the write method

st.text_input(label='', placeholder='Add a new Todo...', on_change=add_todo, key='new_todo')


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

