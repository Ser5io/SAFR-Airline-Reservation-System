import customtkinter
from PIL import ImageTk, Image
from interface.window import Window
from interface.ticket import Llist

FONT_MAX_SIZE = 40
FONT_MIN_SIZE = 15

class Seats(Window):
    def __init__(self, master):
        super().__init__(master)
        self.draw_frame()
    
    def draw_frame(self):
        self.configure(fg_color="white")
        self.configure_layout()
        
        print()
        
        self.create_logo()
        self.cerate_please_choose()
        self.create_section()
        self.create_number()
        self.create_plane()
        self.create_next()
        
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
    
        
    def cerate_please_choose(self):
        pleasechoose = customtkinter.CTkLabel(self,
                                        text="Please Choose A Seat",
                                        fg_color="white",
                                        text_color="black",
                                        font=("Poppins", FONT_MAX_SIZE, "bold"),
                                        justify="center")
        pleasechoose.grid(row=1, 
                        column=0, 
                        columnspan=3,
                        sticky='ew')
        
    def create_section(self):
        section = customtkinter.CTkLabel(self,
                                    text="Section : ",
                                    font=("Poppins", FONT_MAX_SIZE, "bold"))
        section.grid(row=2, 
                    column=0,
                    sticky='e',
                    padx=(10,0),
                    pady=(0,0))

        options = ["A", "B", "C", "D"]
        self.section_combo_box = customtkinter.CTkComboBox(self,
                                            values=options,
                                            fg_color="#d1dbe4",  # ComboBox background color
                                            text_color="black",
                                            border_width=0,
                                            dropdown_fg_color="#d1dbe4",  # Dropdown menu background color
                                            dropdown_text_color="black",  # Dropdown menu text color
                                            corner_radius=30)
        self.section_combo_box.set("Choose an option")  # Set the default value
        self.section_combo_box.grid(row=2, 
                            column=1, 
                            columnspan=2, 
                            sticky='ew')
    
    def create_number(self):
        number = customtkinter.CTkLabel(self,
                                    text="Number : ",
                                    font=("Poppins", FONT_MAX_SIZE, "bold"))
        number.grid(row=3,
                    column=0,
                    sticky='e',
                    padx=(10,0),
                    pady=(0,0))

        options = ["1", "2", "3", "4",
                "5", "6", "7", "8",
                "9", "10", "11", "12"]
        self.number_combo_box = customtkinter.CTkComboBox(self,
                                            values=options,
                                            fg_color="#d1dbe4",  # ComboBox background color
                                            text_color="black",
                                            border_width=0,
                                            dropdown_fg_color="#d1dbe4",  # Dropdown menu background color
                                            dropdown_text_color="black",  # Dropdown menu text color
                                            corner_radius=30)
        self.number_combo_box.set("Choose an option")  # Set the default value
        self.number_combo_box.grid(row=3,
                            column=1,
                            columnspan=2,
                            sticky='ew')
        
    def create_plane(self):
        planeimage = Image.open("images/seats.png")
        resized_plane = planeimage.resize((152, 500))
        plane = ImageTk.PhotoImage(resized_plane)

        planeImage = customtkinter.CTkLabel(self,
                                    image=plane,
                                    text="",
                                    justify="center")
        planeImage.grid(row=0,
                        column=3,
                        rowspan=4,
                        sticky='nsew')
        
    def create_next(self):
        next = customtkinter.CTkButton(self,
                                        text="Next >>",
                                        fg_color="#0E0055",
                                        text_color="#ffffff",
                                        corner_radius=100,
                                        font=("Poppins", FONT_MIN_SIZE+5, "bold"),
                                        hover_color="#0065B4",
                                        command=self.show_ticket_page)
        next.grid(row=4,
                column=3,
                sticky='ew',
                padx=(50,50),
                pady=(20,0))
        
    def show_ticket_page(self):
        global Llist
        Llist[5] = self.section_combo_box.get() + self.number_combo_box.get()
        
        self.section_combo_box.set('')
        self.number_combo_box.set('')
        
        self.master.windows[self.master.current_window].grid_remove()
        
        self.master.current_window = self.master.TICKET_PAGE
        self.master.windows[self.master.current_window].grid(row=0, column=0, sticky='nsew')
    
    
    def configure_layout(self):
        self.grid_columnconfigure((1, 3), weight=1)
        self.grid_columnconfigure(2, weight=5)
        self.grid_rowconfigure(7,weight=1)
    
    def clear_frame(self):
        pass