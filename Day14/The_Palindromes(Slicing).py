# Goal: Check if a string is a palindrome.

s='Hi I am Riya'
a=''.join(x.lower() for x in s if x.isalnum())
print("This string is a palindrome: ",a==a[::-1])
