# import tkinter
# import customtkinter
# from PIL import ImageTk, Image

# class Final_Ticket(customtkinter.CTkFrame):
#     def __init__(self, master, Uname, Ulocationfrom, Ulocationto,Uflightype, Useat):
#         super().__init__(master)
        
#         self.master.geometry("1920x1080")
#         self.master.title('Welcome To SAFR')
#         self.master.iconbitmap("images/Logo.ico")
#         self.configure(fg_color="white")

#         original_header = Image.open("images/final ticket.png")
#         resized_header = original_header.resize((1250, 550))
#         header = ImageTk.PhotoImage(resized_header)

#         l1 = customtkinter.CTkLabel(self,
#                                     image=header,
#                                     text="",
#                                     justify="center",)
#         l1.pack(pady=0)
#         l1.place(relx=0.5, rely=0.65, anchor="center")




        
#         # name.configure(text=self.name)
        
        
        
#         # -- The Header Text -------------------------------------------------------



#         heading = customtkinter.CTkLabel(self,
#                                         text="This is Your Ticket From SAFR",
#                                         fg_color="white",
#                                         text_color="black",
#                                         font=("Poppins", 80, "bold"),
#                                         justify="center")
#         heading.pack(pady=230)

#         # -- navigation bar --------------------------------------------------------

#         logo = customtkinter.CTkLabel(self,
#                                     text="SAFR",
#                                     fg_color="white",
#                                     text_color="black",
#                                     font=("Poppins", 25, "bold"))
#         logo.pack(pady=0)
#         logo.place(relx=0.065, rely=0.055, anchor="center")

#         button1 = customtkinter.CTkButton(self,
#                                         text="Start Booking",
#                                         fg_color="white",
#                                         text_color="#1b4552",
#                                         corner_radius=100,
#                                         font=("Poppins", 15),
#                                         hover_color="#d1dbe4")
#         button1.place(x=562, y=40)

#         button2 = customtkinter.CTkButton(self,
#                                         text="Login",
#                                         fg_color="white",
#                                         text_color="#1b4552",
#                                         corner_radius=100,
#                                         font=("Poppins", 15),
#                                         hover_color="#d1dbe4")
#         button2.place(x=722, y=40)

#         button3 = customtkinter.CTkButton(self,
#                                         text="Sign up",
#                                         fg_color="white",
#                                         text_color="#1b4552",
#                                         corner_radius=100,
#                                         font=("Poppins", 15),
#                                         hover_color="#d1dbe4")
#         button3.place(x=882, y=40)

#         button4 = customtkinter.CTkButton(self,
#                                         text="My Ticket",
#                                         fg_color="white",
#                                         text_color="#1b4552",
#                                         corner_radius=100,
#                                         font=("Poppins", 15),
#                                         hover_color="#d1dbe4")
#         button4.place(x=1042, y=40)

#         button5 = customtkinter.CTkButton(self,
#                                         text="Manager System",
#                                         fg_color="white",
#                                         text_color="#1b4552",
#                                         corner_radius=100,
#                                         font=("Poppins", 15),
#                                         hover_color="#d1dbe4")
#         button5.place(x=1202, y=40)

#         # -- Labels ----------------------------------------------------------------

#         name = customtkinter.CTkLabel(self,
#                                         text=Uname,
#                                         justify="left",
#                                         bg_color="#F7F7F7",
#                                         fg_color="#F7F7F7",
#                                         font=("Poppins", 25))
#         name.pack(pady=0)
#         name.place(relx=0.235, rely=0.56605, anchor="w")


#         locationfrom = customtkinter.CTkLabel(self,
#                                         text=Ulocationfrom,
#                                         justify="left",
#                                         bg_color="#F7F7F7",
#                                         fg_color="#F7F7F7",
#                                         font=("Poppins", 25))
#         locationfrom.pack(pady=0)
#         locationfrom.place(relx=0.235, rely=0.62, anchor="w")


#         locationto = customtkinter.CTkLabel(self,
#                                         text=Ulocationto,
#                                         justify="left",
#                                         bg_color="#F7F7F7",
#                                         fg_color="#F7F7F7",
#                                         font=("Poppins", 25))
#         locationto.pack(pady=0)
#         locationto.place(relx=0.22, rely=0.675, anchor="w")


#         date = customtkinter.CTkLabel(self,
#                                         text="15-Mar",
#                                         justify="left",
#                                         bg_color="#F7F7F7",
#                                         fg_color="#F7F7F7",
#                                         font=("Poppins", 25))
#         date.pack(pady=0)
#         date.place(relx=0.445, rely=0.6208, anchor="w")


#         flighttype = customtkinter.CTkLabel(self,
#                                         text=Uflightype,
#                                         justify="left",
#                                         bg_color="#F7F7F7",
#                                         fg_color="#F7F7F7",
#                                         font=("Poppins", 25))
#         flighttype.pack(pady=0)
#         flighttype.place(relx=0.45, rely=0.675, anchor="w")


