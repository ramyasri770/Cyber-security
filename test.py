import re
phishing_keywords = ["login", "secure", "update", "verify", "account", "banking", "password", "confirm"]

def is_phishing_url(url):
    if url.startswith("http://"):
        return True, "URL uses HTTP instead of HTTPS."
    for keyword in phishing_keywords:
        if keyword in url.lower():
            return True, f"Suspicious keyword found: '{keyword}' in URL."
    if not re.match(r"https?://[a-zA-Z0-9.-]+", url):
        return True, "URL format seems unusual."
    return False, "URL appears to be safe."
url_to_check = input("Enter a URL to check: ")
is_phishing, reason = is_phishing_url(url_to_check)

if is_phishing:
    print(f" Potential phishing detected: {reason}")
else:
    print(" URL seems safe.")
