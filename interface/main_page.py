import customtkinter
from interface.window import Window
from PIL import ImageTk, Image

FONT_SIZE_MEDIUM = 16
FONT_SIZE_LARGE = 44

class MainPage(Window):
    def __init__(self, master):
        super().__init__(master)
        self.draw_frame()
    
    def draw_frame(self):
        self.configure_layout()
        
        self.create_background()
        self.create_introduction()
        self.create_navigation_bar()
    
    def create_navigation_bar(self):
        self.logo_icon = customtkinter.CTkImage(light_image=Image.open("images/Logo.ico"),
                                                dark_image=Image.open("images/Logo.ico"))
        self.logo = customtkinter.CTkLabel(self,
                                           text="  SAFR",
                                           fg_color="white",
                                           text_color="black",
                                           image=self.logo_icon,
                                           compound="left",
                                           anchor="center",
                                           font=("Poppins", FONT_SIZE_MEDIUM + 2, "bold"))
        self.logo.grid(row=0,
                       column=0,
                       pady=(25, 5),
                       sticky="ew")

        self.start_booking = customtkinter.CTkButton(self,
                                                     text="Start Booking",
                                                     fg_color="white",
                                                     border_color="#1b4552",
                                                     border_width=2,
                                                     text_color="#1b4552",
                                                     corner_radius=100,
                                                     font=("Poppins", FONT_SIZE_MEDIUM),
                                                     hover_color="#d1dbe4",
                                                     command=self.master.show_next_frame)
        self.start_booking.grid(row=0,
                                column=1,
                                pady=(25, 5),
                                padx=(10, 0),
                                sticky="ew")

        self.loginButton = customtkinter.CTkButton(self,
                                    text="Login",
                                    fg_color="white",
                                    border_color="#1b4552",
                                    border_width=2,
                                    text_color="#1b4552",
                                    corner_radius=100,
                                    font=("Poppins", FONT_SIZE_MEDIUM),
                                    hover_color="#d1dbe4")
        
        self.loginButton.grid(row=0,
                              column=2,
                              pady=(25, 5),
                              padx=(10, 0),
                              sticky="ew")

        self.sign_up = customtkinter.CTkButton(self,
                                    text="Sign up",
                                    fg_color="white",
                                    border_color="#1b4552",
                                    border_width=2,
                                    text_color="#1b4552",
                                    corner_radius=100,
                                    font=("Poppins", FONT_SIZE_MEDIUM),
                                    hover_color="#d1dbe4")
        self.sign_up.grid(row=0,
                            column=3,
                            pady=(25, 5),
                            padx=(10, 0),
                            sticky="ew")

        self.my_ticket = customtkinter.CTkButton(self,
                                    text="My Ticket",
                                    fg_color="white",
                                    border_color="#1b4552",
                                    border_width=2,
                                    text_color="#1b4552",
                                    corner_radius=100,
                                    font=("Poppins", FONT_SIZE_MEDIUM),
                                    hover_color="#d1dbe4")
        self.my_ticket.grid(row=0,
                              column=4,
                              pady=(25, 5),
                              padx=(10, 0),
                              sticky="ew")

        self.manager_system = customtkinter.CTkButton(self,
                                    text="Manager System",
                                    fg_color="white",
                                    border_color="#1b4552",
                                    border_width=2,
                                    text_color="#1b4552",
                                    corner_radius=100,
                                    font=("Poppins", FONT_SIZE_MEDIUM),
                                    hover_color="#d1dbe4")
        self.manager_system.grid(row=0,
                              column=5,
                              pady=(25, 5),
                              padx=(10, 0),
                              sticky="ew")
    
    def create_introduction(self):
        self.introduction = customtkinter.CTkLabel(self,
                                                   text="Find And Book\nA Great Experience",
                                                   fg_color="white",
                                                   text_color="black",
                                                   font=("Poppins", FONT_SIZE_LARGE, "bold"),
                                                   justify="center")
        self.introduction.grid(row=1,
                               column=0,
                               sticky="ew",
                               pady=(45, 0),
                               columnspan=7)
    
    def create_background(self):
        original_background = Image.open("images/header.jpg")
        resized_background = original_background.resize((1000, 332))
        background_image = ImageTk.PhotoImage(resized_background)

        self.background = customtkinter.CTkLabel(self,
                                                 image=background_image,
                                                 text="")
        self.background.grid(row=2,
                             column=0,
                             sticky="ew",
                             pady=(25, 0),
                             columnspan=7)
    
    def configure_layout(self):
        self.grid_columnconfigure((0, 6), weight=1)
    
    def clear_frame(self):
        pass