# Goal: Use gen.send(value) to inject data into a running generator.

def gen():
  a=0
  while True:
    m=yield a
    if m is not None:
      a+=m
    else:
      a=m
g=gen()
print(next(g))
print(g.send(2))
print(g.send(3))
print(g.send(4))
