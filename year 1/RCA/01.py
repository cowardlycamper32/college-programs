import os

def read_file(file_path):
    if not(os.path.exists("./nonexistent")):
        os.mkdir("./nonexistent")
    with open(file_path, 'a+') as file:
        return file.read()

def count_words_in_file(file_path):
    content = read_file(file_path)
    words = content.split()
    return len(words)

def main():
    file_path = "./nonexistent/file.txt"
    word_count = count_words_in_file(file_path)
    print(f"The file contains {word_count} words.")

main()

