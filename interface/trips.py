import customtkinter
from PIL import Image
from interface.window import Window

FONT_MAX_SIZE = 40
FONT_MIN_SIZE = 15

class Round_Trip(Window):
    def __init__(self, master):
        super().__init__(master)
        
        self.draw_frame()
        
    def draw_frame(self):
        self.configure(fg_color="white")
        self.configure_layout()
        
        self.create_logo()
        self.create_choose_the_plan()
        self.create_tickets()
        
    def create_logo(self):
        logo_icon = customtkinter.CTkImage(light_image=Image.open("images/Logo.ico"),
                                                dark_image=Image.open("images/Logo.ico"))
        logo = customtkinter.CTkLabel(self,
                                    text="  SAFR",
                                    fg_color="white",
                                    text_color="black",
                                    image=logo_icon,
                                    compound="left",
                                    anchor="w",
                                    font=("Poppins", FONT_MIN_SIZE, "bold"))
        logo.grid(row=0,
                column=0,
                pady=(20,0),
                padx=(20,0),
                sticky="nesw")
    
    def create_choose_the_plan(self):
        choosetheplan = customtkinter.CTkLabel(self,
                                        text="Choose The Plan For Round-trip",
                                        fg_color="white",
                                        text_color="black",
                                        font=("Poppins", FONT_MAX_SIZE, "bold"),
                                        justify="center")
        choosetheplan.grid(row=1,
                            column=0,
                            columnspan=3,
                            sticky='ew',
                            padx=10,
                            pady=(20,40))
    
    def create_tickets(self):
        image_path1 = "images/ticket 5.png"
        economy_image = Image.open(image_path1).resize((2000, 2000))
        button_image1 = customtkinter.CTkImage(light_image=economy_image, dark_image=economy_image, size=(400, 148))
        
        economy_button = customtkinter.CTkButton(self,
                                        image=button_image1,  # Set the image
                                        text="",
                                        fg_color="white",
                                        text_color="#ffffff",
                                        hover_color="#d1dbe4",
                                        corner_radius=10,
                                        command=self.show_seats_as_economy_page)
        economy_button.grid(row=2,
                            column=0,
                            columnspan=2,
                            sticky='ew',
                            padx=10,
                            pady=10)

        
        
        image_path2 = "images/ticket 6.png"
        primimage = Image.open(image_path2).resize((2000, 2000))
        button_image2 = customtkinter.CTkImage(light_image=primimage, dark_image=primimage, size=(400, 148))

        prim_button = customtkinter.CTkButton(self,
                                        image=button_image2,  # Set the image
                                        text="",
                                        fg_color="white",
                                        text_color="#ffffff",
                                        hover_color="#d1dbe4",
                                        corner_radius=10,
                                        command=self.show_seats_as_prim_economy_page)
        prim_button.grid(row=2,
                        column=2,
                        sticky='ew',
                        padx=10,
                        pady=10)


        image_path3 = "images/ticket 7.png"
        business_image = Image.open(image_path3).resize((2000, 2000))
        button_image3 = customtkinter.CTkImage(light_image=business_image, dark_image=business_image, size=(400, 148))

        business_button = customtkinter.CTkButton(self,
                                        image=button_image3,  # Set the image
                                        text="",
                                        fg_color="white",
                                        text_color="#ffffff",
                                        hover_color="#d1dbe4",
                                        corner_radius=10,
                                        command=self.show_seats_as_business_page)
        business_button.grid(row=3,
                            column=0,
                            columnspan=2,
                            sticky='ew',
                            padx=10,
                            pady=10)
        
        image_path4 = "images/ticket 8.png"
        first_image = Image.open(image_path4).resize((2000, 2000))
        button_image4 = customtkinter.CTkImage(light_image=first_image, dark_image=first_image, size=(400, 148))

        first_button = customtkinter.CTkButton(self,
                                        image=button_image4,  # Set the image
                                        text="",
                                        fg_color="white",
                                        text_color="#ffffff",
                                        hover_color="#d1dbe4",
                                        corner_radius=10,
                                        command=self.show_seats_as_first_page)
        first_button.grid(row=3,
                        column=2,
                        sticky='ew',
                        padx=10,
                        pady=10)

    def show_seats_as_economy_page(self):
        self.master.ticket.class_left.configure(text='Economy')
        self.master.ticket.class_right.configure(text='Economy')
        
        self.master.windows[self.master.current_window].grid_remove()
        
        self.master.current_window = self.master.SEATS_PAGE
        self.master.windows[self.master.current_window].grid(row=0, column=0, sticky='nsew')
    
    def show_seats_as_prim_economy_page(self):
        self.master.ticket.class_left.configure(text='Premium')
        self.master.ticket.class_right.configure(text='Premium')
        
        self.master.windows[self.master.current_window].grid_remove()
        
        self.master.current_window = self.master.SEATS_PAGE
        self.master.windows[self.master.current_window].grid(row=0, column=0, sticky='nsew')
    
    def show_seats_as_business_page(self):
        self.master.ticket.class_left.configure(text='Business')
        self.master.ticket.class_right.configure(text='Business')
        
        self.master.windows[self.master.current_window].grid_remove()
        
        self.master.current_window = self.master.SEATS_PAGE
        self.master.windows[self.master.current_window].grid(row=0, column=0, sticky='nsew')
    
    def show_seats_as_first_page(self):
        self.master.ticket.class_left.configure(text='First')
        self.master.ticket.class_right.configure(text='First')
        
        self.master.windows[self.master.current_window].grid_remove()
        
        self.master.current_window = self.master.SEATS_PAGE
        self.master.windows[self.master.current_window].grid(row=0, column=0, sticky='nsew')
        
    
    def configure_layout(self):
        self.grid_columnconfigure((1, 2), weight=1)
        self.grid_columnconfigure(0, weight=0)
    
    def clear_frame(self):
        pass
    
    
