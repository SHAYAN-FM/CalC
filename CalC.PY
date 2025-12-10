import customtkinter as ctk
from tkinter import messagebox


app = ctk.CTk()
app.title("CalC")
app.geometry("240x195")


frame = ctk.CTkFrame(app , corner_radius = 0)
frame.pack(fill = "both" , expand = True)


def changecolor(color):
     if color == "روشن":
          ctk.set_appearance_mode("Light")
     elif color == "تیره":
          ctk.set_appearance_mode("Dark")
     elif color == "سیستم":
          ctk.set_appearance_mode("System")
menu_color = ctk.CTkOptionMenu(frame , values = ["سیستم" , "روشن" , "تیره"] , command = changecolor , font = ("B nazanin" , 20))
menu_color.pack(pady = 5)


label = ctk.CTkLabel(frame , text = "عبارت ریاضی را وارد کنید" , font = ("B nazanin" , 20))
label.pack(pady = 2)

i = ctk.CTkEntry(frame)
i.pack(pady = 5)


def h():
    ie = i.get()
    e = eval(ie)
    messagebox.showinfo("mohasebe" , f"{e}")
btn = ctk.CTkButton(frame , text = "عبارت رو حل کن" , font = ("B nazanin" , 18) , command = h)
btn.pack(pady = 1)

def out():
     app.quit()
out = ctk.CTkButton(frame , text = "خروج" , font = ("B nazanin" , 20) , command = out)
out.pack(pady = 5)

app.mainloop()
