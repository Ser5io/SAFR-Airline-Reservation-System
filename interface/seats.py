import tkinter
import customtkinter
from PIL import ImageTk, Image

class Seats(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        self.master.geometry("1920x1080")
        self.master.title('Welcome To SAFR')
        self.master.iconbitmap("images/Logo.ico")
        self.configure(fg_color="white")




        original_header = Image.open("images/seats.png")
        resized_header = original_header.resize((288, 938))
        header = ImageTk.PhotoImage(resized_header)

        l1 = customtkinter.CTkLabel(self,
                                    image=header,
                                    text="",
                                    justify="center",)
        l1.pack(pady=0)
        l1.place(relx=0.85, rely=0.5, anchor="center")

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

        # -- The Header Text -------------------------------------------------------

        heading = customtkinter.CTkLabel(self,
                                        text="Please Choose A Seat",
                                        fg_color="white",
                                        text_color="black",
                                        font=("Poppins", 70, "bold"),
                                        justify="center")
        heading.place(x=100, y=200)

        # --------------------------------------------------------------------------

        l1 = customtkinter.CTkLabel(self,
                                    text="Section : ",
                                    font=("Poppins", 35, "bold"))
        l1.place(x=150, y=400)

        options = ["A", "B", "C", "D"]
        combo_box = customtkinter.CTkComboBox(self,
                                            values=options,
                                            width=700,
                                            height=40,
                                            fg_color="#d1dbe4",  # ComboBox background color
                                            text_color="black",
                                            border_width=0,
                                            dropdown_fg_color="#d1dbe4",  # Dropdown menu background color
                                            dropdown_text_color="black",  # Dropdown menu text color
                                            corner_radius=30)
        combo_box.set("Choose an option")  # Set the default value
        combo_box.place(x=320, y=410)


        l2 = customtkinter.CTkLabel(self,
                                    text="Number : ",
                                    font=("Poppins", 35, "bold"))
        l2.place(x=150, y=570)

        options = ["1", "2", "3", "4",
                "5", "6", "7", "8",
                "9", "10", "11", "12"]
        combo_box = customtkinter.CTkComboBox(self,
                                            values=options,
                                            width=700,
                                            height=40,
                                            fg_color="#d1dbe4",  # ComboBox background color
                                            text_color="black",
                                            border_width=0,
                                            dropdown_fg_color="#d1dbe4",  # Dropdown menu background color
                                            dropdown_text_color="black",  # Dropdown menu text color
                                            corner_radius=30)
        combo_box.set("Choose an option")  # Set the default value
        combo_box.place(x=335, y=580)

        button0 = customtkinter.CTkButton(self,
                                        text="Next >>",
                                        fg_color="#0E0055",
                                        text_color="#ffffff",
                                        width=150,
                                        height=60,
                                        corner_radius=100,
                                        font=("Poppins", 30, "bold"),
                                        hover_color="#0065B4",
                                        command=master.go_to_finalticket)
        button0.place(x=1250, y=870)