uppercase=0
lowercase=0
num=0
space=0
spacial_char=0
username=input("enter a username:")
lenght=len(username)
for ch in username:
    if ch in "012345689":
        num+=1
    if ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        uppercase+=1
    if ch in "abcdefghijklmnopqrstuvwxyz":
        lowercase+=1
    if ch == " ":
        space+=1
    if ch in "!@#$%^&*?/":
        spacial_char+=1
if(
      6<= len(username)<= 15
      and username[0] not in "0123456789"
      and spacial_char==0
      and space==0
      and uppercase>=1
      and lowercase>=1
      and num>=1
      and username[0] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ):

    print("valid username")
else:
    print("invalid username")



    
        