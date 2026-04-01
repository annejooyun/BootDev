from stats import count_words, count_char


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return(file_contents)


def main():
    frankenstein_fp = "./books/frankenstein.txt"
    frankenstein = get_book_text(frankenstein_fp)
    num_words = count_words(frankenstein)
    print(f"Found {num_words} total words")

    chars = count_char(frankenstein)
    print(chars)


main()
