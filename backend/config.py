from pathlib import Path
import firebase_admin
from firebase_admin import credentials, auth, db

BASE_DIR = Path(__file__).resolve().parent.parent
CRED_PATH = BASE_DIR / "backend" / "serviceAccountKey.json"

class FirebaseConfig:
    def __init__(self):
        cred = credentials.Certificate(str(CRED_PATH))
        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://jirah-employee-directory.firebaseio.com/'
        })
        
        self.users_ref = db.reference('/users')
        self.employees_ref = db.reference('/employees')
    
    def get_auth(self):
        return auth
    
    def get_db(self):
        return db