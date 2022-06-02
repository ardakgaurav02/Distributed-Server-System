from watchdog.observers import Observer
from watchdog.events import *
import time
import shutil
import math
import socket
import os

def list():
    start_path = r'C:\Users\16825\PycharmProjects\pythonProject\MainProgram\ServerA\DataA'
    dir_count = 0
    file_count = 0

    # Traverse directory tree
    finale = ''
    for (path, dirs, files) in os.walk(start_path):
        #print('List of directories of server A before syn')
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


class FileEventHandler(FileSystemEventHandler):                                       #Monitor Of client
    def __init__(self):
        FileSystemEventHandler.__init__(self)

    def on_moved(self, event):                                                          #Event On move capture
        if event.is_directory:
            print("directory moved from {0} to {1}".format(event.src_path,event.dest_path))
        else:
            print("file moved from {0} to {1}".format(event.src_path,event.dest_path))
        print("File of Server A and Server B")
        list()

    def on_created(self, event):                                                        #Event On create capture
        if event.is_directory:
            print("directory created:{0}".format(event.src_path))
        else:
            print("file created:{0}".format(event.src_path))
        print("File of Server A and Server B")
        list()

    def on_deleted(self, event):                                                    #Event On delete capture
        if event.is_directory:
            print("directory deleted:{0}".format(event.src_path))
        else:
            print("file deleted:{0}".format(event.src_path))
        print("File of Server A and Server B")
        list()

    def on_modified(self, event):                                                   #Event On modification capture
        if event.is_directory:
            print("directory modified:{0}".format(event.src_path))
        else:
            print("file modified:{0}".format(event.src_path))
        print("File of Server A and Server B")
        list()
def indexlist():
    path = r'C:\Users\16825\PycharmProjects\pythonProject\MainProgram\ServerB\DataB'

    files = os.listdir(path)
    for f in files:
        for idx, val in enumerate(files):
            print(idx, val)
        break

c = socket.socket()                                                  #create Socket
c.connect(('localhost', 9999))
while True:                                 #Conneting to a serverA
    print('Files from server A before syn')
    print("     File Name            Size      Last Modified ")
    print(c.recv(1024).decode())                                         #printing data recieved by Server A
    print('Files from server b before syn')
    print("     File Name            Size      Last Modified ")
    print(c.recv(1024).decode())                                         #printing data recieved by Server B
    indexlist()
    #print('Files from server A and Server b after syn')
    #print("     File Name            Size      Last Modified ")
    #print(c.recv(1024).decode())

    folder_to_track = r'C:\Users\16825\PycharmProjects\pythonProject\MainProgram\ServerA\DataA'
    folder_destination = r'C:\Users\16825\PycharmProjects\pythonProject\MainProgram\ServerB\DataB'
    if __name__ == "__main__":                                                      #Monitor Main Function
        observer = Observer()
        event_handler = FileEventHandler()
        observer.schedule(event_handler,folder_to_track,True)
        observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()
    break


