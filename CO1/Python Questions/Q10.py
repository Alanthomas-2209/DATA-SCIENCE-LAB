# 10.	Write a Python program to check the validity of a password given by the  user.
# The Password should satisfy the following criteria:
# 1.	Contains at least one letter between a and z
# 2.	Contains at least one number between 0 and 9
# 3.	Contains at least one letter between A and Z
# 4.	Contains at least one special character from $, #, @
# 5.	Minimum length of password: 6


import re

def is_valid_password(password):
    if len(password) < 6:
        print("Password is too short. It should be at least 6 characters long.")
        return False

    if not re.search(r'[a-z]', password):
        print("Password doesn't contain any lowercase letters (a-z).")
        return False

    if not re.search(r'[A-Z]', password):
        print("Password doesn't contain any uppercase letters (A-Z).")
        return False

    if not re.search(r'[0-9]', password):
        print("Password doesn't contain any digits (0-9).")
        return False

    if not re.search(r'[$#@]', password):
        print("Password doesn't contain any of the special characters ($, #, @).")
        return False

    return True

password = input("Enter a password: ")

if is_valid_password(password):
    print("Password is valid.")
else:
    print("Password is invalid. Please ensure it meets the specified criteria.")


# def is_valid_password(password):
#     if len(password) < 6:
#         return False
    
#     has_lowercase = False
#     has_uppercase = False
#     has_digit = False
#     has_special_char = False

#     special_characters = {'$', '#', '@'}

#     for char in password:
#         if char.islower():
#             has_lowercase = True
#         elif char.isupper():
#             has_uppercase = True
#         elif char.isdigit():
#             has_digit = True
#         elif char in special_characters:
#             has_special_char = True

#     if has_lowercase and has_uppercase and has_digit and has_special_char:
#         return True

#     return False
