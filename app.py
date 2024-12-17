import customtkinter

# from interface.invoice import Invoice
# from interface.checkout import Checkout

# customtkinter.set_appearance_mode("dark")
# customtkinter.set_default_color_theme("theme/orange.json")
# class App(customtkinter.CTk):
#     def __init__(self, **kwargs):
#         super().__init__()
        
#         self.geometry("300x300")
#         self.title("SOSKI")
        
#         invoice = Invoice(master=self)
#         checkout = Checkout(master=self)
        
#         self.current_window = 1
#         self.windows = [checkout, invoice]
        
#         self.draw_window()
    
#     def draw_window(self):
#         selected_window = self.windows[self.current_window]
#         selected_window.draw_frame()
        
#     def create_back_button(self):
#         pass
    
#     def create_next_button(self):
#         pass

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
        
        self.mainpage = MainPage(self)
        self.information = Information(self)
        self.location = Location(self)
        self.flighttype = FlightTypePage(self)
        self.login = Login(self)
        self.oneway = One_Way(self)
        self.roundtrip = Round_Trip(self)
        self.seats = Seats(self)
        # self.checkout = Checkout(self)
        self.ticket = Ticket(self)
        
        self.flighttype.grid(row=0, column=0, sticky='nesw')
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def show_next_frame(self):
        pass
    
    def show_previous_frame(self):
        pass
    
    def show_home_frame(self):
        pass
    
    def start_booking(self):
        self.mainpage.grid_remove()
        self.information.grid(row=0, column=0, sticky='nesw')
        
    def go_to_location(self):
        self.information.grid_remove()
        self.location.grid(row=0, column=0, sticky='nesw')
    
    def go_to_flighttype(self):
        self.location.grid_remove()
        self.flighttype.grid(row=0, column=0, sticky='nesw')
    
    def go_to_oneway(self):
        self.flighttype.grid_remove()
        self.oneway.grid(row=0, column=0, sticky='nesw')
    
    def go_to_roundtrip(self):
        self.flighttype.grid_remove()
        self.roundtrip.grid(row=0, column=0, sticky='nesw')
        
    def go_to_seats(self):
        self.oneway.grid_remove()
        self.roundtrip.grid_remove()
        self.seats.grid(row=0, column=0, sticky='nesw')
        
    def go_to_finalticket(self):
        self.seats.grid_remove()
        self.finalticket.grid(row=0, column=0, sticky='nesw')
        
app = App()
app.mainloop()