import tkinter as tk


def run_cell(cell_clicked):
    newWindow = tk.Toplevel(map_window)
    newWindow.title(str(cell_clicked))
    newWindow.geometry("200x200")
    tk.Label(newWindow,
          text =str(cell_clicked)).pack()


map_window = tk.Tk()

grid_side_len = 16
cell_kwargs = {"master": map_window,
               "relief": tk.RAISED,
               "borderwidth": 1}

for r in range(grid_side_len):
    map_window.rowconfigure(r, minsize=50)
    for c in range(grid_side_len):
        cell_location = (r, c)
        map_window.columnconfigure(c, minsize=75)
        cell = tk.Frame(**cell_kwargs)
        cell.grid(row=r, column=c, sticky="nsew")
        cell_button = tk.Button(master=cell, text=str(cell_location),
                                command=lambda m=cell_location:
                                run_cell(m))
        cell_button.pack(fill="both", expand=True)

map_window.mainloop()
