import sqlite3
conn = sqlite3.connect("data.db")
c = conn.cursor()



def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS taskstable(task TEXT, task_status TEXT, task_due_date DATE)')
def add_data(task, task_status, task_due_date):
    c.execute('INSERT INTO taskstable(task, task_status, task_due_date) VALUES (?,?,?)',(task, task_status, task_due_date))
    conn.commit()
