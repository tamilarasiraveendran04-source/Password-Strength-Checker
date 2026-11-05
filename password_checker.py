
print("===== PASSWORD STRENGTH CHECKER =====")

password = input("Enter your password: ")

length_check = len(password) >= 8
uppercase_check = any(char.isupper() for char in password)
lowercase_check = any(char.islower() for char in password)
number_check = any(char.isdigit() for char in password)
special_check = any(not char.isalnum() and not char.isspace() for char in password)

print("\n----- PASSWORD ANALYSIS -----")

print("Minimum 8 characters:", length_check)
print("Uppercase letter:", uppercase_check)
print("Lowercase letter:", lowercase_check)
print("Number:", number_check)
print("Special character:", special_check)

if all([length_check, uppercase_check, lowercase_check,
        number_check, special_check]):

    print("\nPassword Strength: STRONG")
    print("Your password meets all the requirements.")

else:
    print("\nPassword Strength: WEAK")
    print("Suggestions to improve your password:")

    if not length_check:
        print("- Use at least 8 characters.")

    if not uppercase_check:
        print("- Add an uppercase letter (A-Z).")

    if not lowercase_check:
        print("- Add a lowercase letter (a-z).")

    if not number_check:
        print("- Add a number (0-9).")

    if not special_check:
        print("- Add a special character (@, #, $, !).")
