import firebase_admin
import requests
from firebase_admin import credentials, auth, firestore
from typing import Optional, Dict, Any
from pathlib import Path
import logging

BASE_DIR = Path(__file__).resolve().parent.parent
CRED_PATH = BASE_DIR / "backend" / "serviceAccountKey.json"

class AuthService:
    def __init__(self):
        if not firebase_admin._apps:
            try:
                cred = credentials.Certificate(str(CRED_PATH))
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

    def reset_password(self, email):
        url = f"https://identitytoolkit.googleapis.com/v1/accounts:sendOobCode?key={self.api_key}"
        payload = {
            "requestType": "PASSWORD_RESET",
            "email": email
        }
        response = requests.post(url, json=payload)
        data = response.json()
        return "email" in data  