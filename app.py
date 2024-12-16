import customtkinter
from interface.main_page import MainPage
from interface.data_page import Data_page
from interface.location_from import Location_From
from interface.location_to import Location_To
from interface.flight_type_page import Flight_Type_Page
from interface.login import Login
from interface.trips import One_Way
from interface.trips import Round_Trip
from interface.seats import Seats
from interface.final_ticket import Final_Ticket



class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        self.mainpage = MainPage(self)
        self.datapage = Data_page(self)
        self.locationfrom = Location_From(self)
        self.locationto = Location_To(self)
        self.flighttype = Flight_Type_Page(self)
        self.login = Login(self)
        self.oneway = One_Way(self)
        self.roundtrip = Round_Trip(self)
        self.seats = Seats(self)
        # self.finalticket = Final_Ticket(self, self.Uname, self.Ulocationfrom, self.Ulocationto, 'First', 'D5')
        
        self.Uname = 'ggggggg'
        self.Ulocationfrom = ''
        self.Ulocationto = ''
        self.Uflighttype = ''
        self.Useat = ''
        
        self.roundtrip.grid(row=0, column=0, sticky='nesw')
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
    
    def start_booking(self):
        self.mainpage.grid_remove()
        self.datapage.grid(row=0, column=0, sticky='nesw')
        
    def go_to_locationFrom(self):
        
        self.datapage.grid_remove()
        self.locationfrom.grid(row=0, column=0, sticky='nesw')
    
    def go_to_locationto(self):
        print(self.Ulocationfrom)
        
        self.locationfrom.grid_remove()
        self.locationto.grid(row=0, column=0, sticky='nesw')
    
    def go_to_flighttype(self):
        self.locationto.grid_remove()
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