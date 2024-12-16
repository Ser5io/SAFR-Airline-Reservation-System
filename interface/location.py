from interface.window import Window
import customtkinter

class Location(Window):
    def __init__(self, master):
        super().__init__(master)
        self.draw_frame()
    
    def draw_frame(self):
        self.configure(fg_color="white")
        self.configure_layout()
        
        self.create_logo()
        self.create_chooselocation()
        self.create_location_to()
        self.create_location_from()
        self.create_next_button()
    
    def create_logo(self):
        logo = customtkinter.CTkLabel(self,
                                           text="SAFR",
                                           fg_color="white",
                                           text_color="black",
                                           font=("Poppins", 25, "bold"))
        logo.grid(row=0,
                       column=0,
                       pady=10,
                       padx=10,
                       sticky="w")
    
    def create_chooselocation(self):
        heading = customtkinter.CTkLabel(self,
                                        text="Choose the locations..",
                                        fg_color="white",
                                        text_color="black",
                                        font=("Poppins", 70, "bold"),
                                        justify="center")
        heading.grid(row=1,
                       column=0,
                       pady=10,
                       padx=10,
                       sticky="ew",
                       columnspan=2)
    
    def create_location_to(self):
        location_to_label = customtkinter.CTkLabel(self,
                                                   text="Location to : ",
                                                   font=("Poppins", 35, "bold"))
        location_to_label.grid(row=2,
                               column=0,
                               pady=10,
                               padx=10,
                               sticky="w")

        location_to_combobox_var = customtkinter.StringVar()
        location_to_combobox = customtkinter.CTkComboBox(self,
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
                                            width=1000,
                                            height=40,
                                            fg_color="#d1dbe4",  # ComboBox background color
                                            text_color="black",
                                            border_width=0,
                                            dropdown_fg_color="#d1dbe4",  # Dropdown menu background color
                                            dropdown_text_color="black",  # Dropdown menu text color
                                            corner_radius=30,
                                            variable=location_to_combobox_var)
        location_to_combobox.grid(row=2,
                               column=1,
                               pady=10,
                               padx=10,
                               sticky="w")
    
    def create_location_from(self):
        location_from_label = customtkinter.CTkLabel(self,
                                    text="Location from : ",
                                    font=("Poppins", 35, "bold"))
        location_from_label.grid(row=3,
                               column=0,
                               pady=10,
                               padx=10,
                               sticky="w")

        location_from_combobox_var = customtkinter.StringVar()
        location_from = customtkinter.CTkComboBox(self,
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
                                            width=1000,
                                            height=40,
                                            fg_color="#d1dbe4",  # ComboBox background color
                                            text_color="black",
                                            border_width=0,
                                            dropdown_fg_color="#d1dbe4",  # Dropdown menu background color
                                            dropdown_text_color="black",  # Dropdown menu text color
                                            corner_radius=30,
                                            variable=location_from_combobox_var)
        location_from.grid(row=3,
                           column=1,
                           pady=10,
                           padx=10,
                           sticky="w")
    
    def create_next_button(self):
        next_button = customtkinter.CTkButton(self,
                                          text="Next >>",
                                          fg_color="#0E0055",
                                          text_color="#ffffff",
                                          width=150,
                                          height=60,
                                          corner_radius=100,
                                          font=("Poppins", 30, "bold"),
                                          hover_color="#0065B4",
                                          command=self.master.go_to_locationto)
        next_button.grid(row=4,
                         column=1,
                         pady=10,
                         padx=10,
                         sticky="e")
        
    def configure_layout(self):
        # self.grid_rowconfigure(1, weight=1)
        pass
    
    def clear_frame(self):
        pass
