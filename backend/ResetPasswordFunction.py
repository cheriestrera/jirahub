import requests

class ResetPasswordFunction:
    def __init__(self):
        self.api_key = "AIzaSyDgOE9QEdwf0KAAJk1d0Zx4SvHzbK_rTzk"
        
    def send_reset_email(self, email):
        url = f"https://identitytoolkit.googleapis.com/v1/accounts:sendOobCode?key={self.api_key}"
        payload = {
            "requestType": "PASSWORD_RESET",
            "email": email
        }
        try:
            response = requests.post(url, json=payload)
            data = response.json()
            
            if "error" in data:
                return False, data["error"]["message"]
            return True, "Password reset email sent"
        except Exception as e:
            return False, str(e)