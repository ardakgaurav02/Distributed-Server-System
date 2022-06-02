import socket
import os
import math
from watchdog.observers import Observer
from watchdog.events import *
import time
import shutil


def list():
    start_path = r'C:\Users\16825\PycharmProjects\pythonProject\MainProgram\ServerA\DataA'
    dir_count = 0
    file_count = 0

    # Traverse directory tree
    finale = ''
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

            finale = finale + '\t{:15.15s}{:8d} {:2s} {:18s}\n'.format(file, fsize, unit, mtime)

            file_count += 1
        break
    print(finale)
    c.send(bytes(finale, "utf-8"))


def syn():  # function to syn files between server A and B
    src = r'C:\Users\16825\PycharmProjects\pythonProject\MainProgram\ServerB\DataB' + '\\'
    dest = r'C:\Users\16825\PycharmProjects\pythonProject\MainProgram\ServerA\DataA' + '\\'

    for path, dirs, files in os.walk(src):
        if files:
            for file in files:
                if not os.path.isfile(dest + file):
                    shutil.copy(path + '\\' + file, dest + file)

s = socket.socket()  # create Socket
s.connect(('localhost', 9991))  # Conneting to a serverB
data = s.recv(1024).decode()

s = socket.socket()  # create Socket
print("Socket created")
s.bind(('localhost', 9999))  # bind Socket to port number
s.listen(3)
print("waiting for connection")
while True:
    c, addr = s.accept()  # Getting the address of client and the socket
    print("connection with", addr)
    list()
    syn()
    c.send(bytes(data, "utf-8"))
    list()

    class FileEventHandler(FileSystemEventHandler):  # Event Handler Class
        def __init__(self):
            FileSystemEventHandler.__init__(self)

        def on_moved(self, event):
            print("file modified from {0} to {1}".format(event.src_path, event.dest_path))
            dirname, basename = os.path.split(event.src_path)
            pathB = os.path.join(r'C:\Users\16825\PycharmProjects\pythonProject\MainProgram\ServerB\DataB', basename)
            os.remove(pathB)
            src = r'C:\Users\16825\PycharmProjects\pythonProject\MainProgram\ServerB\DataB' + '\\'
            dest = r'C:\Users\16825\PycharmProjects\pythonProject\MainProgram\ServerA\DataA' + '\\'
            for path, dirs, files in os.walk(src):
                if files:
                    for file in files:
                        if not os.path.isfile(dest + file):
                            shutil.copy(path + '\\' + file, dest + file)

        def on_created(self, event):
            if event.is_directory:
                print("directory created:{0}".format(event.src_path))
            else:
                print("file created:{0}".format(event.src_path))

        def on_deleted(self, event):
            print("file deleted:{0}".format(event.src_path))
            dirname, basename = os.path.split(event.src_path)
            pathB = os.path.join(r'C:\Users\16825\PycharmProjects\pythonProject\MainProgram\ServerB\DataB', basename)
            os.remove(pathB)

        def on_modified(self, event):
            for filename in os.listdir(folder_to_track):
                src = folder_to_track + '/' + filename
                new_dest = folder_destination + '/' + filename
                if not os.path.isfile(folder_destination + filename):
                    shutil.copy(src, new_dest)

    folder_to_track = r'C:\Users\16825\PycharmProjects\pythonProject\MainProgram\ServerA\DataA'
    folder_destination = r'C:\Users\16825\PycharmProjects\pythonProject\MainProgram\ServerB\DataB'
    if __name__ == "__main__":  # main fucntion Called
        observer = Observer()
        event_handler = FileEventHandler()
        observer.schedule(event_handler, folder_to_track, True)
        observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()


    
