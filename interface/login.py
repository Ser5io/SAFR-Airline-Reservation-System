import tkinter
import customtkinter
from PIL import ImageTk, Image

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue")


class Login(customtkinter.CTkFrame):
    def __init__(self,master):
        super().__init__(master)
        
        
        # self.master.geometry("850x600")
        # self.master.title('SAFR Login Page')
        # self.master.iconbitmap("Logo.ico")
        # self.master.resizable(False, False)


        img0 = ImageTk.PhotoImage(Image.open("images/pattern.png"))
        l1 = customtkinter.CTkLabel(master=self, image=img0)
        l1.pack()

        frame = customtkinter.CTkFrame(master=l1,
                                    width=320,
                                    height=400)
        frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        l2 = customtkinter.CTkLabel(master=frame,
                                    text="Log into your Account!",
                                    font=("Poppins", 20, "bold"))
        l2.place(x = 50, y = 35)

        entry1 = customtkinter.CTkEntry(master=frame,
                                        placeholder_text="Username",
                                        width=220)
        entry1.place(x = 50, y = 100)

        entry2 = customtkinter.CTkEntry(master=frame,
                                        placeholder_text="Password",
                                        width=220,
                                        show="*")
        entry2.place(x = 50, y = 145)

        l3 = customtkinter.CTkLabel(master=frame,
                                    text="Forgot password",
                                    font=("Poppins", 11))
        l3.place(x = 177, y = 175)

        img1 = ImageTk.PhotoImage(Image.open("images/enter.png").resize((20, 20), Image.Resampling.LANCZOS))
        button1 = customtkinter.CTkButton(master=frame,
                                        text="Login",
                                        width=220,
                                        image=img1,
                                        corner_radius=5,
                                        font=("Poppins", 12, "bold"),
                                        command=self.button_function)
        button1.place(x = 50, y = 210)

        img2 = ImageTk.PhotoImage(Image.open("images/Google__G__Logo.svg.webp").resize((20, 20), Image.Resampling.LANCZOS))
        button2 = customtkinter.CTkButton(master=frame,
                                        text="Google",
                                        image=img2,
                                        width=105,
                                        height=20,
                                        corner_radius=5,
                                        compound="left",
                                        font=("Poppins", 12, "bold"),
                                        text_color="black",
                                        fg_color="white",
                                        hover_color="gray",
                                        command=self.button_function)
        button2.place(x = 50, y = 250)

        img3 = ImageTk.PhotoImage(Image.open("images/facebook.png").resize((20, 20), Image.Resampling.LANCZOS))
        button3 = customtkinter.CTkButton(master=frame,
                                        text="Facebook",
                                        image=img3,
                                        width=105,
                                        height=20,
                                        corner_radius=5,
                                        compound="left",
                                        font=("Poppins", 12, "bold"),
                                        text_color="black",
                                        fg_color="white",
                                        hover_color="gray",
                                        command=self.button_function)
        button3.place(x = 165, y = 250)

        l4 = customtkinter.CTkLabel(master=frame,
                                    text="Don't have an account?",
                                    font=("Poppins", 11.5))
        l4.place(x = 50, y = 305)

        img4 = ImageTk.PhotoImage(Image.open("images/add-contact_11710543.png").resize((20, 20), Image.Resampling.LANCZOS))
        button1 = customtkinter.CTkButton(master=frame,
                                        text="Sign up",
                                        width=220,
                                        image=img4,
                                        corner_radius=5,
                                        font=("Poppins", 12, "bold"))
        button1.place(x = 50, y = 330)
                
    

    def button_function(self):
        self.destroy()
        main_page = customtkinter.CTk()
        main_page.geometry("850x500")
        main_page.title('SAFR')
        l1 = customtkinter.CTkLabel(master=main_page, text="Home Page", font=("Poppins", 50, "bold"))
        l1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        main_page.mainloop()
