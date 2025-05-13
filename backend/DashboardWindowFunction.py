from tkinter import Tk, Label, Frame
from backend.MainWindowFunction import AuthService

class DashboardWindow:
    def __init__(self, user_id: str):
        self.window = Tk()
        self.window.geometry("1440x706")
        self.window.title("Employee Dashboard")
        
        # Header
        Label(self.window, text="EMPLOYEE DIRECTORY", font=("Inter Bold", 40)).pack(pady=50)
        
        # User info section
        user_frame = Frame(self.window)
        user_frame.pack()
        Label(user_frame, text=f"Logged in as User ID: {user_id[:8]}...").pack()
        
        # Add your employee directory components here
        
        self.window.mainloop()