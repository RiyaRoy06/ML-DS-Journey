# Goal: Ask the user for a number. If the number is negative, manually trigger an error using raise ValueError("No Negatives").

x=int(input("Enter a number: "))
if x<0:
  raise ValueError("No Negatives")
