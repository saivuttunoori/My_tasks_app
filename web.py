import streamlit as st
import functions

tasks = functions.get_tasks()


def add_task():
    task = st.session_state['new_task'] +'\n'
    tasks.append((task))
    functions.write_tasks(tasks)

st.title("my task app")
st.subheader("created by Aravind")
st.write("It will increase your daily productivity")

# st.checkbox("Buy Grocery")
# st.checkbox("read")

for index,task in enumerate(tasks):
    checkBox = st.checkbox(task,key=task)
    if checkBox:
        tasks.pop(index)
        functions.write_tasks(tasks)
        del st.session_state[task]
        st.rerun()

st.text_input(label="Enter a task", on_change=add_task,
              placeholder="Add a new task", key='new_task')
