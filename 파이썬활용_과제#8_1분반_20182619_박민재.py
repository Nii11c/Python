from tkinter import *

window = Tk()
window.title("Calculator")

lbls = [ ['','','','',''],
          ['7','8','9','/','C'],
          ['4','5','6','*','('],
          ['1','2','3','-',')'],
          ['0','.','=','+',' '] ]

def calc():
    a =10

en = Entry(window, width=30, bg="yellow")
en.grid(row=0, column=0, columnspan=5)

for r in range(1,5):
    for c in range(5):
        btl = Button(window, text=lbls[r][c], width = 5)
        btl.grid(row=r, column=c)

window.mainloop()
