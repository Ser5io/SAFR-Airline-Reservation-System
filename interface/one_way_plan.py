import tkinter
import customtkinter
from PIL import ImageTk, Image

class One_Way(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        self.master.geometry("1920x1080")
        self.master.title('Welcome To SAFR')
        self.master.iconbitmap("images/Logo.ico")
        self.configure(fg_color="white")
        
        heading = customtkinter.CTkLabel(self,
                                        text="Choose The Plan For One-way",
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

        def economy():
            master.Uflighttype = 'Economy'
            master.go_to_seats
            
        image_path1 = "images/ticket 1.png"
        image1 = Image.open(image_path1).resize((2000, 2000))
        button_image1 = customtkinter.CTkImage(light_image=image1, dark_image=image1, size=(660, 250))

        ticket1 = customtkinter.CTkButton(self,
                                        image=button_image1,  # Set the image
                                        text="",
                                        fg_color="white",
                                        text_color="#ffffff",
                                        width=425,
                                        height=300,
                                        hover_color="#d1dbe4",
                                        corner_radius=10,
                                        command=economy)
        ticket1.place(x=200, y=350)
        
        

        def Premium_Economy():
            master.Uflighttype = 'Premium Economy'
            master.go_to_seats
        
        image_path2 = "images/ticket 2.png"
        image2 = Image.open(image_path2).resize((2000, 2000))
        button_image2 = customtkinter.CTkImage(light_image=image2, dark_image=image2, size=(660, 250))

        ticket2 = customtkinter.CTkButton(self,
                                        image=button_image2,  # Set the image
                                        text="",
                                        fg_color="white",
                                        text_color="#ffffff",
                                        width=425,
                                        height=300,
                                        hover_color="#d1dbe4",
                                        corner_radius=10,
                                        command=Premium_Economy)
        ticket2.place(x=1050, y=350)
        
        

        def Business():
            master.Uflighttype = 'Business'
            master.go_to_seats
            
        image_path3 = "images/ticket 3.png"
        image3 = Image.open(image_path3).resize((2000, 2000))
        button_image3 = customtkinter.CTkImage(light_image=image3, dark_image=image3, size=(660, 250))

        ticket3 = customtkinter.CTkButton(self,
                                        image=button_image3,  # Set the image
                                        text="",
                                        fg_color="white",
                                        text_color="#ffffff",
                                        width=425,
                                        height=300,
                                        hover_color="#d1dbe4",
                                        corner_radius=10,
                                        command=Business)
        ticket3.place(x=200, y=650)
        
        

        def First():
            master.Uflighttype = 'First'
            master.go_to_seats
        image_path4 = "images/ticket 4.png"
        image4 = Image.open(image_path4).resize((2000, 2000))
        button_image4 = customtkinter.CTkImage(light_image=image4, dark_image=image4, size=(660, 250))

        ticket4 = customtkinter.CTkButton(self,
                                        image=button_image4,  # Set the image
                                        text="",
                                        fg_color="white",
                                        text_color="#ffffff",
                                        width=425,
                                        height=300,
                                        hover_color="#d1dbe4",
                                        corner_radius=10,
                                        command=First)
        ticket4.place(x=1050, y=650)
        
        
