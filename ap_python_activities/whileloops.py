#washer_timer = input('How long do you want to wash your clothes')
#hile washer_timer > 0:
 #  print('clothes are still washing')

def is_valid_password(password):
    min_length = 8  # Minimum password length

    return len(password) >= min_length

# Example usage:
password = "Password1"  # Change this to the password you want to check
valid = is_valid_password(password)
print("Is the password valid?", valid)