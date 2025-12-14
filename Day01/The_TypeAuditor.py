# Goal: Ask the user to type a number.
#      1. Print the type() of the raw input.
#      2. Cast it to a float.
#      3. Print the type() again. 

num = input("Enter a number : ")
print(type(num))
try:
   new_num=float(num)
   print(type(new_num))
except Error:
  print("Invalid number.")
