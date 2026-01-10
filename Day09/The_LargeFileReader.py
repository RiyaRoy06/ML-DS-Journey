# Goal: Write a generator to read a "file" 100GB file line-by-line.

def fake_file():
    for i in range(5):
        yield f"Line {i}"

for line in fake_file():
    print(line)
