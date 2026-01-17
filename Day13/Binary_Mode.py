# Goal: Read an image file.

with open("image.jpg","rb") as img:
  print(type(img.read()))
