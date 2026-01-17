# Goal: Add a log line to a file without deleting old account.

with open("file.txt","a") as f:
  f.write("\nHello Riya")
with open("file.txt","w") as f:
  f.write("Hello Rai")
try:
  with open("file.txt","x") as f:
    f.write("First time file creation\n")
    print("File created successfully")
except FileExistsError:
    print("File already exists, not overwritten")
