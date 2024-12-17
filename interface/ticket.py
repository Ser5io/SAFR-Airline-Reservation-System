import customtkinter
from interface.window import Window
from PIL import ImageTk, Image

class Ticket(Window):
    def __init__(self, master):
        super().__init__(master)
        
#         self.draw_frame()
        
    def draw_frame(self):
        self.configure_layout()
        
        self.create_ticket_image()
        self.create_yourticket_label()
        self.create_name_labels()
        self.create_from_labels()
        self.create_to_labels()
        self.create_date_labels()
        self.create_class_labels()
        self.create_gate_labels()
        self.create_flightnumber_labels()
        self.create_time_labels()
        self.create_seat_labels()
    
    def create_yourticket_label(self):
        yourticket_label = customtkinter.CTkLabel(self,
                                         text="This is Your Ticket From SAFR",
                                         fg_color="white",
                                         text_color="black",
                                         font=("Poppins", 80, "bold"),
                                         justify="center")
        yourticket_label.pack(pady=150)
    
    def create_ticket_image(self):
        original_ticket = Image.open("images/final ticket.png")
        resized_ticket = original_ticket.resize((1250, 550))
        ticket_image = ImageTk.PhotoImage(resized_ticket)

        ticket = customtkinter.CTkLabel(self,
                                        image=ticket_image,
                                        text="",
                                        justify="center",)
        ticket.pack(pady=0)
        ticket.place(relx=0.5, rely=0.65, anchor="center")
    
    def create_name_labels(self):
        name_left = customtkinter.CTkLabel(self,
                                        text="Kareem Ghazi",
                                        justify="left",
                                        bg_color="#F7F7F7",
                                        fg_color="#F7F7F7",
                                        font=("Poppins", 25))
        name_left.pack(pady=0)
        name_left.place(relx=0.235, rely=0.56605, anchor="w")
        
        name_right = customtkinter.CTkLabel(self,
                                        text="Kareem Ghazi",
                                        justify="left",
                                        bg_color="#F7F7F7",
                                        fg_color="#F7F7F7",
                                        font=("Poppins", 20))
        name_right.pack(pady=0)
        name_right.place(relx=0.671, rely=0.56605, anchor="w")
    
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
    
#     def configure_layout(self):
#         pass
    
#     def clear_frame(self):
#         pass