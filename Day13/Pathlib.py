# Goal: Join a folder and filename safely on Windows and Mac.

from pathlib import Path
folder=Path('Riya')
file=('Rai.txt')
print(folder/file)
