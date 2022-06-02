import socket
import os
import math
import shutil
from watchdog.events import *
import time

def list():
    start_path = r'C:\Users\16825\PycharmProjects\pythonProject\MainProgram\ServerB\DataB'
    dir_count = 0
    file_count = 0
    # Traverse directory tree
    final = ''
    for (path, dirs, files) in os.walk(start_path):
        dir_count += 1
        # Repeat for each file in directory
        for file in files:
            fstat = os.stat(os.path.join(path, file))

            # Convert file size to MB, KB or Bytes
            if (fstat.st_size > 1024 * 1024):
                fsize = math.ceil(fstat.st_size / (1024 * 1024))
                unit = "MB"
            elif (fstat.st_size > 1024):
                fsize = math.ceil(fstat.st_size / 1024)
                unit = "KB"
            else:
                fsize = fstat.st_size
                unit = "B"

            mtime = time.strftime("%X %x", time.gmtime(fstat.st_mtime))

            final = final + '\t{:15.15s}{:8d} {:2s} {:18s}\n'.format(file, fsize, unit, mtime)

            file_count += 1
        break
    print(final)
    s.send(bytes(final, "utf-8"))

def syn():                                                              #function to syn files between server A and B
    src = r'C:\Users\16825\PycharmProjects\pythonProject\MainProgram\ServerA\DataA' + '\\'
    dest = r'C:\Users\16825\PycharmProjects\pythonProject\MainProgram\ServerB\DataB' + '\\'

    for path, dirs, files in os.walk(src):
        if files:
            for file in files:
                if not os.path.isfile(dest + file):
                    shutil.copy(path + '\\' + file, dest + file)

b = socket.socket()                                                               #create Socket
print("Socket created")
b.bind(('localhost', 9991))                                                       #bind Socket to port number
b.listen(3)
print("waiting for connection")
while True:
    s, addr = b.accept()                                                          #Getting the address of client and the socket
    print("connection with", addr)
    print('List of directories of server B before syn')
    list()                                                                         #sending data to Server A
    syn()
    list()


