import customtkinter
from interface.window import Window
from interface.ticket import Ticket

class Invoice(Window):
    def __init__(self, master):
        super().__init__(master)
        self.draw_frame()
    
    def draw_frame(self):
        label = customtkinter.CTkLabel(self.master,
                                       text="Thank you for flying with deez nuts.",
                                       fg_color="transparent")
        # label.pack(pady=20)
        
        tickets_menu_var = customtkinter.StringVar(value="Yousef's Ticket")
        tickets_menu = customtkinter.CTkOptionMenu(self.master, values=["Yousef's Ticket", "Kareem's Ticket"],
                                                   variable=tickets_menu_var)
        # tickets_menu.pack(pady=20)
        
        open_button = customtkinter.CTkButton(self.master, text="Open", command=self.open_event)
        # open_button.pack(pady=10, padx=10)
        
        save_button = customtkinter.CTkButton(self.master, text="Save")
        # save_button.pack(pady=0, padx=60)
        
    def open_event(self):
        ticket = Ticket(self.master)
        # ticket.focus()
    
    def configure_layout(self):
        pass
    
    def clear_frame(self):
        pass