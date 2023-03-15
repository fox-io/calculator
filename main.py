import tkinter as tk

# Create and config the window
root = tk.Tk()
root.title("Calculator")
root.geometry("200x300")
root.resizable(False, False)  # Do not allow resize

# Calculation Variables
left_value = "0"
right_value = "0"
current_function = ""
current_result = "0"

# Add the display
display_font = ("Consolas", 20)
display = tk.Label(root, text="0123456789", font=display_font, anchor="e")
display.grid(row=0, column=0, columnspan=4, sticky="nesw")


# Process keypress
def keypress(key):

    global current_result, right_value, left_value, current_function
    if key == "C":
        clear()
    elif key == "/" or key == "-" or key == "+" or key == "*":
        current_function = key
        left_value = right_value
        right_value = "0"
    elif key == "=":
        if current_function == "/":
            current_result = str(int(left_value) / int(right_value))
        elif current_function == "*":
            current_result = str(int(left_value) * int(right_value))
        elif current_function == "-":
            current_result = str(int(left_value) - int(right_value))
        elif current_function == "+":
            current_result = str(int(left_value) + int(right_value))
        right_value = current_result
    else:
        if right_value == "0":
            right_value = key
        else:
            right_value = str(right_value) + key

    update_display()

    # Return break to prevent duplicated input
    return "break"


# Add buttons
buttons = []  # Stores the tkinter buttons
function_text = ["C", "/", "*", "-", "+", "=", "."]  # Allows for looping to add the buttons

# Add function buttons to UI
for i in range(7):
    button = tk.Button(root, text=function_text[i], command=lambda x=function_text[i]: keypress(x))
    button.grid(row=i < 4 and 1 or i == 4 and 2 or i - 1,
                column=i == 6 and 2 or 6 > i > 3 and 3 or i,
                rowspan=3 < i < 6 and 2 or 1,
                sticky="nesw")
    buttons.append(button)
    # Symbol layout map
    #   c/*-+=. sym
    #   1111245 rows
    #   0123332 cols
    #   0123456 i

# Add number buttons to UI
for i in range(10):
    button = tk.Button(root, text=f"{i}", command=lambda x=str(i): keypress(x))
    if i == 0:
        button.grid(row=5, column=0, columnspan=2, sticky="nesw")
    if 1 <= i <= 3:
        button.grid(row=4, column=i - 1, sticky="nesw")
    if 4 <= i <= 6:
        button.grid(row=3, column=i - 4, sticky="nesw")
    if 7 <= i <= 9:
        button.grid(row=2, column=i - 7, sticky="nesw")
    buttons.append(button)

# Fill window with buttons
root.columnconfigure("all", weight=1)
root.rowconfigure("all", weight=1)


def update_display():
    # Update the display to the current value
    global right_value, display
    display["text"] = str(right_value)


def clear():
    # Clear all values and call the display update
    global left_value, right_value, current_result
    left_value = str(0)
    right_value = str(0)
    current_result = str(0)
    update_display()


# Bind keys
for i in range(10):
    root.bind(str(i), lambda x: keypress(x.keysym))

root.bind('<slash>', lambda x: keypress("/"))
root.bind('<asterisk>', lambda x: keypress("*"))
root.bind('<minus>', lambda x: keypress("-"))
root.bind('<plus>', lambda x: keypress("+"))
root.bind('<period>', lambda x: keypress("."))
root.bind('<Return>', lambda x: keypress("="))
root.bind('<Escape>', lambda x: keypress("C"))

# Ensure focus for keybinds
root.focus_set()

# Run
root.mainloop()
