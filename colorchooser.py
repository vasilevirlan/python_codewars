
import tkinter as tk
from tkinter.colorchooser import askcolor

def callback():
    result = askcolor(color="#6A9662",
                      title = "Color Chooser")
    print(result)

root = tk.Tk()
tk.Button(root,
          text='Choose Color',
          fg="darkgreen",
          command=callback).pack(side=tk.LEFT, padx=10)
tk.Button(text="Quit",
          fg="red").pack(side=tk.LEFT, padx=10)
tk.mainloop()
