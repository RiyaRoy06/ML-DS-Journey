# Goal: Create a variable x=0. Try to print 100/x. Catch the specific error that occures.

x=0
try:
  print(100/x)
except ZeroDivisionError:
  print("Cannot divide by zero.")
