import tkinter as tk
import tkinter.ttk as ttk
# window definition
window = tk.Tk()
window.minsize(400, 400)
# item and graphics declaration
greeting = ttk.Button(text="ELLOOOO")


# packing
greeting.pack()


# mainloop !IMPORTANT! DO NOT ADD CODE BENEATH THIS IF YOU WANT IT TO BE INCLUDED AND DRAWN
window.mainloop()