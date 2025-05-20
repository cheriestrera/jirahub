from pathlib import Path
import firebase_admin
from firebase_admin import credentials, firestore

BASE_DIR = Path(__file__).resolve().parent.parent
CRED_PATH = BASE_DIR / "backend" / "serviceAccountKey.json"

if not firebase_admin._apps:
    cred = credentials.Certificate(str(CRED_PATH))
    firebase_admin.initialize_app(cred)
db = firestore.client()

def get_employee_data(employee_id):
    """Fetch employee data from Firestore by ID."""
    try:
        doc_ref = db.collection("employees").document(employee_id)
        doc = doc_ref.get()
        if doc.exists:
            return doc.to_dict()
        else:
            return None
    except Exception as e:
        print(f"Failed to fetch employee data: {e}")
        return None

def delete_employee(employee_id):
    """Delete employee from Firestore by ID. Returns True if deleted, False otherwise."""
    try:
        doc_ref = db.collection("employees").document(employee_id)
        doc = doc_ref.get()
        if doc.exists:
            doc_ref.delete()
            return True
        else:
            return False
    except Exception as e:
        print(f"Failed to delete employee: {e}")
        return False