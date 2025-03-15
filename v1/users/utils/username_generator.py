import hashlib
import random
import string


def generate_unique_username(email):
    # Extract the local part of the email (before @)
    email_local_part = email.split("@")[0]

    # Generate a short hash of the email to add uniqueness
    email_hash = hashlib.sha256(email.encode()).hexdigest()[:8]

    # Add a random string for additional uniqueness
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=4))

    # Combine parts to create the username
    username = f"{email_local_part}_{email_hash}_{random_string}"
    return username
