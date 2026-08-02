
'''
Phone number Valid agirbeku andre:

✅ Exactly 10 digits irbeku.
✅ Space irabaradu.
✅ Alphabets irabaradu.
✅ Special characters irabaradu.
✅ First digit 6, 7, 8 athava 9 agirbeku.
'''

space_count=0
uppercase_count=0
lowercase_count=0
special_count=0
phone_no=input("enter your password:")
for ch in phone_no:
    if ch in " ":
        space_count+=1
    if ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        uppercase_count+=1
    if ch in "abcdefghijklmnopqrstuvwxyz":
        lowercase_count+=1
    if ch in "!@#$%^&-_*?":
        special_count+=1

if(
    len(phone_no)==10
    and space_count==0
    and uppercase_count==0
    and lowercase_count==0
    and special_count==0
    and phone_no[0] in "6789"
):
    print("valid number")
else:
    print("invalid number")   

