class InvalidDataException(Exception):
    pass

def validate_email(email):
    import re
    email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    try:
        if not email_pattern.match(email):
            raise InvalidDataException("Invalid email address provided")
    except InvalidDataException as e:
        print(e)

# Example usage:
# def register_user(name, email, password):
#     try:
#         validate_email(email)
#         print("User registered successfully")

#     except InvalidDataException as e:
#         print(e)
      

# Example:
# register_user("John Doe", "invalid_email", "password")
