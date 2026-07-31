count=0
name=input("enter your name:")
name=name.lower()
for ch in name:
  if ch in "aeiou":
    count+=1
print("Total number of vowels:", count)
