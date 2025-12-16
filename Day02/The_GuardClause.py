# Goal: Create a variable user=None. Write an if statement that checks if user is None And if user has an "admin" access.

user=None
try:
  if user is not None and user=="admin":
    print("Access.")
  else :
    print("Does not access")
except Error:
  print("Error")
