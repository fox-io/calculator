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

# Add buttons
buttons = []
function_text = ["C", "/", "*", "-", "+", "=", "."]

# Add function buttons
for i in range(7):
    button = tk.Button(root, text=function_text[i])
    button.grid(row=i < 4 and 1 or i == 4 and 2 or i - 1,
                column=i == 6 and 2 or 6 > i > 3 and 3 or i,
                rowspan=3 < i < 6 and 2 or 1,
                sticky="nesw")
    buttons.append(button)
    # c/*-+=. sym
    # 1111245 rows
    # 0123332 cols
    # 0123456 i

# Add number buttons
for i in range(10):
    button = tk.Button(root, text=f"{i}")
    if i == 0:
        button.grid(row=5, column=0, columnspan=2, sticky="nesw")
    if 1 <= i <= 3:
        button.grid(row=4, column=i-1, sticky="nesw")
    if 4 <= i <= 6:
        button.grid(row=3, column=i-4, sticky="nesw")
    if 7 <= i <= 9:
        button.grid(row=2, column=i-7, sticky="nesw")
    buttons.append(button)

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
