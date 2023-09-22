from tkinter import *
from PassGen import generate_password

# Function to generate the password
def generate_password_callback():
    password_length = int(password_length_entry.get())
    generated_password = generate_password(password_length)
    generated_password_textbox.delete(1.0, END)
    generated_password_textbox.insert(1.0, generated_password)

# Function to accept the password
def accept_password_callback():
    username = username_entry.get()
    password = generated_password_textbox.get(1.0, END)
    
    # Append the accepted password and username to the list
    accepted_passwords_listbox.insert(END, f"Username: {username}\nPassword: {password}")
    
    # Clear the username and generated password fields
    username_entry.delete(0, END)
    generated_password_textbox.delete(1.0, END)

# Function to reset the password
def reset_password_callback():
    username_entry.delete(0, END)
    password_length_entry.delete(0, END)
    generated_password_textbox.delete(1.0, END)

# Create the main window
root = Tk()
root.title("Password Generator")

# Set the window size to 800x450 pixels
root.geometry("800x450")

# Create a frame for input elements
input_frame = Frame(root)
input_frame.pack(fill=BOTH, expand=True, padx=20, pady=20)

# Create a frame for accepted passwords
accepted_passwords_frame = Frame(root)
accepted_passwords_frame.pack(fill=BOTH, expand=True, padx=20, pady=10)

# Create the labels
username_label = Label(input_frame, text="Enter username:")
password_length_label = Label(input_frame, text="Enter password length:")
generated_password_label = Label(input_frame, text="Generated password:")

# Create the entry boxes
username_entry = Entry(input_frame)
password_length_entry = Entry(input_frame)

# Create the buttons and color them
button_bg_color = "#4CAF50"  # Green color
button_fg_color = "white"     # White text color
generate_password_button = Button(input_frame, text="Generate Password", command=generate_password_callback,
                                  bg=button_bg_color, fg=button_fg_color)
accept_button = Button(input_frame, text="Accept", command=accept_password_callback,
                       bg=button_bg_color, fg=button_fg_color)
reset_button = Button(input_frame, text="Reset", command=reset_password_callback,
                      bg=button_bg_color, fg=button_fg_color)

# Create the text box
generated_password_textbox = Text(input_frame, width=20, height=1)

# Create a listbox to display accepted passwords
accepted_passwords_listbox = Listbox(accepted_passwords_frame, width=50, height=10)

# Layout the widgets in input frame using grid and weights
username_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
username_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)
password_length_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)
password_length_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)
generated_password_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)
generated_password_textbox.grid(row=2, column=1, padx=10, pady=5, sticky=W)
generate_password_button.grid(row=3, column=0, padx=10, pady=10, sticky=W)
accept_button.grid(row=3, column=1, padx=10, pady=10, sticky=W)
reset_button.grid(row=3, column=2, padx=10, pady=10, sticky=W)

# Configure column weights to resize elements in input frame
input_frame.grid_columnconfigure(0, weight=1)
input_frame.grid_columnconfigure(1, weight=1)
input_frame.grid_rowconfigure(2, weight=1)

# Layout the listbox in accepted passwords frame using grid and weights
accepted_passwords_listbox.grid(row=0, column=0, padx=10, pady=10, sticky=W+E+N+S)
accepted_passwords_frame.grid_rowconfigure(0, weight=1)
accepted_passwords_frame.grid_columnconfigure(0, weight=1)

# Start the mainloop
root.mainloop()
