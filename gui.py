# GUI -------------------------------------------------------------------------------------------------------------------------
# Author: Brian Glen
# Date Created: 12/22/23
# Date Updated: 12/22/23
#   This module contains all code related to the GUI. 

# Libraries -------------------------------------------------------------------------------------------------------------------
import customtkinter

# Objects ---------------------------------------------------------------------------------------------------------------------

class MenuFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.title = customtkinter.CTkLabel(self, text="Menu", fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

        self.button = customtkinter.CTkButton(self, text="CAN View", command=self.button_callback)
        self.button.grid(row=1, column=0, padx=20, pady=10)
        self.button = customtkinter.CTkButton(self, text="BMS View", command=self.button_callback)
        self.button.grid(row=2, column=0, padx=20, pady=10)
        self.button = customtkinter.CTkButton(self, text="Vehicle Configuration", command=self.button_callback)
        self.button.grid(row=3, column=0, padx=20, pady=10)

    # Called when buttons tied to this function are pressed
    def button_callback(self):
        print("button pressed")

class ButtonFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure((0, 1), weight=1)

        self.button = customtkinter.CTkButton(self, text="Connect to Vehicle", command=self.button_callback)
        self.button.grid(row=0, column=0, padx=20, pady=20, sticky="ew")
        self.button = customtkinter.CTkButton(self, text="Load Preset", command=self.button_callback)
        self.button.grid(row=0, column=1, padx=20, pady=20, sticky="ew")

    # Called when buttons tied to this function are pressed
    def button_callback(self):
        print("button pressed")

class CheckboxFrame(customtkinter.CTkFrame):
    def __init__(self, master, title, values):
        super().__init__(master)

        self.grid_columnconfigure(0 , weight=1)
        self.values = values
        self.title = title
        self.checkboxes = []

        self.title = customtkinter.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")


        for i, value in enumerate(self.values):
            checkbox = customtkinter.CTkCheckBox(self, text=value)
            checkbox.grid(row=i+1, column=0, padx=20, pady=(10, 0), sticky="ew")
    
    def get(self):
        checked = []
        for box in self.checkboxes:
            if box.get() == 1:
                checked.append(box.cget("text"))
        return checked
    
class RadiobuttonFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, title, values):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.title = title
        self.radiobuttons = []
        self.variable = customtkinter.StringVar(value="")

        self.title = customtkinter.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

        for i, value in enumerate(self.values):
            radiobutton = customtkinter.CTkRadioButton(self, text=value, value=value, variable=self.variable)
            radiobutton.grid(row=i + 1, column=0, padx=10, pady=(10, 0), sticky="w")
            self.radiobuttons.append(radiobutton)

    def get(self):
        return self.variable.get()

    def set(self, value):
        self.variable.set(value)

class StatusFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.title = "Status"

        self.title = customtkinter.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

        # UpperFrame Config
        self.grid_columnconfigure(0, weight=1) # self centering

        # TODO: Insert real-time updates of connectivity status

class DefaultViewFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # UpperFrame Config
        self.grid_columnconfigure(0, weight=1) # status frame has bias over presets
        self.configure(fg_color="transparent")

        # Frames
        self.status_frame = StatusFrame(self)
        self.status_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nswe")

        self.radiobutton_frame = RadiobuttonFrame(self, title="Vehicle Presets", values=["Stand Test", "Shakedown", "Skidpad FSAE", "Acceleration FSAE", "Acceleration Hybrid", "Autocross FSAE", "Autocross Hybrid", "Endurance FSAE", "Endurance Hybrid"])
        self.radiobutton_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nswe")

class UpperFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # UpperFrame Config
        self.grid_columnconfigure(1, weight=2)
        self.configure(fg_color="transparent")

        # Frames
        self.menu_frame = MenuFrame(self)
        self.menu_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nswe")

        self.menu_frame = DefaultViewFrame(self)
        self.menu_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nswe")

        

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Initialization for GUI
        self.title("Zips Racing Electric Car Config")
        self.geometry("800x600")

        # Frames
        self.grid_columnconfigure(0 , weight=1)

        self.upper_frame = UpperFrame(self)
        self.upper_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nswe")

        self.button_frame = ButtonFrame(self)
        self.button_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nswe")

    def get_preset(self):
        print("preset selected:", self.checkbox_frame.get())

app = App()
app.mainloop()
