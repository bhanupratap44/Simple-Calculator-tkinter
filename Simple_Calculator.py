from tkinter import *

# Create window
root = Tk()
root.title("Simple Calculator")
root.geometry("375x600")
root.resizable(False, False)                  #Allows resizing

# Entry widget
entry = Entry(root, font=("Arial", 20), borderwidth=3, relief=RIDGE, justify='right')
entry.pack(fill=BOTH, ipadx=8, ipady=10, padx=10, pady=10)

# Functions
def button_click(value):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(END, current + value)

def clear_entry():
    entry.delete(0, END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(END, str(result))
    except:
        entry.delete(0, END)
        entry.insert(END, "Error")

# Button layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

# Create buttons
for row in buttons:
    frame = Frame(root)
    frame.pack(expand=True, fill=BOTH)
    for btn_text in row:
        if btn_text == "=":
            Button(frame, text=btn_text, font=("Arial", 18), bg="lightblue",
                   command=calculate).pack(side=LEFT, expand=True, fill=BOTH)
        else:
            Button(frame, text=btn_text, font=("Arial", 18),
                   command=lambda val=btn_text: button_click(val)).pack(side=LEFT, expand=True, fill=BOTH)

# Clear button
Button(root, text="Clear", font=("Arial", 18), bg="red", fg="white",
       command=clear_entry).pack(fill=BOTH, padx=10, pady=5)

# Run loop
root.mainloop()