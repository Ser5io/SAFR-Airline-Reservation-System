import customtkinter

from interface.main_page import MainPage
from interface.main_page_login import MainPageLogin
from interface.information import Information
from interface.location import Location
from interface.flight_type_page import FlightTypePage
from interface.login import Login
from interface.sign_up import Signup
from interface.trips import One_Way
from interface.trips import Round_Trip
from interface.seats import Seats
from interface.ticket import Ticket
from interface.checkout import Checkout
from interface.invoice import Invoice

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        self.geometry("1000x600")
        self.title('SAFR — Airline Reservation System')
        self.iconbitmap("images/Logo.ico")
        self.resizable(0, 0)
        
        self.mainpage = MainPage(self) #DONE
        self.mainpage_login = MainPageLogin(self) #DONE
        self.login = Login(self) #DONE
        self.signup = Signup(self) #DONE
        self.information = Information(self) #DONE
        self.location = Location(self) #DONE
        self.flight_type = FlightTypePage(self) #DONE
        self.oneway = One_Way(self) #DONE
        self.roundtrip = Round_Trip(self) #DONE
        self.seats = Seats(self) #DONE
        self.checkout = Checkout(self)
        self.invoice = Invoice(self)
        self.ticket = Ticket(self) #DONE
        
        self.current_window = 0
        self.windows = [self.mainpage, self.mainpage_login, self.information, self.location, self.flight_type,
                        self.oneway, self.roundtrip, self.seats, self.checkout, self.invoice,
                        self.ticket, self.login, self.signup]
        
        self.MAIN_PAGE = self.windows.index(self.mainpage)
        self.MAIN_PAGE_LOGIN = self.windows.index(self.mainpage_login)
        self.INFORMATION_PAGE = self.windows.index(self.information)
        self.LOCATION_PAGE = self.windows.index(self.location)
        self.FLIGHT_TYPE_PAGE = self.windows.index(self.flight_type)
        self.ONEWAY_PAGE = self.windows.index(self.oneway)
        self.ROUNDTRIP_PAGE = self.windows.index(self.roundtrip)
        self.SEATS_PAGE = self.windows.index(self.seats)
        self.CHECKOUT_PAGE = self.windows.index(self.checkout)
        self.INVOICE_PAGE = self.windows.index(self.invoice)
        self.TICKET_PAGE = self.windows.index(self.ticket)
        self.LOGIN_PAGE = self.windows.index(self.login)
        self.SIGNUP_PAGE = self.windows.index(self.signup)
        
        
        self.configure_layout()
        self.windows[self.current_window].grid(row=0, column=0, sticky='nsew')

    def configure_layout(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
    
    def show_home_frame(self):
        pass
        
app = App()
app.mainloop()