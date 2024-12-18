import customtkinter
from interface.window import Window
from PIL import ImageTk, Image

FONT_MAX_SIZE = 40
FONT_MIN_SIZE = 15
class Ticket(Window):
    def __init__(self, master):
        super().__init__(master)  
        self.draw_frame()
        
    def draw_frame(self):
        self.configure_layout()
        
        self.create_logo()
        self.create_frame()
        self.create_ticket_image()
        self.create_yourticket_label()
        # self.create_name_labels()
        # self.create_from_labels()
        # self.create_to_labels()
        # self.create_date_labels()
        # self.create_class_labels()
        # self.create_gate_labels()
        # self.create_flightnumber_labels()
        # self.create_time_labels()
        # self.create_seat_labels()
        self.create_home_page()
    
    
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
                sticky="nw")
        
    def create_frame(self):
        self.frame = customtkinter.CTkFrame(self,
                                    fg_color='white',)
        self.frame.grid(row=2,
                    column=0,
                    columnspan=2,
                    sticky="nesw",
                    padx=(100,0))
        # frame.grid_columnconfigure((1), weight=1)
        self.frame.grid_rowconfigure((0,6), weight=1)
    
    def create_yourticket_label(self):
        yourticket_label = customtkinter.CTkLabel(self,
                                        text="This is Your Ticket From SAFR",
                                        fg_color="white",
                                        text_color="black",
                                        font=("Poppins", FONT_MAX_SIZE, "bold"),
                                        justify="center")
        yourticket_label.grid(row=1,
                            column=0,
                            columnspan=3,
                            sticky='ew')
    
    def create_ticket_image(self):
        original_ticket = Image.open("images/final ticket.png")
        resized_ticket = original_ticket.resize((800,352))
        ticket_image = ImageTk.PhotoImage(resized_ticket)

        ticket = customtkinter.CTkLabel(self.frame,
                                        image=ticket_image,
                                        text="",)
        ticket.grid(row=0,
                    rowspan=4,
                    column=0,
                    columnspan=4,
                    sticky="nesw",
                    padx=(0,0))
    
    def create_name_labels(self):
        name_left = customtkinter.CTkLabel(self.frame,
                                        text="Kareem Ghazi",
                                        justify="left",
                                        bg_color="#F7F7F7",
                                        fg_color="#F7F7F7",
                                        font=("Poppins", 25))
        name_left.pack()
        name_left.place()
        
        name_right = customtkinter.CTkLabel(self.frame,
                                        text="Kareem Ghazi",
                                        justify="left",
                                        bg_color="#F7F7F7",
                                        fg_color="#F7F7F7",
                                        font=("Poppins", 20))
        # name_right.pack(pady=0)
        # name_right.place(relx=0.671, rely=0.56605, anchor="w")
    
    def create_from_labels(self):
        locationfrom_left = customtkinter.CTkLabel(self,
                                        text="Egypt",
                                        justify="left",
                                        bg_color="#F7F7F7",
                                        fg_color="#F7F7F7",
                                        font=("Poppins", 25))
        locationfrom_left.pack(pady=0)
        locationfrom_left.place(relx=0.235, rely=0.62, anchor="w")
        
        locationfrom_right = customtkinter.CTkLabel(self,
                                        text="Egypt",
                                        justify="left",
                                        bg_color="#F7F7F7",
                                        fg_color="#F7F7F7",
                                        font=("Poppins", 20))
        locationfrom_right.pack(pady=0)
        locationfrom_right.place(relx=0.671, rely=0.62, anchor="w")
        
    def create_to_labels(self):
        locationto_left = customtkinter.CTkLabel(self,
                                        text="Saudi Arabia",
                                        justify="left",
                                        bg_color="#F7F7F7",
                                        fg_color="#F7F7F7",
                                        font=("Poppins", 25))
        locationto_left.pack(pady=0)
        locationto_left.place(relx=0.22, rely=0.675, anchor="w")
        
        locationto_right = customtkinter.CTkLabel(self,
                                        text="Saudi Arabia",
                                        justify="left",
                                        bg_color="#F7F7F7",
                                        fg_color="#F7F7F7",
                                        font=("Poppins", 20))
        locationto_right.pack(pady=0)
        locationto_right.place(relx=0.66, rely=0.675, anchor="w")
    
    def create_date_labels(self):
        date_left = customtkinter.CTkLabel(self,
                                        text="15-Mar",
                                        justify="left",
                                        bg_color="#F7F7F7",
                                        fg_color="#F7F7F7",
                                        font=("Poppins", 25))
        date_left.pack(pady=0)
        date_left.place(relx=0.445, rely=0.6208, anchor="w")
        
        date_right = customtkinter.CTkLabel(self,
                                        text="15-Mar",
                                        justify="left",
                                        bg_color="#F7F7F7",
                                        fg_color="#F7F7F7",
                                        font=("Poppins", 20))
        date_right.pack(pady=0)
        date_right.place(relx=0.642, rely=0.755, anchor="w")
    
    def create_class_labels(self):
        class_left = customtkinter.CTkLabel(self,
                                            text="Economy",
                                            justify="left",
                                            bg_color="#F7F7F7",
                                            fg_color="#F7F7F7",
                                            font=("Poppins", 25))
        class_left.pack(pady=0)
        class_left.place(relx=0.45, rely=0.675, anchor="w")
        
        class_right = customtkinter.CTkLabel(self,
                                        text="Economy",
                                        justify="left",
                                        bg_color="#F7F7F7",
                                        fg_color="#F7F7F7",
                                        font=("Poppins", 20))
        class_right.pack(pady=0)
        class_right.place(relx=0.758, rely=0.755, anchor="w")
    
    def create_gate_labels(self):
        gate_left = customtkinter.CTkLabel(self,
                                        text="A02",
                                        justify="left",
                                        bg_color="#F7F7F7",
                                        fg_color="#F7F7F7",
                                        font=("Poppins", 25))
        gate_left.pack(pady=0)
        gate_left.place(relx=0.195, rely=0.815, anchor="w")
        
        gate_right = customtkinter.CTkLabel(self,
                                        text="A02",
                                        justify="left",
                                        bg_color="#F7F7F7",
                                        fg_color="#F7F7F7",
                                        font=("Poppins", 20))
        gate_right.pack(pady=0)
        gate_right.place(relx=0.642, rely=0.828, anchor="w")
    
    def create_flightnumber_labels(self):
        flightnumber_left = customtkinter.CTkLabel(self,
                                        text="ID02INA",
                                        justify="left",
                                        bg_color="#F7F7F7",
                                        fg_color="#F7F7F7",
                                        font=("Poppins", 25))
        flightnumber_left.pack(pady=0)
        flightnumber_left.place(relx=0.3, rely=0.815, anchor="w")
        
        flightnumber_right = customtkinter.CTkLabel(self,
                                        text="ID02INA",
                                        justify="left",
                                        bg_color="#F7F7F7",
                                        fg_color="#F7F7F7",
                                        font=("Poppins", 20))
        flightnumber_right.pack(pady=0)
        flightnumber_right.place(relx=0.7, rely=0.828, anchor="w")
        
    def create_time_labels(self):
        time_left = customtkinter.CTkLabel(self,
                                        text="08:00 AM",
                                        justify="left",
                                        bg_color="#F7F7F7",
                                        fg_color="#F7F7F7",
                                        font=("Poppins", 25))
        time_left.pack(pady=0)
        time_left.place(relx=0.41, rely=0.815, anchor="w")
        
        time_right = customtkinter.CTkLabel(self,
                                        text="08:00 AM",
                                        justify="left",
                                        bg_color="#F7F7F7",
                                        fg_color="#F7F7F7",
                                        font=("Poppins", 20))
        time_right.pack(pady=0)
        time_right.place(relx=0.7, rely=0.755, anchor="w")
        
    def create_seat_labels(self):
        seat_left = customtkinter.CTkLabel(self,
                                        text="36C",
                                        justify="left",
                                        bg_color="#F7F7F7",
                                        fg_color="#F7F7F7",
                                        font=("Poppins", 25))
        seat_left.pack(pady=0)
        seat_left.place(relx=0.517, rely=0.815, anchor="w")


        seat_right = customtkinter.CTkLabel(self,
                                        text="36C",
                                        justify="left",
                                        bg_color="#F7F7F7",
                                        fg_color="#F7F7F7",
                                        font=("Poppins", 20))
        seat_right.pack(pady=0)
        seat_right.place(relx=0.758, rely=0.828, anchor="w")
        
    def create_home_page(self):
        next_button = customtkinter.CTkButton(self,
                                            text="Home Page >>",
                                            fg_color="#0E0055",
                                            text_color="#ffffff",
                                            corner_radius=100,
                                            font=("Poppins", FONT_MIN_SIZE, "bold"),
                                            hover_color="#0065B4",
                                            command=self.show_homepage_page)
        next_button.grid(row=0,
                        column=1,
                        pady=(10,0),
                        padx=(5,50),
                        sticky="e")
    
    def show_homepage_page(self):
        self.master.windows[self.master.current_window].grid_remove()
        
        self.master.current_window = self.master.MAIN_PAGE
        self.master.windows[self.master.current_window].grid(row=0, column=0, sticky='nsew')
    
    def configure_layout(self):
        self.grid_columnconfigure(1,weight=3)
        self.grid_columnconfigure((0,2),weight=1)
        self.grid_rowconfigure((0,1,3),weight=1)
        self.grid_rowconfigure(2,weight=2)
    
#     def clear_frame(self):
#         pass