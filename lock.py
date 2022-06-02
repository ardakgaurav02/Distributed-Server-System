import sys
import os

#Locking File by using argument
if sys.argv[1] == '0':
    os.system(r"icacls C:\Users\16825\PycharmProjects\pythonProject\MainProgram\ServerA\DataA\FileA.txt /deny Everyone:(W)")
    print('FileA is locked')

#Locking File by using argument
if sys.argv[1] == '1':
    os.system(r"icacls C:\Users\16825\PycharmProjects\pythonProject\MainProgram\ServerA\DataA\FileB.txt /deny Everyone:(W)")
    print('FileB is locked')

#Locking File by using argument
if sys.argv[1] == '2':
    os.system(r"icacls C:\Users\16825\PycharmProjects\pythonProject\MainProgram\ServerA\DataA\FileC.txt /deny Everyone:(W)")
    print('FileC is locked')

#Locking File by using argument
if sys.argv[1] == '3':
    os.system(r"icacls C:\Users\16825\PycharmProjects\pythonProject\MainProgram\ServerA\DataA\FileD.txt /deny Everyone:(W)")
    print('FileD is locked')