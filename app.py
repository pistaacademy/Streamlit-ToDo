import streamlit as st
import pandas as pd

def main():
    st.title("ToDo App with Streamlit")
    menu = ["Create", "Read", "Update", "Delete", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Create":
        st.subheader("Add Items")
        col1, col2 = st.columns(2)

        with col1:
            task = st.text_area("Task To Do")
        with col2:
            task_status = st.selectbox("Status",["ToDo", "Doing", "Done"] )
            task_due_date = st.date_input("Due Date")
        
        if st.button("Add Task"):
            st.success("Successfully Added Data: {}".format(task))
            





    elif choice == "Read":
        st.subheader("View Items")
    elif choice == "Update":
        st.subheader("Edit/Update Items")
    elif choice == "Delete":
        st.subheader("Delete Item")
    else:
        st.subheader("About")

if __name__ == '__main__':
    main()