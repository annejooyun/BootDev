from stats import count_words, count_char, sort_char_dict


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return(file_contents)


def main():

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")

    #Loading book
    frankenstein_fp = "./books/frankenstein.txt"
    frankenstein = get_book_text(frankenstein_fp)

    #Counting words
    num_words = count_words(frankenstein)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    #Counting characters
    chars = count_char(frankenstein)
    print("--------- Character Count -------")   
    sorted_chars = sort_char_dict(chars)

    for element in sorted_chars:
        if element["char"].isalpha():
            print(f"{element["char"]}: {element["num"]}")

    print("============= END ===============")
    

main()
