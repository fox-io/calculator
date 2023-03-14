import tkinter as tk

# Create and config the window
root = tk.Tk()
root.title("Calculator")
root.geometry("200x300")
root.resizable(False, False) # Do not allow resize

# Add the display
display_font = ("Consolas", 20)
display = tk.Label(root, text="0123456789", font=display_font, anchor="e")
display.grid(row=0, column=0, columnspan=4, sticky="nesw")

# Add function buttons
button_clear = tk.Button(root, text="C")
button_clear.grid(row=1, column=0, sticky="nesw")
button_divide = tk.Button(root, text="/")
button_divide.grid(row=1, column=1, sticky="nesw")
button_multiply = tk.Button(root, text="*")
button_multiply.grid(row=1, column=2, sticky="nesw")
button_subtract = tk.Button(root, text="-")
button_subtract.grid(row=1, column=3, sticky="nesw")
button_add = tk.Button(root, text="+")
button_add.grid(row=2, column=3, rowspan=2, sticky="nesw")
button_equals = tk.Button(root, text="=")
button_equals.grid(row=4, column=3, rowspan=2, sticky="nesw")
button_decimal = tk.Button(root, text=".")
button_decimal.grid(row=5, column=2, sticky="nesw")

# Add number buttons
button_0 = tk.Button(root, text="0")
button_0.grid(row=5, column=0, columnspan=2, sticky="nesw")
button_1 = tk.Button(root, text="1")
button_1.grid(row=4, column=0, sticky="nesw")
button_2 = tk.Button(root, text="2")
button_2.grid(row=4, column=1, sticky="nesw")
button_3 = tk.Button(root, text="3")
button_3.grid(row=4, column=2, sticky="nesw")
button_4 = tk.Button(root, text="4")
button_4.grid(row=3, column=0, sticky="nesw")
button_5 = tk.Button(root, text="5")
button_5.grid(row=3, column=1, sticky="nesw")
button_6 = tk.Button(root, text="6")
button_6.grid(row=3, column=2, sticky="nesw")
button_7 = tk.Button(root, text="7")
button_7.grid(row=2, column=0, sticky="nesw")
button_8 = tk.Button(root, text="8")
button_8.grid(row=2, column=1, sticky="nesw")
button_9 = tk.Button(root, text="9")
button_9.grid(row=2, column=2, sticky="nesw")

# Fill window with buttons
root.columnconfigure("all", weight=1)
root.rowconfigure("all", weight=1)


# Define keypress event handler
def keypress(event):
    # Debug for key presses
    # print(event.keysym)

    # TODO: Perform calculator functions

    # Return break to prevent duplicated input
    return "break"


# Bind keys
for i in range(10):
    root.bind(str(i), keypress)
root.bind('<slash>', keypress)
root.bind('<asterisk>', keypress)
root.bind('<minus>', keypress)
root.bind('<plus>', keypress)
root.bind('<period>', keypress)
root.bind('<Return>', keypress)
root.bind('<Escape>', keypress)
# Ensure focus for keybinds
root.focus_set()

# Run
root.mainloop()
