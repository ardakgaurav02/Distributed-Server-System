import os

dir_a = r'C:\Users\16825\PycharmProjects\pythonProject\MainProgram\Test\DataA'
#DirB files have .json extension
dir_b = r'C:\Users\16825\PycharmProjects\pythonProject\MainProgram\Test\DataB'

for fileA in dir_a:
  if not fileA in dir_b:
    os.remove(os.path.join(dir_a,(fileA)))