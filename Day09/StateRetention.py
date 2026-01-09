# Goal: Write a generator that calculates a "Running Average".

def running_average():
  a=0
  b=0
  avg=None
  while True:
    m=yield avg
    if m is not None:
      a+=m
      b+=1
      avg=a/b
g=running_average()
print(next(g))
print(g.send(5))
print(g.send(10))
print(g.send(15))
print(g.send(20))
