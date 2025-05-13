from tkinter import Tk, messagebox

def handle_forgot_password(self):
    email = self.email_entry.get()
    if not email:
        messagebox.showwarning("Input Error", "Please enter your email")
        return
        
    self.auth_service.reset_password(email)
    
def show_dashboard(self, user):
    # Create a new window for the dashboard
    dashboard = Tk()
    dashboard.geometry("1440x800")
    # Here you would load the dashboard UI
    # You can use the SceneManager to handle different views
    dashboard.mainloop()
