from tkinter import *
import ast

root = Tk()

i=0
def get_no(num):
    global i
    display.insert(i,num)
    i+=1

def get_symbol(operator):
    global i
    length = len(operator)
    display.insert(i,operator)
    i+=length

def clear_up():
    display.delete(0,END)

def calculate():
    expression = display.get()
    try:
        next = ast.parse(expression,mode="eval")
        result = eval(compile(next,'<string>','eval'))
        clear_up()
        display.insert(0,result)
    except Exception:
        clear_up()
        display.insert(0,"Error")

def back_space():
    str = display.get()
    if len(str):
        str1=str[:-1]
        clear_up()
        display.insert(0,str1)
    else:
        clear_up()
        display.insert(0,"")

root.geometry("300x300")
display = Entry(root)
display.grid(row=1,columnspan=6)

nos=[1,2,3,4,5,6,7,8,9]
count = 1

for x in range(3):
    for y in range(3):
        text_button = nos[count-1]
        button = Button(root,text=count,height=2,width=2,command=lambda text=text_button:get_no(text))
        button.grid(row=x+2,column=y)
        count+=1
button = Button(root,text="0",height=2,width=2,command=lambda :get_no(0))
button.grid(row=5,column=1)

counter=0
operations = ['+','-','*','/','%','**','**2','(',')']
for x in range(3):
    for y in range(3):
        if counter<len(operations):
            button = Button(root,text=operations[counter],height=2,width=2,command=lambda text=operations[counter]:get_symbol(text))
            button.grid(row=x+2,column=y+4)
            counter+=1
all_clear = Button(root,text="AC",height=2,width=2,command=clear_up)
all_clear.grid(row=5,column=5)
equals = Button(root,text="=",height=2,width=2,command=calculate)
equals.grid(row=5,column=4)
backspace = Button(root,text="<-",height=2,width=2,command=back_space)
backspace.grid(row=5,column=6)
root.mainloop()