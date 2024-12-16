import tkinter
import customtkinter
from PIL import ImageTk, Image

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue")

class Data_page(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        self.master.geometry("1920x1080")
        self.master.title('Welcome To SAFR')
        self.master.iconbitmap("images/Logo.ico")
        self.configure(fg_color="white")

        heading = customtkinter.CTkLabel(self,
                                        text="Please Enter Your Data",
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

        l1 = customtkinter.CTkLabel(self,
                                    text="Name : ",
                                    font=("Poppins", 30, "bold"))
        l1.place(x=200, y=350)

        name = customtkinter.CTkEntry(self,
                                        placeholder_text="Name",
                                        width=500,
                                        height=40,
                                        fg_color="#d1dbe4",
                                        text_color="black",
                                        placeholder_text_color="gray",
                                        border_width=0,
                                        corner_radius=100)
        name.place(x=320, y=357)
        master.Uname = name.get()


        l2 = customtkinter.CTkLabel(self,
                                    text="National ID : ",
                                    font=("Poppins", 30, "bold"))
        l2.place(x=200, y=420)

        entry2 = customtkinter.CTkEntry(self,
                                        placeholder_text="National ID",
                                        width=500,
                                        height=40,
                                        fg_color="#d1dbe4",
                                        text_color="black",
                                        placeholder_text_color="gray",
                                        border_width=0,
                                        corner_radius=100)
        entry2.place(x=400, y=427)


        l3 = customtkinter.CTkLabel(self,
                                    text="Phone Number : ",
                                    font=("Poppins", 30, "bold"))
        l3.place(x=200, y=490)

        entry3 = customtkinter.CTkEntry(self,
                                        placeholder_text="Phone Number",
                                        width=500,
                                        height=40,
                                        fg_color="#d1dbe4",
                                        text_color="black",
                                        placeholder_text_color="gray",
                                        border_width=0,
                                        corner_radius=100)
        entry3.place(x=460, y=497)


        l4 = customtkinter.CTkLabel(self,
                                    text="Travellers : ",
                                    font=("Poppins", 30, "bold"))
        l4.place(x=200, y=560)

        options = ["1", "2", "3"]
        combo_box = customtkinter.CTkComboBox(self,
                                            values=options,
                                            width=500,
                                            height=40,
                                            fg_color="#d1dbe4",  # ComboBox background color
                                            text_color="black",
                                            border_width=0,
                                            dropdown_fg_color="#d1dbe4",  # Dropdown menu background color
                                            dropdown_text_color="black",  # Dropdown menu text color
                                            corner_radius=30)
        combo_box.set("Choose an option")  # Set the default value
        combo_box.place(x=390, y=566)


        button6 = customtkinter.CTkButton(self,
                                        text="Next >>",
                                        fg_color="#0E0055",
                                        text_color="#ffffff",
                                        width=150,
                                        height=60,
                                        corner_radius=100,
                                        font=("Poppins", 30, "bold"),
                                        hover_color="#0065B4",
                                        command=master.go_to_locationFrom)
        button6.place(x=1600, y=850)
