
email=input("enter your email:")
lenght=len(email)
if len(email)>=8 and "@" in email and "." in email and " " not in email:
    print("valid email")
else:
        print("invalid email")
