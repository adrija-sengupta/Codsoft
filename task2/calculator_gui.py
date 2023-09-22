import tkinter as tk
from tkinter import ttk
import calculator_logic

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        # Set the window size to 300x450 (width x height)
        self.root.geometry("300x450")

        self.result_var = tk.StringVar()
        self.result_var.set("")
        self.history = []

        self.create_ui()

    def create_ui(self):
        # Entry field to display input and results
        entry = ttk.Entry(self.root, textvariable=self.result_var, font=("Helvetica", 20), justify="right")
        entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        # Calculator buttons
        buttons = [
            '%', 'CE', 'C', '<-',
            '!', '^', '√', '/',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            'History', '0', '.', '='
        ]

        row = 1
        col = 0
        for button_text in buttons:
            button = ttk.Button(self.root, text=button_text, command=lambda b=button_text: self.button_click(b))
            button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
            col += 1
            if col > 3:
                col = 0
                row += 1

        # Configure grid layout to expand buttons on window resize
        for r in range(1, 6):
            self.root.grid_rowconfigure(r, weight=1)
        for c in range(4):
            self.root.grid_columnconfigure(c, weight=1)

        # Apply the style to the equal button
        equal_button = ttk.Button(self.root, text="+", style="Green.TButton", command=lambda: self.button_click("+"))
        equal_button.grid(row=5, column=3, padx=5, pady=5, sticky="nsew")

    def button_click(self, button_text):
        current_text = self.result_var.get()

        if button_text == "=":
            try:
                result = eval(current_text)
                self.history.append(f"{current_text} = {result}")
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        elif button_text == "C":
            self.result_var.set("")
        elif button_text == "CE":
            self.result_var.set("")
            self.history = []
        elif button_text == "<-":
            self.result_var.set(current_text[:-1])
        elif button_text == "!":
            try:
                num = float(current_text)
                result = calculator_logic.factorial(num)
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        elif button_text == "^":
            try:
                num1, num2 = current_text.split('^')
                result = calculator_logic.power(float(num1), float(num2))
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        elif button_text == "√":
            try:
                num = float(current_text)
                result = calculator_logic.square_root(num)
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        elif button_text == "History":
            self.show_history()
        else:
            self.result_var.set(current_text + button_text)

    def show_history(self):
        history_text = "\n".join(self.history)
        self.result_var.set(history_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
