from function import (
    on_entry_click,
    on_entry_leave,
    add_task,
    remove_task,
    update_task,
    display_tasks,
)
import tkinter as tk
import customtkinter
from CTkListbox import *
from db_connection import conn

custom_font_title = ("Arial", 24)
custom_font_other = ("Arial", 16)

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme(
    "blue"
)  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()
app.title("To-do List")
app.geometry("600x500")


frame = customtkinter.CTkFrame(master=app)
frame.pack(padx=10, pady=10)


label = customtkinter.CTkLabel(frame, text="Daily Task", font=custom_font_title)
label.grid(row=0, column=0, padx=10, pady=10, columnspan=2)


label = customtkinter.CTkLabel(frame, text="Name of task", font=custom_font_other)
label.grid(row=1, column=0, padx=10, pady=10)


entry_title = customtkinter.CTkEntry(master=frame, width=150)
entry_title.insert(0, "Write a task")
entry_title.bind("<FocusIn>", lambda event: on_entry_click(event, entry_title))
entry_title.bind("<FocusOut>", lambda event: on_entry_leave(event, entry_title))
entry_title.grid(row=1, column=1, padx=10, pady=10)


listbox_tasks = CTkListbox(frame)
listbox_tasks.grid(row=3, column=0, padx=10, pady=10, columnspan=2)


button_add = customtkinter.CTkButton(
    master=frame,
    text="Add task",
    width=150,
    command=lambda: add_task(entry_title, listbox_tasks),
)
button_add.grid(row=4, column=0, padx=10, pady=10)


button_delete = customtkinter.CTkButton(
    master=frame,
    text="Delete task",
    width=150,
    command=lambda: remove_task(listbox_tasks),
)
button_delete.grid(row=4, column=1, padx=10, pady=10)


button_update = customtkinter.CTkButton(
    master=frame,
    text="Update task",
    width=150,
    command=lambda: update_task(listbox_tasks, entry_title),
)
button_update.grid(row=5, column=0, padx=10, pady=10, columnspan=2)


if __name__ == "__main__":
    display_tasks(listbox_tasks)
    app.mainloop()
    conn.close()
