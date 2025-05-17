import tkinter as tk
from pathlib import Path
from tkinter import Frame, Tk, ttk, messagebox
import firebase_admin
from firebase_admin import auth, credentials
from firebase_admin import exceptions as firebase_exceptions

class ResetPassword(Frame):
    def __init__(self, master, scene_manager):
        super().__init__(master)
        self.scene_manager = scene_manager
        self.master.title("Password Reset System")
        self.master.geometry("1440x706")
        
        # Initialize Firebase (make sure to replace with your config)
        try:
            cred = credentials.Certificate("serviceAccountKey.json")  # Your Firebase admin SDK JSON file
            firebase_admin.initialize_app(cred)
        except Exception as e:
            messagebox.showerror("Firebase Error", f"Failed to initialize Firebase: {str(e)}")
            self.root.destroy()
            return
    
    def send_reset_email(self):
        email = self.email_entry.get().strip()
        
        if not email:
            messagebox.showerror("Error", "Please enter your email address")
            return
        
        try:
            # Send password reset email
            auth.generate_password_reset_link(email)
            
            self.status_label.config(
                text=f"Password reset link sent to {email}\nPlease check your inbox (and spam folder).",
                fg="green"
            )
            self.reset_btn.config(state=tk.DISABLED)
            
        except firebase_exceptions.FirebaseError as e:
            error_message = self.get_friendly_error(e)
            messagebox.showerror("Error", error_message)
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")
    
    def get_friendly_error(self, error):
        """Convert Firebase errors to user-friendly messages"""
        if isinstance(error, firebase_exceptions.NotFoundError):
            return "No user found with this email address."
        elif isinstance(error, firebase_exceptions.InvalidArgumentError):
            return "Please enter a valid email address."
        elif isinstance(error, firebase_exceptions.UnauthenticatedError):
            return "Authentication failed. Please try again later."
        else:
            return f"Failed to send reset email: {str(error)}"
    
    def back_to_login(self):
        # This would typically close the reset window and reopen the login window
        # In a real app, you might have a controller managing different views
        messagebox.showinfo("Info", "Returning to login screen")
        self.scene_manager.show_scene("login")
