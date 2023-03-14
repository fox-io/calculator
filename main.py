import tkinter as tk

# Create and config the window
root = tk.Tk()
root.title("Calculator")
root.geometry("200x300")
root.resizable(False, False)  # Do not allow resize

# Calculation Variables
left_value = 0
right_value = 0
current_result = 0

# Add the display
display_font = ("Consolas", 20)
display = tk.Label(root, text="0123456789", font=display_font, anchor="e")
display.grid(row=0, column=0, columnspan=4, sticky="nesw")


# Define keypress event handler
def keypress(key):
    global current_result, right_value, left_value
    if key == "C":
        clear()
    elif key == "/":
        current_result = str(int(left_value) / int(right_value))
    elif key == "*":
        current_result = str(int(left_value) * int(right_value))
    elif key == "-":
        current_result = str(int(left_value) - int(right_value))
    elif key == "+":
        current_result = str(int(left_value) + int(right_value))
    elif key == "=":
        right_value = current_result
    elif key == "0":
        right_value = str(right_value) + "0"
    elif key == "1":
        right_value = str(right_value) + "1"
    elif key == "2":
        right_value = str(right_value) + "2"
    elif key == "3":
        right_value = str(right_value) + "3"
    elif key == "4":
        right_value = str(right_value) + "4"
    elif key == "5":
        right_value = str(right_value) + "5"
    elif key == "6":
        right_value = str(right_value) + "6"
    elif key == "7":
        right_value = str(right_value) + "7"
    elif key == "8":
        right_value = str(right_value) + "8"
    elif key == "9":
        right_value = str(right_value) + "9"

    update_display()

    # Return break to prevent duplicated input
    return "break"


# Add buttons
buttons = []
function_text = ["C", "/", "*", "-", "+", "=", "."]

# Add function buttons
for i in range(7):
    button = tk.Button(root, text=function_text[i], command=lambda: keypress(function_text[i]))
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

# Add number buttons
for i in range(10):
    button = tk.Button(root, text=f"{i}", command=lambda: keypress(str(i)))
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
    global right_value, display
    display["text"] = str(right_value)


def clear():
    global left_value, right_value, current_result
    left_value = str(0)
    right_value = str(0)
    current_result = str(0)
    update_display()


# Bind keys
for i in range(10):
    root.bind(str(i), lambda x: keypress(str(i)))

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
