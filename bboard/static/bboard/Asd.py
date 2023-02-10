import tkinter as tk

def calculate():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    if operation.get() == "add":
        result = num1 + num2
    elif operation.get() == "subtract":
        result = num1 - num2
    elif operation.get() == "multiply":
        result = num1 * num2
    else:
        result = num1 / num2
    label_result.config(text="Result: " + str(result))

app = tk.Tk()
app.title("Python Calculator")

frame = tk.Frame(app)
frame.pack()

entry_num1 = tk.Entry(frame)
entry_num1.pack()

entry_num2 = tk.Entry(frame)
entry_num2.pack()

operations = ["add", "subtract", "multiply", "divide"]
operation = tk.StringVar()
operation.set("add")

dropdown = tk.OptionMenu(frame, operation, *operations)
dropdown.pack()

button = tk.Button(frame, text="Calculate", command=calculate)
button.pack()

label_result = tk.Label(app, text="")
label_result.pack()

app.mainloop()