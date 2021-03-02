from tkinter import *

window = Tk()

def weight_convert():
    grams = float(kg_value.get())*1000
    lbs = float(kg_value.get())*2.20462
    ozs = float(kg_value.get())*35.274
    t1.insert(END,grams)
    t2.insert(END, lbs)
    t3.insert(END, ozs)

kg_value=StringVar()

#button
b1 = Button(window, text="convert", command=weight_convert)
b1.grid(row=0,column=2)

#lable
l1 = Label(window, text ="kg")
l1.grid(row=0,column=0)
#execute
e1 = Entry(window,textvariable=kg_value)
e1.grid(row=0,column=1)

#text
t1 = Text(window,height=1,width=20)
t1.grid(row=1,column=0)
t2 = Text(window,height=1,width=20)
t2.grid(row=1,column=1)
t3 = Text(window,height=1,width=20)
t3.grid(row=1,column=2)














window.mainloop()