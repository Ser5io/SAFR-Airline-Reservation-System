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
        # self.create_login()
    
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
        self.firstname = customtkinter.CTkEntry(self,
                                placeholder_text="First name",
                                bg_color=BGCOLOR)
        self.firstname.grid(row=2,
                column=1,
                sticky='ew',
                padx=20,
                pady=(15,0))
        
    def create_lastname_entry(self):
        self.lastname = customtkinter.CTkEntry(self,
                                        placeholder_text="Last name",
                                        bg_color=BGCOLOR)
        self.lastname.grid(row=3,
                column=1,
                sticky='ew',
                padx=20,
                pady=(15,0))
        
    def create_username_entry(self):
        self.username = customtkinter.CTkEntry(self,
                                        placeholder_text="Username",
                                        bg_color=BGCOLOR)
        self.username.grid(row=4,
                column=1,
                sticky='ew',
                padx=20,
                pady=(15,0))
        
    def create_password_entry(self):
        self.password = customtkinter.CTkEntry(self,
                                        placeholder_text="Password",
                                        show="*",
                                        bg_color=BGCOLOR)
        self.password.grid(row=5,
                column=1,
                sticky='ew',
                padx=20,
                pady=(15,0))

        self.confirm_password = customtkinter.CTkEntry(self,
                                        placeholder_text="Confirm password",
                                        show="*",
                                        bg_color=BGCOLOR)
        # self.confirm_password.grid(row=6,
        #                     column=1,
        #                     sticky='ew',
        #                     padx=20,
        #                     pady=(15,0))
        
    def create_signup(self):
        signupimage = ImageTk.PhotoImage(Image.open("images/add-contact_11710543.png").resize((20, 20), Image.Resampling.LANCZOS))
        self.signupbutton = customtkinter.CTkButton(self,
                                        text="Sign up",
                                        image=signupimage,
                                        font=("Poppins", FONT_MIN_SIZE, "bold"),
                                        bg_color=BGCOLOR,
                                        command=self.show_mainpagelogin_page)
        self.signupbutton.grid(row=6,
                        column=1,
                        sticky='ew',
                        padx=20,
                        pady=(15,0))
        
        self.errormsg = customtkinter.CTkLabel(self,
                                        text='',
                                        fg_color=BGCOLOR,
                                        text_color="red",
                                        font=("Poppins", FONT_MIN_SIZE, "bold"),
                                        justify="center")
        self.errormsg.grid(row=9,
                      column=1,
                      padx=(0,0),
                      pady=(0,0),
                      sticky='new')
        
    def create_login(self):
        alreadyhaveacc = customtkinter.CTkLabel(self,
                                    text="Already have an account?",
                                    font=("Poppins", FONT_MIN_SIZE),
                                    bg_color=BGCOLOR,
                                    state='disabled')
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
        
    def show_mainpagelogin_page(self, event=None):
        if self.firstname.get() == '' or self.lastname.get() == '' or self.username.get() == '' or self.password.get() == '':
            self.errormsg.configure(text='Please fill your informaions')
            return

        
        
        
        self.master.mainpage_login.username.configure(text=self.username.get())
        
        self.firstname.delete(0, 'end')
        self.lastname.delete(0, 'end')
        self.username.delete(0, 'end')
        self.password.delete(0, 'end')
        self.confirm_password.delete(0, 'end')
        self.errormsg.configure(text='')
        
        self.master.windows[self.master.current_window].grid_remove()
        
        self.master.current_window = self.master.MAIN_PAGE_LOGIN
        self.master.windows[self.master.current_window].grid(row=0, column=0, sticky='nsew')
        
    def show_login_page(self):
        self.master.windows[self.master.current_window].grid_remove()
        
        self.master.current_window = self.master.LOGIN_PAGE
        self.master.windows[self.master.current_window].grid(row=0, column=0, sticky='nsew')

    def configure_layout(self):
        self.grid_columnconfigure((0, 2), weight=2)
        self.grid_columnconfigure(1, weight=0)
        self.grid_rowconfigure((0, 9), weight=1)
    
    def clear_frame(self):
        pass