def check_password_length(password):
    if len(password)<6:
        raise Exception("Password must be at least 6 characters long")


