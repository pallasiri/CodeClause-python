#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk

def on_button_click(value):
    current_text = entry_var.get()
    entry_var.set(current_text + str(value))

def clear_entry():
    entry_var.set("")

def calculate_result():
    try:
        result = eval(entry_var.get())
        entry_var.set(result)
    except Exception as e:
        entry_var.set("Error")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget for display
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, justify="right", font=('Arial', 14))
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8)

# Button click event handler
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for (text, row, col) in buttons:
    if text == 'C':
        btn = tk.Button(root, text=text, command=clear_entry, padx=20, pady=20, font=('Arial', 12))
    elif text == '=':
        btn = tk.Button(root, text=text, command=calculate_result, padx=20, pady=20, font=('Arial', 12))
    else:
        btn = tk.Button(root, text=text, command=lambda t=text: on_button_click(t), padx=20, pady=20, font=('Arial', 12))

    btn.grid(row=row, column=col)

# Run the Tkinter main loop
root.mainloop()


# In[ ]:




