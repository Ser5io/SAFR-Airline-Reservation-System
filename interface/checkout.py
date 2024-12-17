import customtkinter
from interface.window import Window

class Checkout(Window):
    def __init__(self, master):
        super().__init__(master)
        self.draw_frame()
    
    def draw_frame(self):
        self.configure_layout()
        
        payment_info = Payment_Info(master=self.master)
        payment_info.grid(row=0,
                          column=0,
                          padx=(10, 0),
                          pady=10,
                          sticky="nsew")
        payment_info.draw_frame()
        
        shopping_cart_info = Shopping_Cart_Info(master=self.master)
        shopping_cart_info.grid(row=0,
                                column=1,
                                padx=10,
                                pady=10,
                                sticky="nsew")
        
    def configure_layout(self):
        self.master.grid_columnconfigure((0, 1), weight=1)
        self.master.grid_rowconfigure(0, weight=1)
    
    def clear_frame(self):
        pass
    
class Payment_Info(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
    
    def configure_layout(self):
        # self.grid_rowconfigure((0, 1, 2, 3), weight=1)
        self.grid_columnconfigure((0, 1, 2), weight=1)
    
    def draw_frame(self):
        self.configure_layout()
        
        self.create_first_name(0, 0)
        self.create_last_name(0, 1)
        self.create_email(0, 2)
        self.create_address(1, 0)
        self.create_country_menu(2, 0)
        self.create_phone_number(2, 1)
        self.create_confirm_button(3, 2)
     
    def create_first_name(self, row, column):
        first_name_box = customtkinter.CTkEntry(master=self,
                                                placeholder_text="First name")
        first_name_box.grid(row=row,
                            column=column,
                            padx=(10, 0),
                            pady=10,
                            sticky="ew")
    
    def create_last_name(self, row, column):
        last_name_box = customtkinter.CTkEntry(master=self,
                                               placeholder_text="Last name")
        last_name_box.grid(row=row,
                           column=column,
                           padx=(10, 0),
                           pady=10,
                           sticky="ew")
    
    def create_email(self, row, column):
        email_box = customtkinter.CTkEntry(master=self,
                                           placeholder_text="Email")
        email_box.grid(row=row,
                       column=column,
                       padx=10,
                       pady=10,
                       sticky="ew")
        
    def create_address(self, row, column):
        address_box = customtkinter.CTkEntry(master=self,
                                             placeholder_text="Address")
        address_box.grid(row=row,
                         column=column,
                         sticky="ew",
                         padx=10,
                         pady=10,
                         columnspan=3)
    
    def create_country_menu(self, row, column):
        country_menu_var = customtkinter.StringVar(value="Select...")
        country_menu = customtkinter.CTkOptionMenu(master=self,
                                                   values=["Egypt", "Deez Nuts"],
                                                   variable=country_menu_var)
        country_menu.grid(row=row,
                          column=column,
                          padx=(10, 0),
                          pady=10,
                          sticky="ew")
    
    def create_phone_number(self, row, column):
        phone_number_box = customtkinter.CTkEntry(master=self,
                                                placeholder_text="Phone number")
        phone_number_box.grid(row=row,
                              column=column,
                              sticky="ew",
                              padx=10,
                              pady=10,
                              columnspan=2)
    
    def create_confirm_button(self, row, column):
        confirm_button = customtkinter.CTkButton(master=self,
                                                 text="Confirm..")
        confirm_button.grid(row=row,
                            column=column,
                            sticky="ew",
                            padx=10,
                            pady=10)
    
    def clear_frame(self):
        pass
    
class Shopping_Cart_Info(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
    
    def draw_frame(self):
        pass
    
    def configure_layout(self):
       self.grid_rowconfigure((0, 1, 2, 3), weight=1)
       self.grid_columnconfigure((0, 1), weight=1)
    
    def clear_frame(self):
        pass