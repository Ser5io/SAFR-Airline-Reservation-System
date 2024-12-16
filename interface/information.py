from interface.window import Window
import customtkinter

class Information(Window):
    def __init__(self, master):
        super().__init__(master)
        self.draw_frame()
    
    def draw_frame(self):
        self.configure(fg_color="white")
        self.configure_layout()
        
        self.create_enterdata_label()
        self.create_name_box()
        self.create_national_id()
        self.create_phonenumber()
        self.create_travellers()
        self.create_next_button()
    
    def create_enterdata_label(self):
        enterdata = customtkinter.CTkLabel(self,
                                        text="Please Enter Your Data",
                                        fg_color="white",
                                        text_color="black",
                                        font=("Poppins", 70, "bold"),
                                        justify="center")
        enterdata.grid(row=1,
                       column=0,
                       sticky="ew",
                       columnspan=2)
        
    def create_name_box(self):
        name_label = customtkinter.CTkLabel(self,
                                    text="Name : ",
                                    font=("Poppins", 30, "bold"))
        name_label.grid(row=2,
                        column=0,
                        sticky="ew")

        name = customtkinter.CTkEntry(self,
                                      placeholder_text="Name",
                                      width=500,
                                      height=40,
                                      fg_color="#d1dbe4",
                                      text_color="black",
                                      placeholder_text_color="gray",
                                      border_width=0,
                                      corner_radius=100)
        name.grid(row=2,
                  column=1,
                  sticky="ew")
    
    def create_national_id(self):
        national_id_label = customtkinter.CTkLabel(self,
                                    text="National ID : ",
                                    font=("Poppins", 30, "bold"))
        national_id_label.grid(row=3,
                               column=0,
                               sticky="ew")

        national_id = customtkinter.CTkEntry(self,
                                             placeholder_text="National ID",
                                             width=500,
                                             height=40,
                                             fg_color="#d1dbe4",
                                             text_color="black",
                                             placeholder_text_color="gray",
                                             border_width=0,
                                             corner_radius=100)
        national_id.grid(row=3,
                         column=1,
                         sticky="ew")
    
    def create_phonenumber(self):
        phonenumber_label = customtkinter.CTkLabel(self,
                                    text="Phone Number : ",
                                    font=("Poppins", 30, "bold"))
        phonenumber_label.grid(row=4,
                               column=0,
                               sticky="ew")

        phonenumber = customtkinter.CTkEntry(self,
                                             placeholder_text="Phone Number",
                                             width=500,
                                             height=40,
                                             fg_color="#d1dbe4",
                                             text_color="black",
                                             placeholder_text_color="gray",
                                             border_width=0,
                                             corner_radius=100)
        phonenumber.grid(row=4,
                         column=1,
                         sticky="ew")
    
    def create_travellers(self):
        travellers_label = customtkinter.CTkLabel(self,
                                                  text="Travellers : ",
                                                  font=("Poppins", 30, "bold"))
        travellers_label.grid(row=5,
                              column=0,
                              sticky="ew")

        travellers_combobox_var = customtkinter.StringVar(value="Choose an Option..")
        travellers_combobox = customtkinter.CTkComboBox(self,
                                            values=["1", "2", "3"],
                                            width=500,
                                            height=40,
                                            fg_color="#d1dbe4",  # ComboBox background color
                                            text_color="black",
                                            border_width=0,
                                            dropdown_fg_color="#d1dbe4",  # Dropdown menu background color
                                            dropdown_text_color="black",  # Dropdown menu text color
                                            corner_radius=30,
                                            variable=travellers_combobox_var)
        travellers_combobox.grid(row=5,
                                 column=1,
                                 sticky="ew")
    
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
                                        command=self.master.go_to_locationFrom)
        next_button.grid(row=6,
                         column=1,
                         sticky="e")
    
    def configure_layout(self):
        self.grid_columnconfigure(1, weight=4)

    def clear_frame(self):
        pass