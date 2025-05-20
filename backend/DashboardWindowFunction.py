from pathlib import Path
import firebase_admin
from firebase_admin import credentials, firestore

BASE_DIR = Path(__file__).resolve().parent.parent
CRED_PATH = BASE_DIR / "backend" / "serviceAccountKey.json"

if not firebase_admin._apps:
    cred = credentials.Certificate(str(CRED_PATH))
    firebase_admin.initialize_app(cred)

db = firestore.client()

def get_all_employees():
    employees = []
    try:
        docs = db.collection("employees").stream()
        for doc in docs:
            emp = doc.to_dict()
            emp['id'] = doc.id
            employees.append(emp)
    except Exception as e:
        print("Error loading employees:", e)
    return employees

def get_employees_by_department(department_name):
    employees = []
    docs = db.collection("employees").where("department", "==", department_name).stream()
    for doc in docs:
        data = doc.to_dict()
        employees.append(data)
    return employees

def add_employee(data):
    try:
        db.collection("employees").add(data)
        return True, "Employee added successfully"
    except Exception as e:
        return False, f"Failed to add employee: {e}"

def update_employee(emp_id, data):
    try:
        db.collection("employees").document(emp_id).update(data)
        return True, "Employee updated successfully"
    except Exception as e:
        return False, f"Failed to update employee: {e}"

def delete_employee(emp_id):
    try:
        db.collection("employees").document(emp_id).delete()
        return True, "Employee deleted successfully"
    except Exception as e:
        return False, f"Failed to delete employee: {e}"

def get_employee(emp_id):
    try:
        doc = db.collection("employees").document(emp_id).get()
        if doc.exists:
            emp = doc.to_dict()
            emp['id'] = doc.id
            return emp
        else:
            return None
    except Exception as e:
        print("Error getting employee:", e)
        return None