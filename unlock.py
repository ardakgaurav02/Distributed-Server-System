import sys
import os

# Unlocking File by using argument
if sys.argv[1] == '0':
    os.system(r"icacls C:\Users\16825\PycharmProjects\pythonProject\MainProgram\ServerA\DataA\FileA.txt /grant Everyone:(W)")
    print('FileA is Unlocked')

    file_to_read = r"C:\Users\16825\PycharmProjects\pythonProject\MainProgram\ServerB\DataB\FileA.txt"
    write_to_file = r"C:\Users\16825\PycharmProjects\pythonProject\MainProgram\ServerA\DataA\FileA.txt"

    # Reading a file
    file = open(file_to_read, "r")
    data = file.read()
    file.close()

    # Writing to a file
    with open(write_to_file, "a") as file:  # with method auto closes the file object
        file.write(data)
    #print('completed')

# Unlocking File by using argument
if sys.argv[1] == '1':
    os.system(r"icacls C:\Users\16825\PycharmProjects\pythonProject\MainProgram\ServerA\DataA\FileB.txt /grant Everyone:(W)")
    print('FileB is Unlocked')

    file_to_read = r"C:\Users\16825\PycharmProjects\pythonProject\MainProgram\ServerB\DataB\FileB.txt"
    write_to_file = r"C:\Users\16825\PycharmProjects\pythonProject\MainProgram\ServerA\DataA\FileB.txt"

    # Reading a file
    file = open(file_to_read, "r")
    data = file.read()
    file.close()

    # Writing to a file
    with open(write_to_file, "a") as file:  # with method auto closes the file object
        file.write(data)
    # print('completed')

# Unlocking File by using argument
if sys.argv[1] == '2':
    os.system(r"icacls C:\Users\16825\PycharmProjects\pythonProject\MainProgram\ServerA\DataA\FileC.txt /grant Everyone:(W)")
    print('FileC is Unlocked')

    file_to_read = r"C:\Users\16825\PycharmProjects\pythonProject\MainProgram\ServerB\DataB\FileC.txt"
    write_to_file = r"C:\Users\16825\PycharmProjects\pythonProject\MainProgram\ServerA\DataA\FileC.txt"

    # Reading a file
    file = open(file_to_read, "r")
    data = file.read()
    file.close()

    # Writing to a file
    with open(write_to_file, "a") as file:  # with method auto closes the file object
        file.write(data)
    # print('completed')

# Unlocking File by using argument
if sys.argv[1] == '3':
    os.system(r"icacls C:\Users\16825\PycharmProjects\pythonProject\MainProgram\ServerA\DataA\FileD.txt /grant Everyone:(W)")
    print('FileD is Unlocked')

    file_to_read = r"C:\Users\16825\PycharmProjects\pythonProject\MainProgram\ServerB\DataB\FileD.txt"
    write_to_file = r"C:\Users\16825\PycharmProjects\pythonProject\MainProgram\ServerA\DataA\FileD.txt"

    # Reading a file
    file = open(file_to_read, "r")
    data = file.read()
    file.close()

    # Writing to a file
    with open(write_to_file, "a") as file:  # with method auto closes the file object
        file.write(data)
    # print('completed')