import customtkinter
from interface.window import Window
from PIL import ImageTk, Image

FONT_MAX_SIZE = 40
FONT_MIN_SIZE = 15

class FlightTypePage(Window):
    def __init__(self, master):
        super().__init__(master)
        
        self.draw_frame()
        
    def draw_frame(self):
        self.configure_layout()
        
        self.create_logo()
        self.create_choosetypelabel()
        self.create_oneway_button()
        self.create_roundway_button()
    
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
        
    def create_choosetypelabel(self):
        choosetype_label = customtkinter.CTkLabel(self,
                                        text="Which Flight Type Do You Want?",
                                        fg_color="white",
                                        text_color="black",
                                        font=("Poppins", FONT_MAX_SIZE, "bold"),
                                        justify="center")
        choosetype_label.grid(row=1,
                            column=0,
                            columnspan=3,
                            sticky="ew")
    
    def create_oneway_button(self):
        oneway_image = ImageTk.PhotoImage(Image.open("images/one-way.png").resize((70, 70), Image.Resampling.LANCZOS))
        oneway = customtkinter.CTkButton(self,
                                    text="One-way",
                                    image=oneway_image,
                                    fg_color="#0E0055",
                                    text_color="#ffffff",
                                    corner_radius=1000,
                                    font=("Poppins", FONT_MAX_SIZE, "bold"),
                                    hover_color="#0065B4",
                                    command=self.show_oneway_page)
        oneway.grid(row=2,
                    column=0,
                    columnspan=2,
                    sticky="nesw",
                    padx=(60,20),
                    pady=(0,30))
        
    def show_oneway_page(self):
        self.master.windows[self.master.current_window].grid_remove()
        
        self.master.current_window = self.master.ONEWAY_PAGE
        self.master.windows[self.master.current_window].grid(row=0, column=0, sticky='nsew')
    
    def create_roundway_button(self):
        roundway_image = ImageTk.PhotoImage(Image.open("images/round-trip.png").resize((70, 70), Image.Resampling.LANCZOS))
        roundway = customtkinter.CTkButton(self,
                                    text="Round-trip",
                                    image=roundway_image,
                                    fg_color="#0E0055",
                                    text_color="#ffffff",
                                    corner_radius=1000,
                                    font=("Poppins", FONT_MAX_SIZE-8, "bold"),
                                    hover_color="#0065B4",
                                    command=self.show_roundtrip_page)
        roundway.grid(row=2,
                    column=2,
                    sticky="nesw",
                    padx=(20,0),
                    pady=(0,30))
        
    def show_roundtrip_page(self):
        self.master.windows[self.master.current_window].grid_remove()
        
        self.master.current_window = self.master.ROUNDTRIP_PAGE
        self.master.windows[self.master.current_window].grid(row=0, column=0, sticky='nsew')
    
    def configure_layout(self):
        self.grid_columnconfigure((1,2), weight=2)
        self.grid_columnconfigure((0), weight=1)
        self.grid_columnconfigure((3), weight=1)
        self.grid_rowconfigure((1,2), weight=5)
    
    def clear_frame(self):
        pass