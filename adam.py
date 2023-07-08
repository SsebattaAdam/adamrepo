# Create a file and write content into it
with open('example.txt', 'w') as file:
    file.write('Hello, world!\nThis is an example file.')



class FileContextManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

# Usage
with FileContextManager('example.txt', 'r') as file:
    contents = file.read()
    print(contents)


# Usage of FileContextManager to read the file
with FileContextManager('example.txt', 'r') as file:
    contents = file.read()
    print(contents)


import sqlite3

class DatabaseContextManager:
    def __init__(self, dbname):
        self.dbname = dbname
        self.conn = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.dbname)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()

# Usage
with DatabaseContextManager('car.db') as conn:
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    results = cursor.fetchall()
    for row in results:
        print(row)

import time
import threading
import multiprocessing

def process_function(time_seconds):
    time.sleep(time_seconds)
    print(f"Process finished after {time_seconds} seconds")

if __name__ == '__main__':
    # Multithreading
    thread_1 = threading.Thread(target=process_function, args=(3,))
    thread_2 = threading.Thread(target=process_function, args=(5,))

    thread_1.start()
    thread_2.start()

    thread_1.join()
    thread_2.join()

    # Multiprocessing
    multiprocessing.freeze_support()  # Add this line for Windows compatibility

    process_1 = multiprocessing.Process(target=process_function, args=(3,))
    process_2 = multiprocessing.Process(target=process_function, args=(5,))

    process_1.start()
    process_2.start()

    process_1.join()
    process_2.join()


