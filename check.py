import re

def check_phishing_url(url):
    phishing_keywords = ["login", "verify", "banking", "update", "free", "gift",
                         "password", "security", "urgent", "click", "account"]
    
    if any(keyword in url.lower() for keyword in phishing_keywords):
        return "Warning: This URL may be suspicious!"
    trusted_domains = ["example.com", "bank.com", "secure-site.com"]
    if not any(domain in url for domain in trusted_domains):
        return "Caution: This domain is not in the trusted list."
    return "This URL seems safe."
user_url = input("Enter a URL to check: ")
result = check_phishing_url(user_url)
print(result)