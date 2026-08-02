count=0
space_count=0
name=input("enter your name:")
name=name.lower()
for ch in name:
    if ch in "aeiou":
        count+=1
    if ch == " ":
        space_count+=1
print("Total no.of Ovels:", count)
print("No.of spaces:", space_count)
