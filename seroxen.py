import tkinter as tk
from tkinter import font
import keyboard

  # this code is not powerful because
  # i dont wanna release tools that can be used for making dangerous code
  # because skidders are everywhere
  # and i dont want to be responsible for my src becoming the next major
  # millions of dollars in damage infastructure attacking tool

def gooner(e):
    return "break"

def goon():
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(bg='black')

    edging_gooning = font.Font(family='Arial', size=62, weight='bold')
    licking_pussy = tk.Label(
        root,
        text="SKIBIDI SIGMA OHIO RIZZ GYATT GOONING",
        font=edging_gooning,
        fg='black',
        bg='white'
    )
    licking_pussy.place(relx=0.5, rely=0.5, anchor='center')

    # key blockers wont work btw because you have to be root to block keys
    # and im lazy to learn how to do that

    root.bind('all', gooner)
    root.bind('<Key>', gooner)
    root.bind('<Alt-F4>', gooner)
    root.bind('<Control-c>', gooner)
    root.bind('<Control-v>', gooner)
    root.bind('<Control-x>', gooner)
    root.bind('<Control-Shift-Escape>', gooner)
    root.bind('<Control-Shift-Tab>', gooner)
    root.bind('<Control-Alt-Delete>', gooner)
    root.bind('<Escape>', gooner) 
    root.bind('<Tab>', gooner) 
    root.bind('<Return>', gooner) 

    def SRX(event):
        if event.state == 12 and event.keysym == '6':
            root.quit()
    
    root.bind('<Key-6>', SRX)
    
    root.mainloop()

if __name__ == "__main__":
    goon()