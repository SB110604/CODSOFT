import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3 as sql

# Function to add tasks to the list
def add_new_task():
    task_text = task_input.get()
    if not task_text:
        messagebox.showinfo('Error', 'Field is Empty.')
    else:
        task_list.append(task_text)
        db_cursor.execute('INSERT INTO tasks (title) VALUES (?)', (task_text,))
        refresh_task_list()
        task_input.delete(0, 'end')

# Function to refresh the task list in the listbox
def refresh_task_list():
    clear_task_list()
    for task in task_list:
        task_listbox.insert('end', task)

# Function to delete a selected task from the list
def remove_task():
    try:
        selected_task = task_listbox.get(task_listbox.curselection())
        if selected_task in task_list:
            task_list.remove(selected_task)
            refresh_task_list()
            db_cursor.execute('DELETE FROM tasks WHERE title = ?', (selected_task,))
    except:
        messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')

# Function to delete all tasks from the list
def remove_all_tasks():
    confirmation = messagebox.askyesno('Delete All', 'Are you sure?')
    if confirmation:
        while task_list:
            task_list.pop()
        db_cursor.execute('DELETE FROM tasks')
        refresh_task_list()

# Function to clear the listbox
def clear_task_list():
    task_listbox.delete(0, 'end')

# Function to close the application
def exit_app():
    print(task_list)
    app_window.destroy()

# Function to retrieve tasks from the database
def load_tasks_from_db():
    while task_list:
        task_list.pop()
    for row in db_cursor.execute('SELECT title FROM tasks'):
        task_list.append(row[0])

# Main function
if __name__ == "__main__":
    app_window = tk.Tk()
    app_window.title("Task Manager")
    app_window.geometry("500x450+750+250")
    app_window.resizable(0, 0)
    app_window.configure(bg="#FAEBD7")

    db_connection = sql.connect('tasks.db')
    db_cursor = db_connection.cursor()
    db_cursor.execute('CREATE TABLE IF NOT EXISTS tasks (title TEXT)')

    task_list = []

    header_frame = tk.Frame(app_window, bg="#FAEBD7")
    control_frame = tk.Frame(app_window, bg="#FAEBD7")
    listbox_frame = tk.Frame(app_window, bg="#FAEBD7")

    header_frame.pack(fill="both")
    control_frame.pack(side="left", expand=True, fill="both")
    listbox_frame.pack(side="right", expand=True, fill="both")

    header_label = ttk.Label(
        header_frame,
        text="Task Manager",
        font=("Brush Script MT", "30"),
        background="#FAEBD7",
        foreground="#8B4513"
    )
    header_label.pack(padx=20, pady=20)

    task_label = ttk.Label(
        control_frame,
        text="Enter the Task:",
        font=("Consolas", "11", "bold"),
        background="#FAEBD7",
        foreground="#000000"
    )
    task_label.place(x=30, y=40)

    task_input = ttk.Entry(
        control_frame,
        font=("Consolas", "12"),
        width=18,
        background="#FFF8DC",
        foreground="#A52A2A"
    )
    task_input.place(x=30, y=80)

    add_button = ttk.Button(
        control_frame,
        text="Add Task",
        width=24,
        command=add_new_task
    )
    delete_button = ttk.Button(
        control_frame,
        text="Delete Task",
        width=24,
        command=remove_task
    )
    delete_all_button = ttk.Button(
        control_frame,
        text="Delete All Tasks",
        width=24,
        command=remove_all_tasks
    )
    exit_button = ttk.Button(
        control_frame,
        text="Exit",
        width=24,
        command=exit_app
    )

    add_button.place(x=30, y=120)
    delete_button.place(x=30, y=160)
    delete_all_button.place(x=30, y=200)
    exit_button.place(x=30, y=240)

    task_listbox = tk.Listbox(
        listbox_frame,
        width=26,
        height=13,
        selectmode='SINGLE',
        background="#FFFFFF",
        foreground="#000000",
        selectbackground="#CD853F",
        selectforeground="#FFFFFF"
    )
    task_listbox.place(x=10, y=20)

    load_tasks_from_db()
    refresh_task_list()

    app_window.mainloop()
    db_connection.commit()
    db_cursor.close()
