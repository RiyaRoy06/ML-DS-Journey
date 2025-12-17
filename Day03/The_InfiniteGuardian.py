# Goal: Write a script that askas the user for password repeatedly. It must run forever until the user types "stop".

while True:
  pwd=input("Set Password: ")
  if pwd=="stop":
    break
