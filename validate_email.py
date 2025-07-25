import re


def is_valid_email(email):
    """
    Validate an email address using a regular expression.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if the email is valid, False otherwise.
    """
    email_regex = re.compile(
        r"^(?!.*\.\.)"                       # no consecutive dots
        r"[a-zA-Z0-9_.+-]+"                  # local part
        r"@"
        r"(?:[a-zA-Z0-9-]+\.)+"              # domain (at least one dot)
        r"[a-zA-Z]{2,}$"                     # TLD (at least two letters)
    )
    return email_regex.match(email) is not None


def validate_emails(email_list):
    """
    Validate a list of email addresses.

    Args:
        email_list (list): List of email addresses to validate.

    Returns:
        dict: Dictionary with email as key and validation result as value.
    """
    return {email: is_valid_email(email) for email in email_list}