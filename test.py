import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.switch_state = False

    def create_widgets(self):
        # Create buttons
        self.y_plus_button = tk.Button(self, text="[Y+]", command=self.y_plus)
        self.y_plus_button.grid(row=0, column=1)

        self.x_minus_button = tk.Button(self, text="[X-]", command=self.x_minus)
        self.x_minus_button.grid(row=1, column=0)

        self.h_button = tk.Button(self, text="[H]", command=self.xy_home)
        self.h_button.grid(row=1, column=1)

        self.x_plus_button = tk.Button(self, text="[X+]", command=self.x_plus)
        self.x_plus_button.grid(row=1, column=2)

        self.y_minus_button = tk.Button(self, text="[Y-]", command=self.y_minus)
        self.y_minus_button.grid(row=2, column=1)

        # Create switch button
        self.on_image = tk.PhotoImage(file="on.png")
        self.off_image = tk.PhotoImage(file="off.png")
        self.switch_button = tk.Button(self, image=self.off_image, command=self.toggle_switch)
        self.switch_button.grid(row=2, column=2)

    def toggle_switch(self):
        self.switch_state = not self.switch_state
        if self.switch_state:
            self.switch_button.config(image=self.on_image)
            print('Continuous feed on')
        else:
            self.switch_button.config(image=self.off_image)
            print('Continuous feed off')
    def x_plus(self):
        print('x+ working')
    def x_minus(self):
        print('x- working')
    def y_plus(self):
        print('y+ working')
    def y_minus(self):
        print('y- working')
    def xy_home(self):
        print('home working')

root = tk.Tk()
app = Application(master=root)
app.mainloop()
