import os

def principal():
    print(f"The name of this module is: {__name__}")
    # code
    # ...

def main():
    for root, directories, files in os.walk("C:/Users/User/"):
        print(f"Root: {root}")
        print(f"Directories: {directories}")
        print(f"Files: {files}")

if __name__ == '__main__':
    principal()
