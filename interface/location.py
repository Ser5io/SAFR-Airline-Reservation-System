from interface.window import Window
from interface.ticket import Llist
import customtkinter
from PIL import ImageTk, Image


FONT_MAX_SIZE = 40
FONT_MIN_SIZE = 15


class Location(Window):
    def __init__(self, master):
        super().__init__(master)
        self.draw_frame()
    
    def draw_frame(self):
        self.configure(fg_color="white")
        self.configure_layout()
        
        
        self.create_logo()
        self.create_chooselocation()
        self.create_location_from()
        self.create_location_to()
        self.create_next_button()
    
    def create_logo(self):
        logo_icon = customtkinter.CTkImage(light_image=Image.open("images/Logo.ico"),
                                                dark_image=Image.open("images/Logo.ico"))
        logo = customtkinter.CTkLabel(self,
                                    text="  SAFR",
                                    fg_color="white",
                                    text_color="black",
                                    image=logo_icon,
                                    compound="left",
                                    anchor="w",
                                    font=("Poppins", FONT_MIN_SIZE, "bold"))
        logo.grid(row=0,
                column=0,
                pady=(20,0),
                padx=(20,0),
                sticky="nesw")
    
    def create_chooselocation(self):
        heading = customtkinter.CTkLabel(self,
                                        text="Choose the locations..",
                                        fg_color="white",
                                        text_color="black",
                                        font=("Poppins", FONT_MAX_SIZE+20, "bold"),
                                        justify="center")
        heading.grid(row=1,
                    column=1,
                    pady=(120,5),
                    padx=10,
                    sticky="ew",
                    columnspan=2)

    def create_location_from(self):
        location_from_label = customtkinter.CTkLabel(self,
                                    text="Location from : ",
                                    font=("Poppins", FONT_MIN_SIZE+15, "bold"))
        location_from_label.grid(row=2,
                            column=1,
                            pady=(0,0),
                            padx=10,
                            sticky="w")

        self.location_from_combobox_var = customtkinter.StringVar()
        self.location_from_combobox = customtkinter.CTkComboBox(self,
                                            values=["Egypt",
                                                    "America",
                                                    "England",
                                                    "Brazil",
                                                    "China",
                                                    "France",
                                                    "Saudi Arabia",
                                                    "Emirates",
                                                    "Germany",
                                                    "Russia"],
                                            fg_color="#d1dbe4",  # ComboBox background color
                                            text_color="black",
                                            border_width=0,
                                            dropdown_fg_color="#d1dbe4",  # Dropdown menu background color
                                            dropdown_text_color="black",  # Dropdown menu text color
                                            corner_radius=30,
                                            variable=self.location_from_combobox_var)
        self.location_from_combobox.grid(row=2,
                        column=2,
                        columnspan=2,
                        pady=(0,0),
                        padx=(5,100),
                        sticky="ew")

    def create_location_to(self):
        location_to_label = customtkinter.CTkLabel(self,
                                                text="Location to : ",
                                                font=("Poppins", FONT_MIN_SIZE+15, "bold"))
        location_to_label.grid(row=3,
                            column=1,
                            padx=10,
                            pady=(0,0),
                            sticky="e")

        self.location_to_combobox_var = customtkinter.StringVar()
        self.location_to_combobox = customtkinter.CTkComboBox(self,
                                            values=["Egypt",
                                                    "America",
                                                    "England",
                                                    "Brazil",
                                                    "China",
                                                    "France",
                                                    "Saudi Arabia",
                                                    "Emirates",
                                                    "Germany",
                                                    "Russia"],
                                            fg_color="#d1dbe4",  # ComboBox background color
                                            text_color="black",
                                            border_width=0,
                                            dropdown_fg_color="#d1dbe4",  # Dropdown menu background color
                                            dropdown_text_color="black",  # Dropdown menu text color
                                            corner_radius=30,
                                            variable=self.location_to_combobox_var)
        self.location_to_combobox.grid(row=3,
                            column=2,
                            columnspan=2,
                            padx=(5,100),
                            pady=(0,0),
                            sticky="ew")
    
    
    def create_next_button(self):
        next_button = customtkinter.CTkButton(self,
                                            text="Next >>",
                                            fg_color="#0E0055",
                                            text_color="#ffffff",
                                            corner_radius=100,
                                            font=("Poppins", FONT_MIN_SIZE, "bold"),
                                            hover_color="#0065B4",
                                            command=self.show_flighttype_page)
        next_button.grid(row=4,
                        column=2,
                        pady=(10,0),
                        padx=(5,50),
                        sticky="e")
    
    def show_flighttype_page(self):
        global Llist
        Llist[1] = self.location_from_combobox.get()
        Llist[2] = self.location_to_combobox.get()
        
        
        self.master.windows[self.master.current_window].grid_remove()
        
        self.master.current_window = self.master.FLIGHT_TYPE_PAGE
        self.master.windows[self.master.current_window].grid(row=0, column=0, sticky='nsew')
        
    def configure_layout(self):
        self.grid_rowconfigure((0, 4), weight=0)
        self.grid_columnconfigure((0, 3), weight=1)
        self.grid_columnconfigure(2, weight=3)
    
    def clear_frame(self):
        pass
