import tkinter as tk
from tkinter import ttk
import sv_ttk
import serial
import serial.tools.list_ports
import time


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
        self.switch = ttk.Checkbutton(self, text='Step', style='Switch.TCheckbutton', command=self.toggle_switch)
        self.switch.grid(row=4, column=3)
        
        # Feedrate Entry
        self.float_entry = tk.Entry(self, width=10)
        self.float_entry.grid(row=1, column=0)
        self.float_value = tk.DoubleVar()
        # Feedrate Set Button
        self.set_float_button = tk.Button(self, text="Set", command=self.set_float_value)
        self.set_float_button.grid(row=1, column=1)
        # Feedrate display
        self.feedrate_text = tk.StringVar()
        self.feedrate_text.set("0 mm/min")
        self.feedrate_label = tk.Label(self, textvariable=self.feedrate_text)
        self.feedrate_label.grid(row=0, column=0)
        
        # Create move buttons
        self.y_plus_button = tk.Button(self, text="[Y+]", command=self.y_plus)
        self.y_plus_button.grid(row=2, column=2)

        self.x_minus_button = tk.Button(self, text="[X-]", command=self.x_minus)
        self.x_minus_button.grid(row=3, column=1)

        self.h_button = tk.Button(self, text="[H]", command=self.xy_home)
        self.h_button.grid(row=3, column=2, padx=20, pady=15)

        self.x_plus_button = tk.Button(self, text="[X+]", command=self.x_plus)
        self.x_plus_button.grid(row=3, column=3)

        self.y_minus_button = tk.Button(self, text="[Y-]", command=self.y_minus)
        self.y_minus_button.grid(row=4, column=2)
        
        # list available com ports
        self.com_ports = serial.tools.list_ports.comports()
        self.com_port_names = [port.device for port in self.com_ports]
        # Make the COM port dopdown
        self.COMlist = ttk.Combobox(self, width=5, values=self.com_port_names)
        self.COMlist.grid(row=6, column=0)
        # Connected label
        self.com_connected = False
        self.com_label = tk.Label(self, text='Disconnected', fg='red')
        self.com_label.grid(row=5, column=0)
        # Connect button
        self.connect_button = tk.Button(self, text="Connect", command=self.connect_to_com_port)
        self.connect_button.grid(row=6, column=1)
        
        # Debug output
        self.debug_output_text = tk.Text(self, width=80, height=10)
        self.debug_output_text.grid(row=8, column=0, columnspan=3)
        # Create a scrollbar for the debug output text box
        self.debug_output_scrollbar = tk.Scrollbar(self)
        self.debug_output_scrollbar.grid(row=8, column=3, sticky="ns")
        self.debug_output_text.config(yscrollcommand=self.debug_output_scrollbar.set)
        self.debug_output_scrollbar.config(command=self.debug_output_text.yview)

    def toggle_switch(self, event=None):
        self.switch_state = not self.switch_state
        if self.switch_state:
            print('Continuous Feed Is On')
            self.contFeed = True
            self.switch.config(text='Cont')
        else:
            print('Continuous Feed Is Off')
            self.contFeed = False
            self.switch.config(text='Step')
            
    def set_float_value(self):
        try:
            self.float_value.set(float(self.float_entry.get()))
            self.feed = self.float_value.get()
            self.feedrate_text.set(str(self.feed) + str(' mm/min'))
        except ValueError:
            print("Invalid input. Please enter a number.")
            
    def connect_to_com_port(self):
        selected_port = self.COMlist.get()
        if selected_port:
            try:
                self.serial_connection = serial.Serial(selected_port, 115200, timeout=1)
                self.com_label.config(text="Connected", fg="green")
                time.sleep(0.5)
                self.receive_response()
            except serial.SerialException as e:
                self.com_label.config(text="Error: " + str(e), fg="red")
        else:
            self.con_label.config(text="Please select a COM port", fg="red")
            
    def send_command(self, command):
        # Send the command to the controller
        self.serial_connection.write(command.encode())

        # Display the command in the debug output text box
        self.debug_output_text.insert(tk.END, f">> {command}\n")
        self.debug_output_text.see(tk.END)

    def receive_response(self):
        # Receive all available responses from the controller
        if self.serial_connection.in_waiting:
            response = self.serial_connection.readline().decode()
            self.debug_output_text.insert(tk.END, f"<< {response}\n")
            self.debug_output_text.see(tk.END)
        # Call this method again after 10ms to check for new data
        self.after(30, self.receive_response)
        
    def x_plus(self):
        print('x+ working')
        self.command = '$j=G0G91X10.'
        self.send_command(self.command)
        self.receive_response()
    def x_minus(self):
        print('x- working')
        self.command = '$j=G0G91X-10.'
        self.send_command(self.command)
        self.receive_response()
    def y_plus(self):
        print('y+ working')
        self.command = '$j=G0G91Y10.'
        self.send_command(self.command)
        self.receive_response()
    def y_minus(self):
        print('y- working')
        self.command = '$j=G0G91Y-10.'
        self.send_command(self.command)
        self.receive_response()
    def xy_home(self):
        print('home working')
        self.command = '$H'
        
root = tk.Tk()
app = Application(master=root)
app.mainloop()
