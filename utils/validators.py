import re

def validate_email(email):
    """
    Validate email format.
    """
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)


def validate_password(password):
    """
    Password requirements:
    - Minimum 8 characters
    - At least one uppercase letter
    - At least one lowercase letter
    - At least one digit
    """

    if len(password) < 8:
        return False

    if not re.search(r'[A-Z]', password):
        return False

    if not re.search(r'[a-z]', password):
        return False

    if not re.search(r'\d', password):
        return False

    return True


def validate_task_status(status):
    """
    Allowed task statuses.
    """
    allowed_status = [
        "Pending",
        "In Progress",
        "Completed"
    ]

    return status in allowed_status