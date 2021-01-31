try:
    import Tkinter as tk
except:
    import tkinter as tk

root = tk.Tk()
root.geometry("100x50")

button = tk.Button(text = "Click and Quit", command = root.quit)
button.pack()

root.mainloop()