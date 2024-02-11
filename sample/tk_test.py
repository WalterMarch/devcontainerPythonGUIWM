import tkinter as tk

root_window = tk.Tk()

root_window.title("Hello, World")
root_window.geometry("300x100")
root_window.configure(background="#353535")

tk.Label(root_window, text="Hello, World", fg="White", bg="#353535").pack()

tk.Button(root_window, text="Exit", width=10, command=root_window.destroy).pack()

root_window.mainloop()
