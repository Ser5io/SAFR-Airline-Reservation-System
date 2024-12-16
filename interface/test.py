import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Frame Switcher")
        self.geometry("400x300")

        # Create frames
        self.frame1 = Frame1(self)
        self.frame2 = Frame2(self)

        # Show the first frame
        self.frame1.grid(row=0, column=0, sticky="nsew")

    def switch_to_frame2(self):
        self.frame1.grid_remove()
        self.frame2.grid(row=0, column=0, sticky="nsew")

    def switch_to_frame1(self):
        self.frame2.grid_remove()
        self.frame1.grid(row=0, column=0, sticky="nsew")

class Frame1(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.label = ctk.CTkLabel(self, text="This is Frame 1")
        self.label.pack(pady=20)
        self.button = ctk.CTkButton(self, text="Go to Frame 2", command=master.switch_to_frame2)
        self.button.pack(pady=10)

class Frame2(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.label = ctk.CTkLabel(self, text="This is Frame 2")
        self.label.pack(pady=20)
        self.button = ctk.CTkButton(self, text="Go to Frame 1", command=master.switch_to_frame1)
        self.button.pack(pady=10)

if __name__ == "__main__":
    app = App()
    app.mainloop()
