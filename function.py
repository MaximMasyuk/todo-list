import tkinter as tk
from CTkMessagebox import CTkMessagebox
from db_connection import cursor, conn


def on_entry_click(event, entry):
    if entry.get() == "Write a task":
        entry.delete(0, tk.END)


def on_entry_leave(event, entry):
    if entry.get() == "":
        entry.insert(0, "Write a task")


def add_task(entry_name, listbox):
    name_task = entry_name.get()

    if not name_task:
        CTkMessagebox(title="Error", message="Add name", icon="cancel")
    else:
        cursor.execute("INSERT INTO tasks (title)  VALUES (%s)", (name_task,))

        conn.commit()

        listbox.insert(tk.END, name_task)
        entry_name.delete(0, tk.END)


def remove_task(list):
    selected_task = list.curselection()
    if selected_task is None:
        CTkMessagebox(title="Error", message="Select the task to delete", icon="cancel")
    else:
        list.delete(selected_task)
        cursor.execute("DELETE FROM tasks WHERE title = %s", (list.get(list.curselection()),))

        conn.commit()


def update_task(listbox, entry):
    selected_task = listbox.get(listbox.curselection())
    updated_task = entry.get()
    if selected_task and updated_task:
        listbox.delete(listbox.curselection())
        listbox.insert(tk.END, updated_task)
        entry.delete(0, tk.END)
        cursor.execute("UPDATE  tasks SET title = %s WHERE title = %s", (updated_task, selected_task))

        conn.commit()
    else:
        CTkMessagebox(title="Error", message="Enter an updated title or select a task to update", icon="cancel")


def display_tasks(listbox):
    cursor.execute("SELECT title FROM tasks")
    rows = cursor.fetchall()
    for row in rows:
        listbox.insert(tk.END, row)


