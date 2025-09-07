from tkinter import *

root = Tk()
root.geometry('500x500')

label_look = Label(root, text="查询地点：")
label_look.grid(row=0, column=0, columnspan=2)

entry_location = Entry(root, width=20)
entry_location.grid(row=0, column=3, columnspan=2)


def gett():
    print(entry_location.get())
    weather.insert(END,entry_location.get())
    weather['state'] = 'disabled'


search_but = Button(root, text="立即查询", command=gett)
search_but.grid(row=0, column=10)

weather = Text(root, height=80, width=500, bg="white", fg="black")
weather.place(x=0, y=30)


mainloop()