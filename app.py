from tkinter import *

app_root = None  # Initialize the variable to hold the root

def start_app():
    global app_root  # Declare the variable as global

    app_root = Tk()
    app_root.title("Chessor V1")
    app_root.iconbitmap(r"C:\Users\Massimo\PycharmProjects\chessor\chessor-icon.ico")
    app_root.geometry("650x400")

    app_root.mainloop()

if __name__ == "__main__":
    start_app()