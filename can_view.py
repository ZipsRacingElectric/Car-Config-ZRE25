# CAN view called from gui.py
# Used to view the ca
import customtkinter
from typing import Union
from typing import Callable


class NewCANWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("800x600")

        self.label = customtkinter.CTkLabel(self, text="ToplevelWindow")
        self.label.pack(padx=20, pady=20)





