# Goal: Write a while True generator that produces Fibonacci numbers forever.

def fibonacci():
  a,b=0,1
  while True:
    yield a
    a,b=b,a+b
f=fibonacci()
for _ in range(20):
  print(next(f))
