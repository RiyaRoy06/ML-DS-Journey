# Goal: Writre a script that asks the user for their age. If they type text(e.g., "twenty"), print "Numbers only" instead of crashing.

try:
  age=int(input("Enter your age: "))
  #print("Your age is: ",age)
except ValueError:
  print("Numbers only")
