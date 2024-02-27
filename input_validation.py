import tkinter as tk

def validate_input(P):
    if P == "":
        return True
    try:
        float(P)
        return True
    except ValueError:
        return False

root = tk.Tk()

# Create an Entry widget with validation
validate_func = root.register(validate_input)
entry = tk.Entry(root, validate="key", validatecommand=(validate_func, '%P'))
entry.pack(padx=10, pady=10)

root.mainloop()
