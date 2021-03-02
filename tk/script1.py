from tkinter import *

window = Tk()

def km_to_miles():
    t1.insert(END,e1_value.get())

#button 1
b1 = Button(window,text="Execute",command=km_to_miles)
b1.grid(row=0,column=0)

e1_value=StringVar()

#entry 1 enter stuff here
e1 = Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)

#text 1 text area
t1 = Text(window,height=1,width=20)
t1.grid(row=0,column=2)

#should always be at the end
window.mainloop()
