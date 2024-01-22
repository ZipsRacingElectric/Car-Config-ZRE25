# CAN view called from gui.py
# Used to view the ca
import customtkinter
from typing import Union
from typing import Callable

import gui

class NewCANWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("800x600")

        self.button = customtkinter.CTkButton(self, text="CANBus view", command=self.button_callback)
        self.button.grid(row=1, column=0, padx=20, pady=10)


    def button_callback(self):
        print("button pressed")





