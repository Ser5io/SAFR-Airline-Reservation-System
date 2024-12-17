import customtkinter

from interface.main_page import MainPage
from interface.information import Information
from interface.location import Location
from interface.flight_type_page import FlightTypePage
from interface.login import Login
from interface.trips import One_Way
from interface.trips import Round_Trip
from interface.seats import Seats
from interface.ticket import Ticket
from interface.checkout import Checkout

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        self.geometry("1366x768")
        self.title('Welcome To SAFR')
        self.iconbitmap("images/Logo.ico")
        
        mainpage = MainPage(self)
        login = Login(self)
        information = Information(self)
        location = Location(self)
        flighttype = FlightTypePage(self)
        oneway = One_Way(self)
        # roundtrip = Round_Trip(self)
        seats = Seats(self)
        checkout = Checkout(self)
        ticket = Ticket(self)
        
        self.current_window = 0
        self.windows = [mainpage, information, location,
                        flighttype, oneway, seats, checkout, ticket]

        self.configure_layout()
        self.windows[self.current_window].grid(row=0, column=0, sticky='nsew')

    def configure_layout(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def show_next_frame(self):
        self.windows[self.current_window].grid_remove()
        
        self.current_window += 1
        self.windows[self.current_window].grid(row=0, column=0, sticky='nsew')
    
    def show_previous_frame(self):
        self.windows[self.current_window].grid_remove()
        
        self.current_window -= 1
        self.windows[self.current_window].grid(row=0, column=0, sticky='nsew')
    
    def show_home_frame(self):
        pass
        
app = App()
app.mainloop()