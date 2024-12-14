import tkinter
import customtkinter
from PIL import ImageTk, Image
# from login import Login



customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue")

class MainPage(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        self.master.geometry("1920x1080")
        self.master.title('Welcome To SAFR')
        self.master.iconbitmap("images/Logo.ico")
        self.configure(fg_color="white")

        original_header = Image.open("images/header.jpg")
        resized_header = original_header.resize((1350, 450))
        header = ImageTk.PhotoImage(resized_header)

        self.l1 = customtkinter.CTkLabel(self,
                            image=header,
                            text="",
                            justify="center")
        self.l1.pack(pady=0)
        self.l1.place(relx=0.5, rely=0.65, anchor="center")

# -- The Header Text -------------------------------------------------------



        self.heading = customtkinter.CTkLabel(self,
                                        text="Find And Book\nA Great Experience",
                                        fg_color="white",
                                        text_color="black",
                                        font=("Poppins", 60, "bold"),
                                        justify="center")
        self.heading.pack(pady=230)

# -- navigation bar --------------------------------------------------------

        self.logo = customtkinter.CTkLabel(self,
                            text="SAFR",
                            fg_color="white",
                            text_color="black",
                            font=("Poppins", 25, "bold"))
        self.logo.pack(pady=0)
        self.logo.place(relx=0.065, rely=0.055, anchor="center")

        self.button1 = customtkinter.CTkButton(self,
                                    text="Start Booking",
                                    fg_color="white",
                                    text_color="#1b4552",
                                    corner_radius=100,
                                    font=("Poppins", 15),
                                    hover_color="#d1dbe4",
                                    command=master.start_booking)
        self.button1.place(x=562, y=40)

        self.loginButton = customtkinter.CTkButton(self,
                                    text="Login",
                                    fg_color="white",
                                    text_color="#1b4552",
                                    corner_radius=100,
                                    font=("Poppins", 15),
                                    hover_color="#d1dbe4")
        
        
        self.loginButton.place(x=722, y=40)

        self.button3 = customtkinter.CTkButton(self,
                                    text="Sign up",
                                    fg_color="white",
                                    text_color="#1b4552",
                                    corner_radius=100,
                                    font=("Poppins", 15),
                                    hover_color="#d1dbe4")
        self.button3.place(x=882, y=40)

        self.button4 = customtkinter.CTkButton(self,
                                    text="My Ticket",
                                    fg_color="white",
                                    text_color="#1b4552",
                                    corner_radius=100,
                                    font=("Poppins", 15),
                                    hover_color="#d1dbe4")
        self.button4.place(x=1042, y=40)

        self.button5 = customtkinter.CTkButton(self,
                                    text="Manager System",
                                    fg_color="white",
                                    text_color="#1b4552",
                                    corner_radius=100,
                                    font=("Poppins", 15),
                                    hover_color="#d1dbe4")
        self.button5.place(x=1202, y=40)
        

# --------------------------------------------------------------------------
