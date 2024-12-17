import tkinter
import customtkinter
from PIL import ImageTk, Image
from interface.window import Window

BGCOLOR = '#E8E8E8'
FONT_MAX_SIZE = 20
FONT_MIN_SIZE = 15

class Signup(Window):
    def __init__(self, master):
        super().__init__(master)
        self.draw_frame()
    
    def draw_frame(self):
        self.configure_layout()
        
        self.create_back_ground()
        self.create_frame()
        self.create_account()
        self.create_firstname_entry()
        self.create_lastname_entry()
        self.create_username_entry()
        self.create_password_entry()
        self.create_signup()
        self.create_login()
    
    def create_back_ground(self):
        self.bg_image = ImageTk.PhotoImage(Image.open("images/pattern.png"))
        bg_label = customtkinter.CTkLabel(master=self, image=self.bg_image, text="")
        bg_label.grid(row=0, column=0, rowspan=10, columnspan=3, sticky="nsew")
        
    def create_frame(self):
        frame = customtkinter.CTkFrame(self,
                                    bg_color=BGCOLOR)
        frame.grid(row=1,
                rowspan=8,
                column=1,
                sticky='nesw')
    
    def create_account(self):
        createacc = customtkinter.CTkLabel(self,
                            text="Create an Account!",
                            font=("Poppins", FONT_MAX_SIZE, "bold"),
                            bg_color=BGCOLOR)
        createacc.grid(row=1,
                column=1,
                sticky='ew',
                padx=20,
                pady=(15,0))
    
    def create_firstname_entry(self):
        firstname = customtkinter.CTkEntry(self,
                                placeholder_text="First name",
                                bg_color=BGCOLOR)
        firstname.grid(row=2,
                column=1,
                sticky='ew',
                padx=20,
                pady=(15,0))
        
    def create_lastname_entry(self):
        lastname = customtkinter.CTkEntry(self,
                                        placeholder_text="Last name",
                                        bg_color=BGCOLOR)
        lastname.grid(row=3,
                column=1,
                sticky='ew',
                padx=20,
                pady=(15,0))
        
    def create_username_entry(self):
        username = customtkinter.CTkEntry(self,
                                        placeholder_text="Username",
                                        bg_color=BGCOLOR)
        username.grid(row=4,
                column=1,
                sticky='ew',
                padx=20,
                pady=(15,0))
        
    def create_password_entry(self):
        password = customtkinter.CTkEntry(self,
                                        placeholder_text="Password",
                                        show="*",
                                        bg_color=BGCOLOR)
        password.grid(row=5,
                column=1,
                sticky='ew',
                padx=20,
                pady=(15,0))

        confirm_password = customtkinter.CTkEntry(self,
                                        placeholder_text="Confirm password",
                                        show="*",
                                        bg_color=BGCOLOR)
        confirm_password.grid(row=5,
                            column=1,
                            sticky='ew',
                            padx=20,
                            pady=(15,0))
        
    def create_signup(self):
        signupimage = ImageTk.PhotoImage(Image.open("images/add-contact_11710543.png").resize((20, 20), Image.Resampling.LANCZOS))
        signupbutton = customtkinter.CTkButton(self,
                                        text="Sign up",
                                        image=signupimage,
                                        font=("Poppins", FONT_MIN_SIZE, "bold"),
                                        bg_color=BGCOLOR,
                                        command=self.button_function)
        signupbutton.grid(row=6,
                        column=1,
                        sticky='ew',
                        padx=20,
                        pady=(15,0))
        
    def create_login(self):
        alreadyhaveacc = customtkinter.CTkLabel(self,
                                    text="Already have an account?",
                                    font=("Poppins", FONT_MIN_SIZE),
                                    bg_color=BGCOLOR)
        alreadyhaveacc.grid(row=7,
                        column=1,
                        sticky='w',
                        padx=20,
                        pady=(15,0))

        enterimage = ImageTk.PhotoImage(Image.open("images/enter.png").resize((20, 20), Image.Resampling.LANCZOS))
        loginbutton = customtkinter.CTkButton(self,
                                            text="login",
                                            image=enterimage,
                                            font=("Poppins", FONT_MIN_SIZE, "bold"),
                                            bg_color=BGCOLOR)
        loginbutton.grid(row=8,
                    column=1,
                    sticky='ew',
                    padx=20,
                    pady=(15,15))

        
    def button_function(self):
        self.destroy()
        main_page = customtkinter.CTk()
        main_page.geometry("850x500")
        main_page.title('SAFR')
        l1 = customtkinter.CTkLabel(master=main_page, text="Home Page", font=("Poppins", 50, "bold"))
        l1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    def configure_layout(self):
        self.grid_columnconfigure((0,2), weight=2)
        self.grid_columnconfigure(1, weight=0)
        self.grid_rowconfigure((0,9), weight=1)
    
    def clear_frame(self):
        pass