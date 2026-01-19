# Goal: Print 1-100. Div by 3 "Fizz", by 5 "Buzz", both "FizzBuzz".

for i in range(1,101):
  print("FizzBuzz" if i%15==0 else "Fizz" if i%3==0 else "Buzz" if i%5==0 else i)
