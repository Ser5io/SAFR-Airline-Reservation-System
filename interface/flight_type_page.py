import customtkinter
from interface.window import Window
from PIL import ImageTk, Image

class FlightTypePage(Window):
    def __init__(self, master):
        super().__init__(master)
        
        self.draw_frame()
        
    def draw_frame(self):
        self.configure_layout()
        
        self.create_choosetypelabel()
        self.create_oneway_button()
        self.create_roundway_button()
    
    def create_choosetypelabel(self):
        choosetype_label = customtkinter.CTkLabel(self,
                                        text="Which Flight Type Do You Want?",
                                        fg_color="white",
                                        text_color="black",
                                        font=("Poppins", 70, "bold"),
                                        justify="center")
        choosetype_label.grid(row=0,
                              column=0,
                              sticky="ew",
                              columnspan=2)
    
    def create_oneway_button(self):
        oneway_image = ImageTk.PhotoImage(Image.open("images/one-way.png").resize((70, 70), Image.Resampling.LANCZOS))
        oneway = customtkinter.CTkButton(self,
                                    text="One-way",
                                    image=oneway_image,
                                    fg_color="#0E0055",
                                    text_color="#ffffff",
                                    width=425,
                                    height=300,
                                    corner_radius=60,
                                    font=("Poppins", 30, "bold"),
                                    hover_color="#0065B4",
                                    command=self.master.show_next_frame)
        oneway.grid(row=1,
                    column=0,
                    sticky="ew")
    
    def create_roundway_button(self):
        roundway_image = ImageTk.PhotoImage(Image.open("images/round-trip.png").resize((70, 70), Image.Resampling.LANCZOS))
        roundway = customtkinter.CTkButton(self,
                                    text="Round-trip",
                                    image=roundway_image,
                                    fg_color="#0E0055",
                                    text_color="#ffffff",
                                    width=425,
                                    height=300,
                                    corner_radius=60,
                                    font=("Poppins", 30, "bold"),
                                    hover_color="#0065B4",
                                    command=self.master.show_next_frame)
        roundway.grid(row=1,
                      column=1,
                      sticky="ew")
    
    def configure_layout(self):
        pass
    
    def clear_frame(self):
        pass
