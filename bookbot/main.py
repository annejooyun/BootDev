
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return(file_contents)

def count_words(file_string):
    file_arr = file_string.split()
    return len(file_arr)

def main():
    frankenstein_fp = "./books/frankenstein.txt"
    frankenstein = get_book_text(frankenstein_fp)
    num_words = count_words(frankenstein)
    print(f"Found {num_words} total words")


main()
