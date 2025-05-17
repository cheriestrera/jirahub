import firebase_admin
from firebase_admin import credentials, firestore

if not firebase_admin._apps:
    cred = credentials.Certificate("C:/Users/Marites/Downloads/CC15project/backend/serviceAccountKey.json")
    firebase_admin.initialize_app(cred)

db = firestore.client()

def get_all_employees():
    """Return a list of all employee dicts with their Firestore document IDs."""
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

def get_employees_by_department(department):
    """Return a list of employees filtered by department."""
    employees = []
    try:
        docs = db.collection("employees").where("Department", "==", department).stream()
        for doc in docs:
            emp = doc.to_dict()
            emp['id'] = doc.id
            employees.append(emp)
    except Exception as e:
        print("Error filtering employees:", e)
    return employees

def add_employee(data):
    """Add a new employee. Data is a dict with Name, Department, Email, Phone."""
    try:
        db.collection("employees").add(data)
        return True, "Employee added successfully"
    except Exception as e:
        return False, f"Failed to add employee: {e}"

def update_employee(emp_id, data):
    """Update an existing employee by document ID."""
    try:
        db.collection("employees").document(emp_id).update(data)
        return True, "Employee updated successfully"
    except Exception as e:
        return False, f"Failed to update employee: {e}"

def delete_employee(emp_id):
    """Delete an employee by document ID."""
    try:
        db.collection("employees").document(emp_id).delete()
        return True, "Employee deleted successfully"
    except Exception as e:
        return False, f"Failed to delete employee: {e}"

def get_employee(emp_id):
    """Get a single employee's data by document ID."""
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