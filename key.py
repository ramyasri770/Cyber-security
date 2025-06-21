import re

phishing_keywords = ["login", "verify", "update", "banking", "secure", "account", "password"]

def is_phishing_url(url):
        
    if re.search(r'\b[a-zA-Z0-9-]+\.com\b', url) and re.search(r'\b[a-zA-Z0-9-]+\.secure\b', url):
        return True

    for keyword in phishing_keywords:
        if keyword in url.lower():
            return True

    if re.search(r'--|@|%', url):
        return True
    
    return False

urls = [
    "https://secure-login.bank.com",
    "https://my-account.verification.com",
    "https://safe-shopping.com",
    "https://update-password.com",
]

for url in urls:
    print(f"URL: {url} --> {'Potential Phishing' if is_phishing_url(url) else 'Safe'}")