class One_Way(Window):
    def __init__(self, master):
        super().__init__(master)
        
        self.draw_frame()
        
    def draw_frame(self):
        self.configure(fg_color="white")
        self.configure_layout()
        
        self.create_logo()
        self.create_choose_the_plan()
        self.create_tickets()
        
    def create_logo(self):
        logo_icon = customtkinter.CTkImage(light_image=Image.open("images/Logo.ico"),
                                                dark_image=Image.open("images/Logo.ico"))
        logo = customtkinter.CTkLabel(self,
                                    text="  SAFR",
                                    fg_color="white",
                                    text_color="black",
                                    image=logo_icon,
                                    compound="left",
                                    anchor="w",
                                    font=("Poppins", FONT_MIN_SIZE, "bold"))
        logo.grid(row=0,
                column=0,
                pady=(20,0),
                padx=(20,0),
                sticky="nesw")
    
    
    def create_choose_the_plan(self):
        choosetheplan = customtkinter.CTkLabel(self,
                                        text="Choose The Plan For One_Way",
                                        fg_color="white",
                                        text_color="black",
                                        font=("Poppins", FONT_MAX_SIZE, "bold"),
                                        justify="center")
        choosetheplan.grid(row=1,
                            column=0,
                            columnspan=3,
                            sticky='ew',
                            padx=10,
                            pady=(20,40))
    
    def create_tickets(self):
        image_path1 = "images/ticket 1.png"
        economy_image = Image.open(image_path1).resize((2000, 2000))
        button_image1 = customtkinter.CTkImage(light_image=economy_image, dark_image=economy_image, size=(400, 148))
        
        economy_button = customtkinter.CTkButton(self,
                                        image=button_image1,  # Set the image
                                        text="",
                                        fg_color="white",
                                        text_color="#ffffff",
                                        hover_color="#d1dbe4",
                                        corner_radius=10,
                                        command=self.show_seats_as_economy_page)
        economy_button.grid(row=2,
                            column=0,
                            columnspan=2,
                            sticky='ew',
                            padx=10,
                            pady=10)

        
        
        image_path2 = "images/ticket 2.png"
        primimage = Image.open(image_path2).resize((2000, 2000))
        button_image2 = customtkinter.CTkImage(light_image=primimage, dark_image=primimage, size=(400, 148))

        prim_button = customtkinter.CTkButton(self,
                                        image=button_image2,  # Set the image
                                        text="",
                                        fg_color="white",
                                        text_color="#ffffff",
                                        hover_color="#d1dbe4",
                                        corner_radius=10,
                                        command=self.show_seats_as_prim_economy_page)
        prim_button.grid(row=2,
                        column=2,
                        sticky='ew',
                        padx=10,
                        pady=10)


        image_path3 = "images/ticket 3.png"
        business_image = Image.open(image_path3).resize((2000, 2000))
        button_image3 = customtkinter.CTkImage(light_image=business_image, dark_image=business_image, size=(400, 148))

        business_button = customtkinter.CTkButton(self,
                                        image=button_image3,  # Set the image
                                        text="",
                                        fg_color="white",
                                        text_color="#ffffff",
                                        hover_color="#d1dbe4",
                                        corner_radius=10,
                                        command=self.show_seats_as_business_page)
        business_button.grid(row=3,
                            column=0,
                            columnspan=2,
                            sticky='ew',
                            padx=10,
                            pady=10)
        
        image_path4 = "images/ticket 4.png"
        first_image = Image.open(image_path4).resize((2000, 2000))
        button_image4 = customtkinter.CTkImage(light_image=first_image, dark_image=first_image, size=(400, 148))

        first_button = customtkinter.CTkButton(self,
                                        image=button_image4,  # Set the image
                                        text="",
                                        fg_color="white",
                                        text_color="#ffffff",
                                        hover_color="#d1dbe4",
                                        corner_radius=10,
                                        command=self.show_seats_as_first_page)
        first_button.grid(row=3,
                    column=2,
                    sticky='ew',
                    padx=10,
                    pady=10)

    def show_seats_as_economy_page(self):
        self.master.ticket.class_left.configure(text='Economy')
        self.master.ticket.class_right.configure(text='Economy')
        
        self.master.windows[self.master.current_window].grid_remove()
        
        self.master.current_window = self.master.SEATS_PAGE
        self.master.windows[self.master.current_window].grid(row=0, column=0, sticky='nsew')
    
    def show_seats_as_prim_economy_page(self):
        self.master.ticket.class_left.configure(text='Premium')
        self.master.ticket.class_right.configure(text='Premium')
        
        self.master.windows[self.master.current_window].grid_remove()
        
        self.master.current_window = self.master.SEATS_PAGE
        self.master.windows[self.master.current_window].grid(row=0, column=0, sticky='nsew')
    
    def show_seats_as_business_page(self):
        self.master.ticket.class_left.configure(text='Business')
        self.master.ticket.class_right.configure(text='Business')
        
        self.master.windows[self.master.current_window].grid_remove()
        
        self.master.current_window = self.master.SEATS_PAGE
        self.master.windows[self.master.current_window].grid(row=0, column=0, sticky='nsew')
    
    def show_seats_as_first_page(self):
        self.master.ticket.class_left.configure(text='First')
        self.master.ticket.class_right.configure(text='First')
        
        self.master.windows[self.master.current_window].grid_remove()
        
        self.master.current_window = self.master.SEATS_PAGE
        self.master.windows[self.master.current_window].grid(row=0, column=0, sticky='nsew')
    
    def configure_layout(self):
        self.grid_columnconfigure((1, 2), weight=1)
        self.grid_columnconfigure(0, weight=0)
    
    def clear_frame(self):
        pass