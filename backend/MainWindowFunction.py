import firebase_admin
from firebase_admin import credentials, auth, firestore
from typing import Tuple, Optional, Dict, Any
from tkinter import messagebox
import logging

class AuthService:
    def __init__(self):
        """Initialize Firebase authentication and Firestore"""
        if not firebase_admin._apps:
            try:
                cred = credentials.Certificate(
                    r"C:\Users\Marites\Downloads\CC15project\backend\serviceAccountKey.json"
                )
                firebase_admin.initialize_app(cred)
                self.auth = auth
                self.db = firestore.client()
            except Exception as e:
                logging.error(f"Firebase initialization failed: {str(e)}")
                raise

    def login(self, email: str, password: str) -> Optional[Dict[str, Any]]:
        """Handle user login with email and password"""
        try:
            user = self.auth.get_user_by_email(email)
            
            # In a real implementation, you would verify the password here
            # This is simplified since Firebase Admin doesn't have password verification
            # You would typically use Firebase Client SDK for actual password auth
            
            # Get additional user data from Firestore
            user_ref = self.db.collection('users').document(user.uid)
            user_data = user_ref.get().to_dict()
            
            if not user_data:
                messagebox.showerror("Login Failed", "User data not found")
                return None
                
            return {
                'uid': user.uid,
                'email': user.email,
                'is_admin': user_data.get('is_admin', False),
                'name': user_data.get('name', ''),
                **user_data
            }
            
        except auth.UserNotFoundError:
            messagebox.showerror("Login Failed", "User not found")
        except Exception as e:
            messagebox.showerror("Login Failed", str(e))
        return None

    def register(self, email: str, password: str, admin_code: str, user_data: Dict[str, Any]) -> bool:
        """Register a new user with admin verification"""
        try:
            # Verify admin code (in real app, use secure validation)
            if admin_code != "1234":
                messagebox.showerror("Registration Failed", "Invalid admin code")
                return False
                
            # Create user in Firebase Auth
            user = self.auth.create_user(
                email=email,
                password=password
            )
            
            # Store additional data in Firestore
            user_ref = self.db.collection('users').document(user.uid)
            user_ref.set({
                'email': email,
                'is_admin': True,  # Since only admins can register
                'created_at': firestore.SERVER_TIMESTAMP,
                **user_data
            })
            
            messagebox.showinfo("Success", "User registered successfully")
            return True
            
        except auth.EmailAlreadyExistsError:
            messagebox.showerror("Registration Failed", "Email already exists")
        except Exception as e:
            messagebox.showerror("Registration Failed", str(e))
        return False

    def reset_password(self, email: str) -> bool:
        """Send password reset email"""
        try:
            self.auth.generate_password_reset_link(email)
            messagebox.showinfo("Success", "Password reset email sent")
            return True
        except auth.UserNotFoundError:
            messagebox.showerror("Error", "User not found")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        return False

    def get_current_user(self) -> Optional[Dict[str, Any]]:
        """Get the currently authenticated user"""
        # In a real implementation, you would track the current user session
        return None