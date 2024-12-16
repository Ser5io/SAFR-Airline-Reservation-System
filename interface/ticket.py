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