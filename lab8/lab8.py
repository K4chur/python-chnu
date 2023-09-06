import tkinter as tk
from tkinter import messagebox

def find_maximum():
    try:
        x = int(entry_x.get())
        y = int(entry_y.get())
        z = int(entry_z.get())
        max_value = max(x, y, z)
        messagebox.showinfo("Maximum Value", f"The maximum value is: {max_value}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid integers for x, y, and z.")

# Create the main window
window = tk.Tk()
window.title("Maximum Value Finder")

window.geometry("300x200")  # Width x Height

# Create and place labels and entry widgets for x, y, and z
label_x = tk.Label(window, text="Enter x:")
label_x.pack()
entry_x = tk.Entry(window)
entry_x.pack()

label_y = tk.Label(window, text="Enter y:")
label_y.pack()
entry_y = tk.Entry(window)
entry_y.pack()

label_z = tk.Label(window, text="Enter z:")
label_z.pack()
entry_z = tk.Entry(window)
entry_z.pack()

# Create and place the "Find Maximum" button
find_button = tk.Button(window, text="Find Maximum", command=find_maximum)
find_button.pack()

# Start the GUI main loop
window.mainloop()
