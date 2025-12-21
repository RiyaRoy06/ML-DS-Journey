# Goal: Write a try/except block that divides two numbers. Add a finally block that print "Execusion Complete" regardless of whether the division succeeded or failed.

x=int(input("Enter first number: "))
y=int(input("Enter second number: "))
try:
  print(x/y)
except ZeroDivisionError:
  print("Cannot divide by zero.")
finally:
  print("Execution Complete")
