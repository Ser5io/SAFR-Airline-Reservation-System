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
from interface.flight_type_page import Flight_Type_Page
from interface.login import Login
from interface.one_way_plan import One_Way
from interface.round_trip_plan import Round_Trip
from interface.seats import Seats
# from interface.ticket import Final_Ticket

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
        self.Uname = 'ggggggg'
        # self.finalticket = Final_Ticket(self, self.Uname, self.Ulocationfrom, self.Ulocationto, 'First', 'D5')
        
        
        self.Ulocationfrom = ''
        self.Ulocationto = ''
        self.Uflighttype = ''
        self.Useat = ''
        
        self.location.grid(row=0, column=0, sticky='nesw')
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