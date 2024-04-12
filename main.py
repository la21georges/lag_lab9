def encoder(password_string):
    new_password = ""
    for digit in password_string:
        digit = int(digit)
        digit += 3
        new_password += str(digit)
    return new_password

print(encoder("12345555"))

def decoder(password_string):
    new_password = ""
    for digit in password_string:
        digit = int(digit)
        digit -= 3
        new_password -= str(digit)
    return new_password
