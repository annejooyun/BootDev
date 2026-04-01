from stats import count_words, count_char, sort_char_dict
import sys


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return(file_contents)


def main():

    if len(sys.argv) != 2:
        print(len(sys.argv))
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:

        filepath = sys.argv[1]


        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {filepath}...")

        #Loading book
        book = get_book_text(filepath)

        #Counting words
        num_words = count_words(book)
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")

        #Counting characters
        chars = count_char(book)
        print("--------- Character Count -------")   
        sorted_chars = sort_char_dict(chars)

        for element in sorted_chars:
            if element["char"].isalpha():
                print(f"{element["char"]}: {element["num"]}")

        print("============= END ===============")
    

main()
