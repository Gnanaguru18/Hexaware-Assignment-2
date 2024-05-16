class InvalidDataException(Exception):
    def __init__(self, email):
        super().__init__(f"Entered email {email} is not valid")

def validate_email(email):
    import re
    email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    try:
        if not email_pattern.match(email):
            raise InvalidDataException(email)
    except InvalidDataException as e:
        print(e)
        return True
    else:
        return False
