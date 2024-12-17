import tkinter
import customtkinter
from PIL import ImageTk, Image
from interface.window import Window

BGCOLOR = '#E8E8E8'
FONT_MAX_SIZE = 20
FONT_MIN_SIZE = 10

class Login(Window):
    def __init__(self, master):
        super().__init__(master)
        self.draw_frame()
    
    def draw_frame(self):
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
                                    fg_color=BGCOLOR,
                                    bg_color=BGCOLOR)
        frame.grid(row=1,
                rowspan=8,
                column=1,
                sticky='nesw')
    
    def create_MSG(self):
        MSG = customtkinter.CTkLabel(self,
                                    text="Log into your Account!",
                                    font=("Poppins", FONT_MAX_SIZE, "bold"),
                                    bg_color=BGCOLOR)
        MSG.grid(row=1,
                column=1,
                sticky='ew',
                padx=20,
                pady=(15,0))
        
    def create_username_entry(self):
        username_entry = customtkinter.CTkEntry(self,
                                        placeholder_text="Username",
                                        bg_color=BGCOLOR)
        username_entry.grid(row=2,
                            column=1,
                            sticky='ew',
                            padx=20,
                            pady=(15,0))
    
    def create_password_entry(self):
        password_entry = customtkinter.CTkEntry(self,
                                        placeholder_text="Password",
                                        show="*",
                                        bg_color=BGCOLOR)
        password_entry.grid(row=3,
                            column=1,
                            sticky='ew',
                            padx=20,
                            pady=(15,0))
    

        forgot_password = customtkinter.CTkLabel(self,
                                    text="Forgot password",
                                    font=("Poppins", FONT_MIN_SIZE),
                                    bg_color=BGCOLOR)
        forgot_password.grid(row=4,
                            column=1,
                            sticky='w',
                            padx=20,
                            pady=(0,0))
    
    def cerate_login(self):
        loginimage = ImageTk.PhotoImage(Image.open("images/enter.png").resize((20, 20), Image.Resampling.LANCZOS))
        loginbutton = customtkinter.CTkButton(self,
                                        text="Login",
                                        width=220,
                                        image=loginimage,
                                        corner_radius=5,
                                        font=("Poppins", FONT_MIN_SIZE, "bold"),
                                        command=self.show_mainpage)
        loginbutton.grid(row=5,
                            column=1,
                            sticky='ew',
                            padx=20,
                            pady=(15,0))
    
    def show_mainpage(self):
        self.master.windows[self.master.current_window].grid_remove()
        
        self.master.current_window = 0
        self.master.windows[self.master.current_window].grid(row=0, column=0, sticky='nsew')
        
    def create_google(self):
        googleimage = ImageTk.PhotoImage(Image.open("images/Google__G__Logo.svg.webp").resize((20, 20), Image.Resampling.LANCZOS))
        googlebutton = customtkinter.CTkButton(self,
                                        text="Google",
                                        image=googleimage,
                                        # width=105,
                                        # height=20,
                                        corner_radius=5,
                                        compound="left",
                                        font=("Poppins", FONT_MIN_SIZE, "bold"),
                                        text_color="black",
                                        fg_color=BGCOLOR,
                                        bg_color=BGCOLOR,
                                        hover_color="gray")
        googlebutton.grid(row=6,
                            column=1,
                            sticky='w',
                            padx=0,
                            pady=(15,0))
        
    def create_facebook(self):
        facebbookimage = ImageTk.PhotoImage(Image.open("images/facebook.png").resize((20, 20), Image.Resampling.LANCZOS))
        facebookbutton = customtkinter.CTkButton(self,
                                        text="Facebook",
                                        image=facebbookimage,
                                        # width=105,
                                        # height=20,
                                        corner_radius=5,
                                        compound="left",
                                        font=("Poppins", FONT_MIN_SIZE, "bold"),
                                        text_color="black",
                                        fg_color=BGCOLOR,
                                        bg_color=BGCOLOR,
                                        hover_color="gray")
        facebookbutton.grid(row=6,
                            column=1,
                            sticky='e',
                            padx=0,
                            pady=(15,0))
        
    def create_signup(self):
        forgot = customtkinter.CTkLabel(self,
                                    text="Don't have an account?",
                                    font=("Poppins", FONT_MIN_SIZE),
                                    bg_color=BGCOLOR)
        forgot.grid(row=7,
                    column=1,
                    sticky='e',
                    padx=20,
                    pady=(15,0))
        
        signupimage = ImageTk.PhotoImage(Image.open("images/add-contact_11710543.png").resize((20, 20), Image.Resampling.LANCZOS))
        signupbutton = customtkinter.CTkButton(self,
                                        text="Sign up",
                                        width=220,
                                        image=signupimage,
                                        corner_radius=5,
                                        font=("Poppins", FONT_MIN_SIZE, "bold"),
                                        command=self.show_signup_page)
        signupbutton.grid(row=8,
                    column=1,
                    sticky='ew',
                    padx=20,
                    pady=(0,15))
        
    def show_signup_page(self):
        self.master.windows[self.master.current_window].grid_remove()
        
        self.master.current_window = 3
        self.master.windows[self.master.current_window].grid(row=0, column=0, sticky='nsew')
    
    def configure_layout(self):
        self.grid_columnconfigure((0,2), weight=2)
        self.grid_columnconfigure(1, weight=0)
        self.grid_rowconfigure((0,9), weight=1)
    
    def clear_frame(self):
        pass