import tkinter as tk

def update_result():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result_label.config(text=f"Result: {num1 + num2}")
    except ValueError:
        result_label.config(text="Invalid input")


root = tk.Tk()
root.title("Addition Calculator")

entry1 = tk.Entry(root)
entry1.pack(pady=10)

entry2 = tk.Entry(root)
entry2.pack(pady=10)

result_label = tk.Label(root, text="Result: ")
result_label.pack()

# Bind the update_result function to both entry widgets
entry1.bind("<KeyPress>", lambda event: update_result())
entry2.bind("<KeyPress>", lambda event: update_result())

root.mainloop()