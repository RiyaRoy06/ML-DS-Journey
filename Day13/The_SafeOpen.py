# Goal: Write a file without .close().

with open("file.txt","w") as f:
  f.write("Hello Riya",)
print(f"File is closed: {f.closed}")
