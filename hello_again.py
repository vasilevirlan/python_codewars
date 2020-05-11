
from tkinter import *

'''This little application will say hallo on pushing the
    button and will quit the indow if you push "quit"
'''
class App:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.button = Button(
            frame, text="QUIT", fg='red', command=frame.quit)

        self.button.pack(side=RIGHT)

        self.hi_there = Button(frame, text="Hello salut!!", command=self.say_hi)
        self.hi_there.pack(side=RIGHT)
    def say_hi(self):
        print("Salutare din tkinter!!")

root = Tk()

app = App(root)
root.mainloop()
root.destroy()