#         self.name2 = customtkinter.CTkLabel(self,
#                                         text=Uname,
#                                         justify="left",
#                                         bg_color="#F7F7F7",
#                                         fg_color="#F7F7F7",
#                                         font=("Poppins", 20))
#         self.name2.pack(pady=0)
#         self.name2.place(relx=0.671, rely=0.56605, anchor="w")
        


#         locationfrom2 = customtkinter.CTkLabel(self,
#                                         text=Ulocationfrom,
#                                         justify="left",
#                                         bg_color="#F7F7F7",
#                                         fg_color="#F7F7F7",
#                                         font=("Poppins", 20))
#         locationfrom2.pack(pady=0)
#         locationfrom2.place(relx=0.671, rely=0.62, anchor="w")


#         locationto2 = customtkinter.CTkLabel(self,
#                                         text=Ulocationto,
#                                         justify="left",
#                                         bg_color="#F7F7F7",
#                                         fg_color="#F7F7F7",
#                                         font=("Poppins", 20))
#         locationto2.pack(pady=0)
#         locationto2.place(relx=0.66, rely=0.675, anchor="w")


#         label9 = customtkinter.CTkLabel(self,
#                                         text="A02",
#                                         justify="left",
#                                         bg_color="#F7F7F7",
#                                         fg_color="#F7F7F7",
#                                         font=("Poppins", 25))
#         label9.pack(pady=0)
#         label9.place(relx=0.195, rely=0.815, anchor="w")


#         label10 = customtkinter.CTkLabel(self,
#                                         text="ID02INA",
#                                         justify="left",
#                                         bg_color="#F7F7F7",
#                                         fg_color="#F7F7F7",
#                                         font=("Poppins", 25))
#         label10.pack(pady=0)
#         label10.place(relx=0.3, rely=0.815, anchor="w")


#         time = customtkinter.CTkLabel(self,
#                                         text="08:00 AM",
#                                         justify="left",
#                                         bg_color="#F7F7F7",
#                                         fg_color="#F7F7F7",
#                                         font=("Poppins", 25))
#         time.pack(pady=0)
#         time.place(relx=0.41, rely=0.815, anchor="w")


#         seat = customtkinter.CTkLabel(self,
#                                         text=Useat,
#                                         justify="left",
#                                         bg_color="#F7F7F7",
#                                         fg_color="#F7F7F7",
#                                         font=("Poppins", 25))
#         seat.pack(pady=0)
#         seat.place(relx=0.517, rely=0.815, anchor="w")


#         label13 = customtkinter.CTkLabel(self,
#                                         text="A02",
#                                         justify="left",
#                                         bg_color="#F7F7F7",
#                                         fg_color="#F7F7F7",
#                                         font=("Poppins", 20))
#         label13.pack(pady=0)
#         label13.place(relx=0.642, rely=0.828, anchor="w")


#         label14 = customtkinter.CTkLabel(self,
#                                         text="ID02INA",
#                                         justify="left",
#                                         bg_color="#F7F7F7",
#                                         fg_color="#F7F7F7",
#                                         font=("Poppins", 20))
#         label14.pack(pady=0)
#         label14.place(relx=0.7, rely=0.828, anchor="w")


#         seat2 = customtkinter.CTkLabel(self,
#                                         text=Useat,
#                                         justify="left",
#                                         bg_color="#F7F7F7",
#                                         fg_color="#F7F7F7",
#                                         font=("Poppins", 20))
#         seat2.pack(pady=0)
#         seat2.place(relx=0.758, rely=0.828, anchor="w")


#         label16 = customtkinter.CTkLabel(self,
#                                         text="15-Mar",
#                                         justify="left",
#                                         bg_color="#F7F7F7",
#                                         fg_color="#F7F7F7",
#                                         font=("Poppins", 20))
#         label16.pack(pady=0)
#         label16.place(relx=0.642, rely=0.755, anchor="w")


#         label17 = customtkinter.CTkLabel(self,
#                                         text="08:00 AM",
#                                         justify="left",
#                                         bg_color="#F7F7F7",
#                                         fg_color="#F7F7F7",
#                                         font=("Poppins", 20))
#         label17.pack(pady=0)
#         label17.place(relx=0.7, rely=0.755, anchor="w")


#         label18 = customtkinter.CTkLabel(self,
#                                         text="FIRST",
#                                         justify="left",
#                                         bg_color="#F7F7F7",
#                                         fg_color="#F7F7F7",
#                                         font=("Poppins", 20))
#         label18.pack(pady=0)
#         label18.place(relx=0.758, rely=0.755, anchor="w")

import customtkinter
from PIL import Image
from interface.window import Window

class Ticket(customtkinter.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        
        self.draw_frame()
        
    def draw_frame(self):
        self.geometry("800x355")
        self.create_background()
        
    def create_background(self):
        my_image = customtkinter.CTkImage(light_image=Image.open("images/ticket_background.png"),
                                          dark_image=Image.open("images/ticket_background.png"),
                                          size=(800, 355))

        image_label = customtkinter.CTkLabel(self, image=my_image, text="")
        image_label.pack()
    
    def configure_layout(self):
        pass
    
    def clear_frame(self):
        pass