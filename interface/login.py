import tkinter
import customtkinter
from PIL import ImageTk, Image
from interface.window import Window

        
#         # self.master.geometry("850x600")
#         # self.master.iconbitmap("Logo.ico")
#         # self.master.resizable(False, False)

BGCOLOR = '#E8E8E8'

class Login(Window):
    def __init__(self, master):
        super().__init__(master)
        self.draw_frame()
    
    def draw_frame(self):
        self.master.title('SAFR Login Page')
        self.configure_layout()
        
        self.create_back_ground()
        self.create_frame()
        self.create_MSG()
        self.create_username_entry()
        self.create_password_entry()
        self.cerate_login()
        self.create_google()
        self.create_facebook()
        self.create_signup()
        
    
    def create_back_ground(self):
        self.bg_image = ImageTk.PhotoImage(Image.open("images/pattern.png"))
        bg_label = customtkinter.CTkLabel(master=self, image=self.bg_image, text="")
        bg_label.grid(row=0, column=0, rowspan=10, columnspan=3, sticky="nsew")
        
    def create_frame(self):
        frame = customtkinter.CTkFrame(self,
                                    width=320,
                                    height=400,
                                    fg_color=BGCOLOR)
        frame.grid(row=1,
                rowspan=7,
                column=1,
                sticky='nesw')
    
    def create_MSG(self):
        MSG = customtkinter.CTkLabel(self,
                                    text="Log into your Account!",
                                    font=("Poppins", 20, "bold"),
                                    fg_color=BGCOLOR)
        MSG.grid(row=1,
                column=1,
                sticky='ew',
                pady=20,
                padx=20)
        
    def create_username_entry(self):
        username_entry = customtkinter.CTkEntry(self,
                                        placeholder_text="Username",
                                        width=220,
                                        fg_color=BGCOLOR)
        username_entry.grid(row=2,
                            column=1,
                            sticky='ew')
    
    def create_password_entry(self):
        password_entry = customtkinter.CTkEntry(self,
                                        placeholder_text="Password",
                                        width=220,
                                        show="*",
                                        fg_color=BGCOLOR)
        password_entry.grid(row=3,
                            column=1,
                            sticky='ew')
    

        forgot_password = customtkinter.CTkLabel(self,
                                    text="Forgot password",
                                    font=("Poppins", 11),
                                    fg_color=BGCOLOR)
        forgot_password.grid(row=4,
                            column=1,
                            sticky='w')
    
    def cerate_login(self):
        loginimage = ImageTk.PhotoImage(Image.open("images/enter.png").resize((20, 20), Image.Resampling.LANCZOS))
        loginbutton = customtkinter.CTkButton(self,
                                        text="Login",
                                        width=220,
                                        image=loginimage,
                                        corner_radius=5,
                                        font=("Poppins", 12, "bold"),
                                        command=self.button_function)
        loginbutton.grid(row=5,
                            column=1,
                            sticky='ew')
        
    def create_google(self):
        googleimage = ImageTk.PhotoImage(Image.open("images/Google__G__Logo.svg.webp").resize((20, 20), Image.Resampling.LANCZOS))
        googlebutton = customtkinter.CTkButton(self,
                                        text="Google",
                                        image=googleimage,
                                        width=105,
                                        height=20,
                                        corner_radius=5,
                                        compound="left",
                                        font=("Poppins", 12, "bold"),
                                        text_color="black",
                                        fg_color="white",
                                        hover_color="gray",
                                        command=self.button_function)
        googlebutton.grid(row=6,
                            column=1,
                            sticky='w')
        
    def create_facebook(self):
        facebbookimage = ImageTk.PhotoImage(Image.open("images/facebook.png").resize((20, 20), Image.Resampling.LANCZOS))
        facebookbutton = customtkinter.CTkButton(self,
                                        text="Facebook",
                                        image=facebbookimage,
                                        width=105,
                                        height=20,
                                        corner_radius=5,
                                        compound="left",
                                        font=("Poppins", 12, "bold"),
                                        text_color="black",
                                        fg_color="white",
                                        hover_color="gray",
                                        command=self.button_function)
        facebookbutton.grid(row=6,
                            column=1,
                            sticky='e')
        
    def create_signup(self):
        forgot = customtkinter.CTkLabel(self,
                                    text="Don't have an account?",
                                    font=("Poppins", 11.5),
                                    fg_color=BGCOLOR)
        forgot.grid(row=7,
                    column=1,
                    sticky='e')
        
        signupimage = ImageTk.PhotoImage(Image.open("images/add-contact_11710543.png").resize((20, 20), Image.Resampling.LANCZOS))
        signupbutton = customtkinter.CTkButton(self,
                                        text="Sign up",
                                        width=220,
                                        image=signupimage,
                                        corner_radius=5,
                                        font=("Poppins", 12, "bold"))
        signupbutton.grid(row=8,
                    column=1,
                    sticky='ew')


    def button_function(self):
        self.destroy()
        main_page = customtkinter.CTk()
        main_page.geometry("850x500")
        main_page.title('SAFR')
        l1 = customtkinter.CTkLabel(master=main_page, text="Home Page", font=("Poppins", 50, "bold"))
        l1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        main_page.mainloop()
    
    def configure_layout(self):
        self.grid_columnconfigure((0,2), weight=2)
        self.grid_columnconfigure(1, weight=0)
        self.grid_rowconfigure((0,9), weight=1)
    
    def clear_frame(self):
        pass