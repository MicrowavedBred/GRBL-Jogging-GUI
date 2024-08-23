import tkinter as tk
from tkinter import ttk
import sv_ttk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.switch_state = False

    def create_widgets(self):
        sv_ttk.set_theme("dark")
        
        # Continuous Feed Switch
        self.contFeed = False
        self.switch = ttk.Checkbutton(self, text='Off', style='Switch.TCheckbutton', command=self.toggle_switch)
        self.switch.grid(row=3, column=3)
        
        # Feedrate Entry
        self.float_entry = tk.Entry(self, width=10)
        self.float_entry.grid(row=1, column=0)
        self.float_value = tk.DoubleVar()
        # Feedrate Set Button
        self.set_float_button = tk.Button(self, text="Set", command=self.set_float_value)
        self.set_float_button.grid(row=1, column=1)
        # Feedrate display
        # Create a StringVar to hold the feedrate text
        self.feedrate_text = tk.StringVar()
        self.feedrate_text.set("0 mm/min")  # Initialize with a default value
        # Feedrate display
        self.feedrate_label = tk.Label(self, textvariable=self.feedrate_text)
        self.feedrate_label.grid(row=0, column=0)
        
        # Create buttons
        self.y_plus_button = tk.Button(self, text="[Y+]", command=self.y_plus)
        self.y_plus_button.grid(row=1, column=2)

        self.x_minus_button = tk.Button(self, text="[X-]", command=self.x_minus)
        self.x_minus_button.grid(row=2, column=1)

        self.h_button = tk.Button(self, text="[H]", command=self.xy_home)
        self.h_button.grid(row=2, column=2, padx=20, pady=15)

        self.x_plus_button = tk.Button(self, text="[X+]", command=self.x_plus)
        self.x_plus_button.grid(row=2, column=3)

        self.y_minus_button = tk.Button(self, text="[Y-]", command=self.y_minus)
        self.y_minus_button.grid(row=3, column=2)
        
        # Make the COM port dopdown
        self.COMlist = ttk.Combobox(self, width=5)
        self.COMlist.grid(row=3, column=0)
        
        self.com_connected = False
        self.com_label = tk.Label(self, text='Disconnected', fg='red')
        self.com_label.grid(row=4, column=0)

    def toggle_switch(self, event=None):
        self.switch_state = not self.switch_state
        if self.switch_state:
            #self.switch_label.config(image=self.on_image)
            print('Continuous Feed Is On')
            self.contFeed = True
            print(self.contFeed)
            self.switch.config(text='On')
        else:
            #self.switch_label.config(image=self.off_image)
            print('Continuous Feed Is Off')
            self.contFeed = False
            print(self.contFeed)
            self.switch.config(text='Off')
            
    def set_float_value(self):
        try:
            self.float_value.set(float(self.float_entry.get()))
            self.feed = self.float_value.get()
            self.feedrate_text.set(str(self.feed) + str(' mm/min'))  # Update the StringVar
        except ValueError:
            print("Invalid input. Please enter a number.")
        
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
