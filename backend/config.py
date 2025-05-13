import firebase_admin
from firebase_admin import credentials, auth, db

class FirebaseConfig:
    def __init__(self):
        # Initialize Firebase
        cred = credentials.Certificate("C:/Users/Marites/Downloads/1 MainWindow-20250511T145919Z-1-001/1 MainWindow/backend/serviceAccountKey.json")
        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://jirah-employee-directory.firebaseio.com/'
        })
        
        # Database references
        self.users_ref = db.reference('/users')
        self.employees_ref = db.reference('/employees')
    
    def get_auth(self):
        return auth
    
    def get_db(self):
        return db