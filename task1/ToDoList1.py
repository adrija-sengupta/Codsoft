import tkinter as tk

def add_task():
    task = entry_tasks.get()
    if task:
        tasks.append(task)
        entry_tasks.delete(0, tk.END)
        update_listbox()

def edit_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        index = selected_task_index[0]
        task = entry_tasks.get()
        if task:
            tasks[index] = task
            entry_tasks.delete(0, tk.END)
            update_listbox()

def delete_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        index = selected_task_index[0]
        tasks.pop(index)
        update_listbox()

def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

def submit_task():
    task = entry_tasks.get()
    if task:
        tasks.append(task)
        entry_tasks.delete(0, tk.END)
        update_listbox()

root = tk.Tk()
root.title("ToDo List")

# Set the size of the root window
root.geometry("800x400")  # Adjust the dimensions as needed

# Create the label and entry widgets
label_tasks = tk.Label(root, text="Tasks", bg="green", fg="white", font=("Arial", 20))
entry_tasks = tk.Entry(root, font=("Arial", 15))

# Create the listbox widget
listbox = tk.Listbox(root, width=40, height=10, font=("Arial", 15))  # Increase the width
listbox.pack(pady=10)

# Create the button widgets
button_edit = tk.Button(root, text="EDIT", command=edit_task, font=("Arial", 15))
button_delete = tk.Button(root, text="Delete", command=delete_task, font=("Arial", 15))
button_submit = tk.Button(root, text="Submit", command=submit_task, font=("Arial", 15))

# Pack the widgets
label_tasks.pack(fill=tk.X)
entry_tasks.pack(fill=tk.X)
button_edit.pack(side="left", fill=tk.X, expand=True)
button_delete.pack(side="left", fill=tk.X, expand=True)
button_submit.pack(side="left", fill=tk.X, expand=True)

# Create a list to store the tasks
tasks = []

# Bind the enter key to the add task button
entry_tasks.bind("<Return>", lambda event=None: submit_task())

root.mainloop()
