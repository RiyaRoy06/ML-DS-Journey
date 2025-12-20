# Goal: Write a function connect(port=3306) that prints "Connecting to [port]". Call it once with no arguments, and once with 5432.

def connect(port=3306):
  print(f"Connecting to {port}")
connect()
connect(5432)
