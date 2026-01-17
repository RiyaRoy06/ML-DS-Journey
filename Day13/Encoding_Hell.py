# Goal: Fix a "UnicodeDecodeError".

with open("u.txt","w",encoding="utf-8") as f:
  f.write("Hello Riya")
with open('u.txt','r',encoding='utf-8') as f:
    print(f.read())
