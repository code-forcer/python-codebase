import re

def is_valid_email(email):
    # Regular expression pattern to validate an email address
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email)

def email_slicer(email):
    if is_valid_email(email):
        # Split the email into username and domain
        username, domain = email.split('@')
        return f"Username: {username}\nDomain: {domain}"
    else:
        return "Invalid email address. Please enter a valid email."

# Get user input
email = input("Enter your email address: ")
print(email_slicer(email))
