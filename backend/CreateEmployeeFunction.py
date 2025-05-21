from pathlib import Path
import firebase_admin
from firebase_admin import credentials, firestore
from tkinter import messagebox

BASE_DIR = Path(__file__).resolve().parent.parent
CRED_PATH = BASE_DIR / "backend" / "serviceAccountKey.json"

class CreateEmployeeFunction:
    def __init__(self):
        try:
            if not firebase_admin._apps:
                cred = credentials.Certificate(str(CRED_PATH))
                firebase_admin.initialize_app(cred)
            self.db = firestore.client()
            print("Firebase initialized successfully")
        except Exception as e:
            messagebox.showerror("Firebase Error", f"Failed to initialize Firebase: {str(e)}")
    
    def validate_inputs(self, employee_data):
        required_fields = [
            ('employee_id', "Employee ID"),
            ('first_name', "First Name"),
            ('last_name', "Last Name"),
            ('department', "Department"),
            ('address', "Address"),
            ('phone_number', "Phone Number")
        ]
        
        for field, field_name in required_fields:
            if not employee_data.get(field):
                messagebox.showerror("Validation Error", f"{field_name} is required!")
                return False
        
        if employee_data['department'] == "Department":
            messagebox.showerror("Validation Error", "Please select a valid department.")
            return False

        phone = employee_data['phone_number']
        if not phone.isdigit() or len(phone) < 10:
            messagebox.showerror("Validation Error", "Phone number must be at least 10 digits and contain only numbers")
            return False
        
        return True
    
    def create_employee(self, employee_data):
        try:
            if not self.validate_inputs(employee_data):
                return False
            
            doc_ref = self.db.collection('employees').document(employee_data['employee_id'])
            if doc_ref.get().exists:
                messagebox.showerror("Error", "Employee ID already exists!")
                return False
            
            doc_ref.set({
                'employee_id': employee_data['employee_id'],
                'first_name': employee_data['first_name'],
                'last_name': employee_data['last_name'],
                'department': employee_data['department'],
                'address': employee_data['address'],
                'phone_number': employee_data['phone_number']
            })
            
            messagebox.showinfo("Success", "Employee created successfully!")
            return True
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create employee: {str(e)}")
            import traceback
            traceback.print_exc()
            return False
    
    def get_all_departments(self):
        return ["Secretariat", "Logistics", "Sales", "Labor", "Proprietor"]
    
    def clear_form(self, fields):
        for field in fields.values():
            if hasattr(field, 'delete'):
                field.delete(0, 'end')
            elif hasattr(field, 'set'):
                field.set('Department')