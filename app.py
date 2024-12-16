import customtkinter
from interface.invoice import Invoice
from interface.checkout import Checkout

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("theme/orange.json")

class App(customtkinter.CTk):
    def __init__(self, **kwargs):
        super().__init__()
        
        self.geometry("300x300")
        self.title("SOSKI")
        
        invoice = Invoice(master=self)
        checkout = Checkout(master=self)
        
        self.current_window = 1
        self.windows = [checkout, invoice]
        
        self.draw_window()
    
    def draw_window(self):
        selected_window = self.windows[self.current_window]
        selected_window.draw_frame()
        
    def create_back_button(self):
        pass
    
    def create_next_button(self):
        pass
    
app = App()
app.mainloop()