import customtkinter
from interface.window import Window
from PIL import ImageTk, Image



Uname = 'NULL'
Ulocationfrom = 'NULL'
Ulocationto = 'NULL'
Utype = 'NULL'
Uclass = 'NULL'
Useat = 'NULL'


Llist = [Uname,
Ulocationfrom,
Ulocationto,
Utype,
Uclass,
Useat]



FONT_MAX_SIZE = 40
FONT_MIN_SIZE = 15
TEST_COLOR = 'red'
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
        self.create_name_labels()
        self.create_from_labels()
        self.create_to_labels()
        self.create_date_labels()
        self.create_class_labels()
        self.create_gate_labels()
        self.create_flightnumber_labels()
        self.create_time_labels()
        self.create_seat_labels()
        self.create_home_page()
        self.load()
        
    def load(self):
        load_button = customtkinter.CTkButton(self,
                                            text="load",
                                            fg_color="#0E0055",
                                            text_color="#ffffff",
                                            corner_radius=100,
                                            font=("Poppins", FONT_MIN_SIZE, "bold"),
                                            hover_color="#0065B4",
                                            command=self.set_data)
        load_button.grid(row=1,
                        column=0,
                        pady=(10,10),
                        padx=(5,0),
                        sticky="w")
    
    
    def set_data(self):
        global Llist
        self.name_left.configure(text=Llist[0])
        self.name_right.configure(text=Llist[0])
        
        self.locationfrom_left.configure(text=Llist[1])
        self.locationfrom_right.configure(text=Llist[1])
        
        self.locationto_left.configure(text=Llist[2])
        self.locationto_right.configure(text=Llist[2])
        
        self.class_left.configure(text=Llist[4])
        self.class_right.configure(text=Llist[4])
        
        self.seat_left.configure(text=Llist[5])
        self.seat_right.configure(text=Llist[5])
    
    
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
        self.name_left = customtkinter.CTkLabel(self.frame,
                                        text=Uname,
                                        justify="left",
                                        bg_color="#F7F7F7",
                                        fg_color="#F7F7F7",
                                        font=("Poppins", FONT_MIN_SIZE))
        self.name_left.place(x=69 ,y=133 ,anchor="w")
        
        self.name_right = customtkinter.CTkLabel(self.frame,
                                        text=Uname,
                                        justify="left",
                                        bg_color="#F7F7F7",
                                        fg_color="#F7F7F7",
                                        font=("Poppins", FONT_MIN_SIZE))
        self.name_right.place(x=610, y=135, anchor="w")
        
    
    def create_from_labels(self):
        self.locationfrom_left = customtkinter.CTkLabel(self.frame,
                                        text=Ulocationfrom,
                                        justify="left",
                                        bg_color="#F7F7F7",
                                        fg_color='#F7F7F7',
                                        font=("Poppins", FONT_MIN_SIZE))
        self.locationfrom_left.place(x=69, y=170, anchor="w")
        
        self.locationfrom_right = customtkinter.CTkLabel(self.frame,
                                        text=Ulocationfrom,
                                        justify="left",
                                        bg_color="#F7F7F7",
                                        fg_color='#F7F7F7',
                                        font=("Poppins", FONT_MIN_SIZE))
        self.locationfrom_right.place(x=610, y=170, anchor="w")
        
    def create_to_labels(self):
        self.locationto_left = customtkinter.CTkLabel(self.frame,
                                        text=Ulocationto,
                                        justify="left",
                                        bg_color="#F7F7F7",
                                        fg_color='#F7F7F7',
                                        font=("Poppins", FONT_MIN_SIZE))
        self.locationto_left.place(x=49, y=205, anchor="w")
        
        self.locationto_right = customtkinter.CTkLabel(self.frame,
                                        text=Ulocationto,
                                        justify="left",
                                        bg_color="#F7F7F7",
                                        fg_color='#F7F7F7',
                                        font=("Poppins", FONT_MIN_SIZE))
        self.locationto_right.place(x=595, y=205, anchor="w")
        
    
    def create_date_labels(self):
        date_left = customtkinter.CTkLabel(self.frame,
                                        text="15-Mar",
                                        justify="left",
                                        bg_color="#F7F7F7",
                                        fg_color="#F7F7F7",
                                        font=("Poppins", FONT_MIN_SIZE))
        date_left.place(x=330, y=170, anchor="w")
        
        date_right = customtkinter.CTkLabel(self.frame,
                                        text="15-Mar",
                                        justify="left",
                                        bg_color="#F7F7F7",
                                        fg_color="#F7F7F7",
                                        font=("Poppins", FONT_MIN_SIZE))
        date_right.place(x=571, y=246, anchor="nw")
        
    
    def create_class_labels(self):
        self.class_left = customtkinter.CTkLabel(self.frame,
                                            text=Uclass,
                                            justify="left",
                                            bg_color="#F7F7F7",
                                            fg_color="#F7F7F7",
                                            font=("Poppins", FONT_MIN_SIZE))
        self.class_left.place(x=335, y=205, anchor="w")
        
        self.class_right = customtkinter.CTkLabel(self.frame,
                                        text=Uclass,
                                        justify="left",
                                        bg_color="#F7F7F7",
                                        fg_color="#F7F7F7",
                                        font=("Poppins", FONT_MIN_SIZE))
        self.class_right.place(x=712, y=246, anchor="nw")
        
    
    def create_gate_labels(self):
        gate_left = customtkinter.CTkLabel(self.frame,
                                        text="A02",
                                        justify="left",
                                        bg_color="#F7F7F7",
                                        fg_color="#F7F7F7",
                                        font=("Poppins", FONT_MAX_SIZE - 15))
        gate_left.place(x=25, y=280, anchor="nw")

        
        gate_right = customtkinter.CTkLabel(self.frame,
                                        text="A02",
                                        justify="left",
                                        bg_color="#F7F7F7",
                                        fg_color="#F7F7F7",
                                        font=("Poppins", FONT_MIN_SIZE))
        gate_right.place(x=571, y=292, anchor="nw")
        
    def create_flightnumber_labels(self):
        flightnumber_left = customtkinter.CTkLabel(self.frame,
                                        text="ID02INA",
                                        justify="left",
                                        bg_color="#F7F7F7",
                                        fg_color="#F7F7F7",
                                        font=("Poppins", FONT_MAX_SIZE - 15))
        flightnumber_left.place(x=153, y=280, anchor="nw")

        
        flightnumber_right = customtkinter.CTkLabel(self.frame,
                                        text="ID02INA",
                                        justify="left",
                                        bg_color="#F7F7F7",
                                        fg_color="#F7F7F7",
                                        font=("Poppins", FONT_MIN_SIZE))
        flightnumber_right.place(x=640, y=292, anchor="nw")

        
    def create_time_labels(self):
        time_left = customtkinter.CTkLabel(self.frame,
                                        text="08:00 AM",
                                        justify="left",
                                        bg_color="#F7F7F7",
                                        fg_color="#F7F7F7",
                                        font=("Poppins", FONT_MAX_SIZE - 15))
        time_left.place(x=286, y=280, anchor="nw")

        
        time_right = customtkinter.CTkLabel(self.frame,
                                        text="08:00 AM",
                                        justify="left",
                                        bg_color="#F7F7F7",
                                        fg_color="#F7F7F7",
                                        font=("Poppins", FONT_MIN_SIZE))
        time_right.place(x=640, y=246, anchor="nw")

        
    def create_seat_labels(self):
        self.seat_left = customtkinter.CTkLabel(self.frame,
                                        text=Useat,
                                        justify="left",
                                        bg_color="#F7F7F7",
                                        fg_color="#F7F7F7",
                                        font=("Poppins", FONT_MAX_SIZE - 15))
        self.seat_left.place(x=422, y=280, anchor="nw")



        self.seat_right = customtkinter.CTkLabel(self.frame,
                                        text=Useat,
                                        justify="left",
                                        bg_color="#F7F7F7",
                                        fg_color="#F7F7F7",
                                        font=("Poppins", FONT_MIN_SIZE))
        self.seat_right.place(x=712, y=292, anchor="nw")
        
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