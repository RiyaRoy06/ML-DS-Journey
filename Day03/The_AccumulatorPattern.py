# Goal: Ask the user for a Number N(e.g., 5). Calculate the sum of all numbers from 1 to N(1+2+3+4+5).

N=int(input("Enter a Number: "))
sum=0
i=1
while i<=N:
  sum+=i
  i+=1
print("Sum = ",sum)
