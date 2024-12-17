import customtkinter
from PIL import ImageTk, Image
from interface.window import Window

class Seats(Window):
    def __init__(self, master):
        super().__init__(master)
        self.draw_frame()
    
    def draw_frame(self):
        self.configure(fg_color="white")
        self.configure_layout()
        
        self.create_navigation_bar()
        self.cerate_please_choose()
        self.create_section()
        self.create_number()
        self.create_plane()
        self.create_next()
        
    def create_navigation_bar(self):
        logo = customtkinter.CTkLabel(self,
                                    text="SAFR",
                                    fg_color="white",
                                    text_color="black",
                                    font=("Poppins", 25, "bold")
)
        logo.grid(row=0, 
                column=0,
                sticky='w')
        
    def cerate_please_choose(self):
        pleasechoose = customtkinter.CTkLabel(self,
                                        text="Please Choose A Seat",
                                        fg_color="white",
                                        text_color="black",
                                        font=("Poppins", 70, "bold"),
                                        justify="center")
        pleasechoose.grid(row=1, 
                        column=0, 
                        columnspan=2,
                        sticky='ew')
        
    def create_section(self):
        section = customtkinter.CTkLabel(self,
                                    text="Section : ",
                                    font=("Poppins", 35, "bold"))
        section.grid(row=2, 
                    column=0, 
                    sticky='e')

        options = ["A", "B", "C", "D"]
        section_combo_box = customtkinter.CTkComboBox(self,
                                            values=options,
                                            width=700,
                                            height=40,
                                            fg_color="#d1dbe4",  # ComboBox background color
                                            text_color="black",
                                            border_width=0,
                                            dropdown_fg_color="#d1dbe4",  # Dropdown menu background color
                                            dropdown_text_color="black",  # Dropdown menu text color
                                            corner_radius=30)
        section_combo_box.set("Choose an option")  # Set the default value
        section_combo_box.grid(row=2, 
                            column=1, 
                            sticky='ew')
    
    def create_number(self):
        number = customtkinter.CTkLabel(self,
                                    text="Number : ",
                                    font=("Poppins", 35, "bold"))
        number.grid(row=3,
                    column=0,
                    sticky='ew')

        options = ["1", "2", "3", "4",
                "5", "6", "7", "8",
                "9", "10", "11", "12"]
        number_combo_box = customtkinter.CTkComboBox(self,
                                            values=options,
                                            width=700,
                                            height=40,
                                            fg_color="#d1dbe4",  # ComboBox background color
                                            text_color="black",
                                            border_width=0,
                                            dropdown_fg_color="#d1dbe4",  # Dropdown menu background color
                                            dropdown_text_color="black",  # Dropdown menu text color
                                            corner_radius=30)
        number_combo_box.set("Choose an option")  # Set the default value
        number_combo_box.grid(row=3,
                            column=1,
                            sticky='ew')
        
    def create_plane(self):
        planeimage = Image.open("images/seats.png")
        resized_plane = planeimage.resize((214, 700))
        plane = ImageTk.PhotoImage(resized_plane)

        planeImage = customtkinter.CTkLabel(self,
                                    image=plane,
                                    text="",
                                    justify="center")
        planeImage.grid(row=0,
                        column=3,
                        rowspan=4,
                        sticky='ew')
        
    def create_next(self):
        next = customtkinter.CTkButton(self,
                                        text="Next >>",
                                        fg_color="#0E0055",
                                        text_color="#ffffff",
                                        width=150,
                                        height=60,
                                        corner_radius=100,
                                        font=("Poppins", 30, "bold"),
                                        hover_color="#0065B4",
                                        command=self.master.show_next_frame)
        next.grid(row=4,
                column=3,
                sticky='ew',
                padx=10,
                pady=10)
    
    def configure_layout(self):
        self.grid_columnconfigure((1, 3), weight=1)
        self.grid_columnconfigure(2, weight=5)
        self.grid_rowconfigure(7,weight=1)
    
    def clear_frame(self):
        pass