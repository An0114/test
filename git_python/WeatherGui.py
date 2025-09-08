from tkinter import *

class WeatherGui:
    def __init__(self, root):
        self.root = root
        self.root.geometry('500x500')
        self.root.title('天气')
        self.root.iconbitmap('weather_ico.ico')

        self.label = Label(root, text='查询地点：', font=('Arial', 14))
        self.label.place(x=5, y=15)

        self.entry_var = StringVar()
        self.entry = Entry(root, textvariable=self.entry_var, font=('Arial', 14), width=20)
        # self.entry.insert(0,'beijing')
        self.entry.place(x=100, y=15)

        self.btn = Button(root, text="立即查询", font=('Arial', 11), height=1)
        self.btn.place(x=350, y=15)

        self.text = Text(root, font=('Arial', 14), width=500, height=400, state='disabled')
        self.text.place(x=0, y=50)

    def print_weather(self, weather_data):
        if self.entry.get() :
            self.text.config(state=NORMAL)
            self.text.insert(END, weather_data)
            self.entry.delete(0, END)
        self.text.config(state=DISABLED)

    def run(self):
        self.root.mainloop()

    def get_entry(self):
        return self.entry_var.get()

if __name__ == '__main__':
    root = Tk()
    app = WeatherGui(root)
    app.run()
