import tkinter
import customtkinter
from PIL import ImageTk, Image

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue")

def button_function():
    sign.destroy()
    main_page = customtkinter.CTk()
    main_page.geometry("850x500")
    main_page.title('SAFR')
    l1 = customtkinter.CTkLabel(master=main_page, text="Home Page", font=("Poppins", 50, "bold"))
    l1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    main_page.mainloop()

sign = customtkinter.CTk()
sign.geometry("850x600")
sign.title('SAFR Sign up Page')
sign.iconbitmap("../images/Logo.ico")
sign.resizable(False, False)


img0 = ImageTk.PhotoImage(Image.open("../images/pattern.png"))
l1 = customtkinter.CTkLabel(master=sign, image=img0)
l1.pack()

frame = customtkinter.CTkFrame(master=l1,
                               width=320,
                               height=450)
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

l2 = customtkinter.CTkLabel(master=frame,
                            text="Create an Account!",
                            font=("Poppins", 24, "bold"))
l2.place(x=50, y=35)

entry1 = customtkinter.CTkEntry(master=frame,
                                placeholder_text="First name",
                                width=220)
entry1.place(x=50, y=90)

entry2 = customtkinter.CTkEntry(master=frame,
                                placeholder_text="Last name",
                                width=220)
entry2.place(x=50, y=135)

entry3 = customtkinter.CTkEntry(master=frame,
                                placeholder_text="Username",
                                width=220)
entry3.place(x=50, y=180)

entry4 = customtkinter.CTkEntry(master=frame,
                                placeholder_text="Password",
                                width=220,
                                show="*")
entry4.place(x=50, y=225)

entry5 = customtkinter.CTkEntry(master=frame,
                                placeholder_text="Confirm password",
                                width=220,
                                show="*")
entry5.place(x=50, y=270)

img1 = ImageTk.PhotoImage(Image.open("../images/add-contact_11710543.png").resize((20, 20), Image.Resampling.LANCZOS))
button1 = customtkinter.CTkButton(master=frame,
                                  text="Sign up",
                                  width=220,
                                  image=img1,
                                  corner_radius=5,
                                  font=("Poppins", 12, "bold"),
                                  command=button_function)
button1.place(x=50, y=315)

l4 = customtkinter.CTkLabel(master=frame,
                            text="Already have an account?",
                            font=("Poppins", 11.5))
l4.place(x=50, y=355)

img4 = ImageTk.PhotoImage(Image.open("../images/enter.png").resize((20, 20), Image.Resampling.LANCZOS))
button1 = customtkinter.CTkButton(master=frame,
                                  text="login",
                                  width=220,
                                  image=img4,
                                  corner_radius=5,
                                  font=("Poppins", 12, "bold"))
button1.place(x=50, y=380)

sign.mainloop()