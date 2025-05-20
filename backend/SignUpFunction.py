from pathlib import Path
from tkinter import messagebox
import requests
import firebase_admin
from firebase_admin import credentials, firestore, auth
from typing import Dict, Any

BASE_DIR = Path(__file__).resolve().parent.parent
CRED_PATH = BASE_DIR / "backend" / "serviceAccountKey.json"

if not firebase_admin._apps:
    cred = credentials.Certificate(str(CRED_PATH))
    firebase_admin.initialize_app(cred)

    api_key = "AIzaSyDgOE9QEdwf0KAAJk1d0Zx4SvHzbK_rTzk"

    def register_admin(name, email, password, admin_code):
        # Optionally check admin_code here
        url = f"https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={api_key}"
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
                    firestore.client().collection('users').document(local_id).set({
                        'name': name,
                        'email': email,
                        'is_admin': True,
                        'created_at': firestore.SERVER_TIMESTAMP
                    })
                return True, "Registration successful!"
            except Exception as e:
                print("Firestore write error:", e)
                return False, f"User created but failed to save extra info: {e}"
        else:
            error_message = data.get("error", {}).get("message", "Unknown error")
            return False, error_message