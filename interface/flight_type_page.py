import tkinter
import customtkinter
from PIL import ImageTk, Image


class Flight_Type_Page(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        self.master.geometry("1920x1080")
        self.master.title('Welcome To SAFR')
        self.master.iconbitmap("images/Logo.ico")
        self.configure(fg_color="white")



        heading = customtkinter.CTkLabel(self,
                                        text="Which Flight Type Do You Want?",
                                        fg_color="white",
                                        text_color="black",
                                        font=("Poppins", 70, "bold"),
                                        justify="center")
        heading.pack(pady=170)

        # -- navigation bar --------------------------------------------------------

        logo = customtkinter.CTkLabel(self,
                                    text="SAFR",
                                    fg_color="white",
                                    text_color="black",
                                    font=("Poppins", 25, "bold"))
        logo.pack(pady=0)
        logo.place(relx=0.065, rely=0.055, anchor="center")

        button1 = customtkinter.CTkButton(self,
                                        text="Start Booking",
                                        fg_color="white",
                                        text_color="#1b4552",
                                        corner_radius=100,
                                        font=("Poppins", 15),
                                        hover_color="#d1dbe4")
        button1.place(x=562, y=40)

        button2 = customtkinter.CTkButton(self,
                                        text="Login",
                                        fg_color="white",
                                        text_color="#1b4552",
                                        corner_radius=100,
                                        font=("Poppins", 15),
                                        hover_color="#d1dbe4")
        button2.place(x=722, y=40)

        button3 = customtkinter.CTkButton(self,
                                        text="Sign up",
                                        fg_color="white",
                                        text_color="#1b4552",
                                        corner_radius=100,
                                        font=("Poppins", 15),
                                        hover_color="#d1dbe4")
        button3.place(x=882, y=40)

        button4 = customtkinter.CTkButton(self,
                                        text="My Ticket",
                                        fg_color="white",
                                        text_color="#1b4552",
                                        corner_radius=100,
                                        font=("Poppins", 15),
                                        hover_color="#d1dbe4")
        button4.place(x=1042, y=40)

        button5 = customtkinter.CTkButton(self,
                                        text="Manager System",
                                        fg_color="white",
                                        text_color="#1b4552",
                                        corner_radius=100,
                                        font=("Poppins", 15),
                                        hover_color="#d1dbe4")
        button5.place(x=1202, y=40)

        # --------------------------------------------------------------------------

        img1 = ImageTk.PhotoImage(Image.open("images/one-way.png").resize((70, 70), Image.Resampling.LANCZOS))
        btn1 = customtkinter.CTkButton(self,
                                    text="One-way",
                                    image=img1,
                                    fg_color="#0E0055",
                                    text_color="#ffffff",
                                    width=425,
                                    height=300,
                                    corner_radius=60,
                                    font=("Poppins", 30, "bold"),
                                    hover_color="#0065B4",
                                    command=master.go_to_oneway)
        btn1.place(x=1062.5, y=400)

        img2 = ImageTk.PhotoImage(Image.open("images/round-trip.png").resize((70, 70), Image.Resampling.LANCZOS))
        btn2 = customtkinter.CTkButton(self,
                                    text="Round-trip",
                                    image=img2,
                                    fg_color="#0E0055",
                                    text_color="#ffffff",
                                    width=425,
                                    height=300,
                                    corner_radius=60,
                                    font=("Poppins", 30, "bold"),
                                    hover_color="#0065B4",
                                    command=master.go_to_roundtrip)
        btn2.place(x=425, y=400)