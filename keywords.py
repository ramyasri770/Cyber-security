import re

def is_phishing_email(email_text):
    phishing_keywords = ["urgent", "verify your account", "click here", "update payment", "reset password"]
    
    for keyword in phishing_keywords:
        if re.search(keyword, email_text, re.IGNORECASE):
            return True
    return False
email_text = input("Enter email text to scan: ")
if is_phishing_email(email_text):
    print("Warning: Possible phishing attempt detected!")
else:
    print("No phishing indicators found.")