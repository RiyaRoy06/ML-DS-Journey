# Goal: Create a global variable x=10. Write a function change_x() that sets x=20 inside it. Print x outside the function.

x=10
def change_x():
  global x
  x=20
print(x)
