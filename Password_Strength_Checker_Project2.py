print("")
print("Welcome to Password Strength Checker!")
print("-> You can now set a password and check its strength")
while True:
    pswd = input("Enter your Password: ")
    length = len(pswd)
    hasUpper = any(ch.isupper() for ch in pswd)
    hasLower = any(ch.islower() for ch in pswd)
    hasDigit = any(ch.isdigit() for ch in pswd)
    if length < 6:
        print("Weak Password (Too short)")
        print("Please try again :(")
        continue
    elif hasUpper and hasLower and hasDigit and length >= 8:
        print("Strong Password :)")
        break
    else:
        print("Medium Password - Accepted")
        reasons = []
        if not hasUpper:
            reasons.append("missing uppercase letter")
        if not hasLower:
            reasons.append("missing lowercase letter")
        if not hasDigit:
            reasons.append("missing digit")
        if length < 8:
            reasons.append("length less than 8 characters")
        print("Reason:", ", ".join(reasons))
        break
print("Password set successfully!!")
