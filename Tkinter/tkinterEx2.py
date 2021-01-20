from tkinter import Tk,Button,Text,Entry,END,StringVar,Label

window = Tk()

def kg_to():
    grams=float(e2_value.get())*1000
    t1.insert(END,grams)
    pounds=float(e2_value.get())*2.20462
    t2.insert(END,pounds)
    ounces=float(e2_value.get())*35.274
    t3.insert(END,ounces)
    # Empty the Text boxes if they had text from the previous use and fill them again
    t1.delete("1.0", END)  # Deletes the content of the Text box from start to END
    t1.insert(END,grams)  # Fill in the text box with the value of gram variable
    t2.delete("1.0", END)
    t2.insert(END,pounds)
    t3.delete("1.0", END)
    t3.insert(END,ounces)


e1=Label(window,text="Kilograms")
e1.grid(row=0,column=0)

e2_value=StringVar()
e2=Entry(window,textvariable=e2_value)
e2.grid(row=0,column=1)

b1=Button(window,text="Convert",command=kg_to)
b1.grid(row=0,column=2)

t1=Text(window,height=1,width=20)
t1.grid(row=1,column=0)

t2=Text(window,height=1,width=20)
t2.grid(row=1,column=1)

t3=Text(window,height=1,width=20)
t3.grid(row=1,column=2)

window.mainloop()