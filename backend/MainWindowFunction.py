import firebase_admin
import requests
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
            except Exception as e:
                logging.error(f"Firebase initialization failed: {str(e)}")
                raise
        
        self.auth = auth
        self.db = firestore.client()
        self.api_key = "AIzaSyDgOE9QEdwf0KAAJk1d0Zx4SvHzbK_rTzk"  # <-- Replace with your actual API key

    def login(self, email: str, password: str) -> Optional[Dict[str, Any]]:
        url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={self.api_key}"
        payload = {
            "email": email,
            "password": password,
            "returnSecureToken": True
        }
        response = requests.post(url, json=payload)
        data = response.json()
        if "idToken" in data:
            return data  # Successful login, returns user info
        else:
            return None  # Login failed

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

    def reset_password(self, email):
        url = f"https://identitytoolkit.googleapis.com/v1/accounts:sendOobCode?key={self.api_key}"
        payload = {
            "requestType": "PASSWORD_RESET",
            "email": email
        }
        response = requests.post(url, json=payload)
        data = response.json()
        return "email" in data  # Returns True if email sent, False otherwise

    def get_current_user(self) -> Optional[Dict[str, Any]]:
        """Get the currently authenticated user"""
        # In a real implementation, you would track the current user session
        return None
    
    def register_admin(self, name, email, password, admin_code):
        # Optionally check admin_code here
        url = f"https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={self.api_key}"
        payload = {
            "email": email,
            "password": password,
            "returnSecureToken": True
        }
        response = requests.post(url, json=payload)
        data = response.json()
        if "idToken" in data:
            # Save 'name' and other info to Firestore
            try:
                # Get the user's UID from the response
                local_id = data.get("localId")
                if local_id:
                    self.db.collection('users').document(local_id).set({
                        'name': name,
                        'email': email,
                        'is_admin': True,
                        'created_at': firestore.SERVER_TIMESTAMP
                    })
                return True, "Registration successful!"
            except Exception as e:
                return False, f"User created but failed to save extra info: {e}"
        else:
            error_message = data.get("error", {}).get("message", "Unknown error")
            return False, error_message