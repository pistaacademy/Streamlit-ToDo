import streamlit as st
import pandas as pd
import plotly.express as px

from db_fxns import create_table, add_data, view_all_data,view_unique_task, get_task

def main():
    st.title("ToDo App with Streamlit")
    menu = ["Create", "Read", "Update", "Delete", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    create_table()

    if choice == "Create":
        st.subheader("Add Items")
        col1, col2 = st.columns(2)

        with col1:
            task = st.text_area("Task To Do")
        with col2:
            task_status = st.selectbox("Status",["ToDo", "Doing", "Done"] )
            task_due_date = st.date_input("Due Date")
        
        if st.button("Add Task"):
            add_data(task, task_status, task_due_date)
            st.success("Successfully Added Data: {}".format(task))






    elif choice == "Read":
        st.subheader("View Items")
        result = view_all_data()
        df = pd.DataFrame(result, columns=['Task', 'Status', "Due Date"])
        with st.expander("View All Data"):
            st.dataframe(df)
        with st.expander("Task Status"):
            task_df =df['Status'].value_counts().to_frame()
            task_df = task_df.reset_index()
            st.dataframe(task_df)

            p1 = px.pie(task_df, names='index', values='Status')
            st.plotly_chart(p1)

    elif choice == "Update":
        st.subheader("Edit/Update Items")
        result = view_all_data()
        df = pd.DataFrame(result, columns=['Task', 'Status', "Due Date"])
        with st.expander("Current Data"):
            st.dataframe(df)
        
        list_of_task = [i[0] for i in view_unique_task()]
        selected_task = st.selectbox("Task To Edit", list_of_task)
        selected_result = get_task(selected_task)
        if selected_result:
            task = selected_result[0][0]
            task_status = selected_result[0][1]
            task_due_date = selected_result[0][2]

            col1, col2 = st.columns(2)

            with col1:
                new_task = st.text_area("Task To Do", task)
            with col2:
                new_task_status = st.selectbox(task_status, ["ToDo", "Doing", "Done"])
                new_task_due_date = st.date_input(task_due_date)
            if st.button("Update Task"):
                st.success("Successfully Updated Data:{}".format(task))




    elif choice == "Delete":
        st.subheader("Delete Item")
    else:
        st.subheader("About")

if __name__ == '__main__':
    main()