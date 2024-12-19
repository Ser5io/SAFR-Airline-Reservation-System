from interface.window import Window
import customtkinter
from PIL import ImageTk, Image



FONT_SIZE_MEDIUM = 16
FONT_SIZE_LARGE = 40

class Information(Window):
    def __init__(self, master):
        super().__init__(master)
        self.draw_frame()
    
    def draw_frame(self):
        self.configure(fg_color="white")
        self.configure_layout()
        
        self.create_logo()
        self.create_enterdata_label()
        self.create_name_box()
        self.create_national_id()
        self.create_phonenumber()
        self.create_travellers()
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
                                    font=("Poppins", FONT_SIZE_MEDIUM, "bold"))
        logo.grid(row=0,
                column=0,
                pady=10,
                padx=10,
                sticky="nw")

    def create_enterdata_label(self):
        enterdata = customtkinter.CTkLabel(self,
                                        text="Enter your information..",
                                        fg_color="white",
                                        text_color="black",
                                        font=("Poppins", FONT_SIZE_LARGE, "bold"),
                                        justify="center")
        enterdata.grid(row=1,
                       column=1,
                       sticky="ew",
                       columnspan=2)
        
    def create_name_box(self):
        name_label = customtkinter.CTkLabel(self,
                                    text="Name : ",
                                    font=("Poppins", FONT_SIZE_MEDIUM, "bold"))
        name_label.grid(row=2,
                        column=1,
                        pady=(10, 0),
                        sticky="e")

        self.name = customtkinter.CTkEntry(self,
                                      placeholder_text="Name",
                                      fg_color="#d1dbe4",
                                      text_color="black",
                                      placeholder_text_color="gray",
                                      border_width=0,
                                      corner_radius=100)
        self.name.grid(row=2,
                  column=2,
                  padx=(10, 0),
                  pady=(10, 0),
                  sticky="ew")
        
    
    def create_national_id(self):
        national_id_label = customtkinter.CTkLabel(self,
                                    text="National ID:",
                                    font=("Poppins", FONT_SIZE_MEDIUM, "bold"))
        national_id_label.grid(row=3,
                               column=1,
                               pady=(10, 0),
                               sticky="e")

        self.national_id = customtkinter.CTkEntry(self,
                                             placeholder_text="National ID",
                                             fg_color="#d1dbe4",
                                             text_color="black",
                                             placeholder_text_color="gray",
                                             border_width=0,
                                             corner_radius=100)
        self.national_id.grid(row=3,
                         column=2,
                         padx=(10, 0),
                         pady=(10, 0),
                         sticky="ew")
    
    def create_phonenumber(self):
        phonenumber_label = customtkinter.CTkLabel(self,
                                    text="Phone Number:",
                                    font=("Poppins", FONT_SIZE_MEDIUM, "bold"))
        phonenumber_label.grid(row=4,
                               column=1,
                               pady=(10, 0),
                               sticky="e")

        self.phonenumber = customtkinter.CTkEntry(self,
                                             placeholder_text="Phone Number",
                                             fg_color="#d1dbe4",
                                             text_color="black",
                                             placeholder_text_color="gray",
                                             border_width=0,
                                             corner_radius=100)
        self.phonenumber.grid(row=4,
                         column=2,
                         padx=(10, 0),
                         pady=(10, 0),
                         sticky="ew")
    
    def create_travellers(self):
        travellers_label = customtkinter.CTkLabel(self,
                                                  text="Travellers: ",
                                                  font=("Poppins", FONT_SIZE_MEDIUM, "bold"))
        travellers_label.grid(row=5,
                              column=1,
                              pady=(10, 0),
                              sticky="e")


        self.travellers_var = customtkinter.StringVar()
        self.travellers_combobox = customtkinter.CTkComboBox(self,
                                            values=["1"],
                                            fg_color="#d1dbe4",  # ComboBox background color
                                            text_color="black",
                                            border_width=0,
                                            dropdown_fg_color="#d1dbe4",  # Dropdown menu background color
                                            dropdown_text_color="black",  # Dropdown menu text color
                                            corner_radius=30,
                                            variable=self.travellers_var)
        self.travellers_combobox.set('')
        self.travellers_combobox.grid(row=5,
                                 column=2,
                                 padx=(10, 0),
                                 pady=(10, 0),
                                 sticky="ew")
    
    def create_next_button(self):
        next_button = customtkinter.CTkButton(self,
                                        text="Next >>",
                                        fg_color="#0E0055",
                                        text_color="#ffffff",
                                        corner_radius=100,
                                        font=("Poppins", FONT_SIZE_MEDIUM, "bold"),
                                        hover_color="#0065B4",
                                        command=self.show_location_page)
        next_button.grid(row=6,
                         column=2,
                         padx=(10, 0),
                         pady=(10, 0),
                         sticky="e")
        
        self.errormsg = customtkinter.CTkLabel(self,
                                        text='',
                                        fg_color="white",
                                        text_color="red",
                                        font=("Poppins", FONT_SIZE_MEDIUM, "bold"),
                                        justify="center")
        self.errormsg.grid(row=7,
                      column=2,
                      padx=(10,0),
                      pady=(10,0),
                      sticky='ne')
        
    def show_location_page(self):
        
        if self.name.get() == '' or self.national_id.get() == '' or self.phonenumber.get() == '' or self.travellers_combobox.get() == '':
            self.errormsg.configure(text='Please fill your informations')
            return
        elif len(self.name.get()) > 20:
            self.errormsg.configure(text='you cant make the name more then 20 character')
            return
        
        
        self.master.ticket.name_left.configure(text=self.name.get())
        self.master.ticket.name_right.configure(text=self.name.get())
        self.name.delete(0, 'end')
        self.national_id.delete(0, 'end')
        self.phonenumber.delete(0, 'end')
        self.errormsg.configure(text='')
        self.travellers_combobox.set('')

        self.master.windows[self.master.current_window].grid_remove()
        
        self.master.current_window = self.master.LOCATION_PAGE
        self.master.windows[self.master.current_window].grid(row=0, column=0, sticky='nsew')
    
    def configure_layout(self):
        self.grid_rowconfigure((0, 7), weight=1)
        self.grid_columnconfigure((0, 3), weight=1)
        self.grid_columnconfigure(2, weight=2)

    def clear_frame(self):
        pass