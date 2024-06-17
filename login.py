from tkinter import *
from tkinter import ttk
import app
from PIL import ImageTk, Image
lcs_f = r"C:\Users\Massimo\PycharmProjects\chessor\lcsf.txt"

with open(lcs_f, "r") as f:
    f_r = f.read()

def close():
    root.after(2000,root.destroy())
def launch_app():
    app.start_app()

def Login():
    user_input = feet_entry.get().strip()
    lcs_row_split = f_r.strip().split("\n")

    if user_input in lcs_row_split:
        for widget in mainframe.winfo_children():

            if int(widget.grid_info()["row"]) == 3 and int(widget.grid_info()["column"]) == 2:
                widget.grid_forget()
        grr_log = ttk.Label(mainframe, text="Logged in!",foreground= "#67F070" )
        grr_log.grid(row=3, column=2)
        root.after(2000, close)
        root.after(3000,app.start_app())
    else:
        err_log = ttk.Label(mainframe, text="Wrong License", foreground="red")
        err_log.grid(row=3, column=2)
root = Tk()
root.title("Chessor V1")
root.iconbitmap(r"C:\Users\Massimo\PycharmProjects\chessor\chessor-icon.ico")
image = Image.open(r"C:\Users\Massimo\PycharmProjects\chessor\chessor-bckr.jpg")
bckrph = ImageTk.PhotoImage(image)


root.bckrlb= Label(root, image = bckrph)
root.bckrlb.place(x=0, y=0, relwidth=1, relheight=1)


mainframe = ttk.Frame(root, padding="10 10 12 12" )
mainframe.grid(column=0, row=0, sticky=(N))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

feet_entry = ttk.Entry(mainframe, width=30)
feet_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe).grid(column=2, row=2, sticky = (W, E))

ttk.Button(mainframe, text="Login", command=Login).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="Insert your license").grid(column=1, row=1, sticky=W)



for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

feet_entry.focus()

root.mainloop()