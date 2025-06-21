import re

def is_suspicious_url(url):
    suspicious_patterns = [r"login.*", r"verify.*", r"update.*", r"\d{2,}"]
    for pattern in suspicious_patterns:
        if re.search(pattern, url, re.IGNORECASE):
            return True
    return False
def check_domain_reputation(url):
    try:
        response = requests.get(f"https://api.example.com/check?domain={url}")
        data = response.json()
        return data.get("reputation", "Unknown")
    except Exception:
        return "Error checking domain"
url = input("Enter a URL to check: ")
if is_suspicious_url(url):
    print("Warning: This URL may be phishing-related.")
else:
    reputation = check_domain_reputation(url)
    print(f"Domain reputation: {reputation}")