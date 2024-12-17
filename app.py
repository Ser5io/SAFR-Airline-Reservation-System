import customtkinter

from interface.main_page import MainPage
from interface.information import Information
from interface.location import Location
from interface.flight_type_page import Flight_Type_Page
from interface.login import Login
from interface.trips import One_Way
from interface.trips import Round_Trip
from interface.seats import Seats
from interface.ticket import Final_Ticket

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        self.geometry("1920x1080")
        self.title('Welcome To SAFR')
        self.iconbitmap("images/Logo.ico")
        self.configure(fg_color="white")
        
        self.mainpage = MainPage(self) # DONE
        self.information = Information(self)
        self.location = Location(self)
        self.flighttype = Flight_Type_Page(self)
        self.login = Login(self)
        self.oneway = One_Way(self)
        self.roundtrip = Round_Trip(self)
        self.seats = Seats(self)
        self.finalticket = Final_Ticket(self)
        
        self.Uname = 'ggggggg'
        # self.finalticket = Final_Ticket(self, self.Uname, self.Ulocationfrom, self.Ulocationto, 'First', 'D5')
        
        
        self.Ulocationfrom = ''
        self.Ulocationto = ''
        self.Uflighttype = ''
        self.Useat = ''
        
        self.login.grid(row=0, column=0, sticky='nesw')
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
    
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