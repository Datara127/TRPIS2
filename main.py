from file_oper import read_file, write_file
from config import FILE_NAME

def main():
    write_file(FILE_NAME, "Hello")

    content = read_file(FILE_NAME)
    print(f"File content:\n{content}")

if __name__ == "__main__":
    main()