from stats import get_num_words, get_letter_count, sort_letter_count
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


    book = sys.argv[1]
    book_text = get_book_text(book)
    num_words = get_num_words(book_text)
    letter_count = get_letter_count(book_text)
    sorted_letters = sort_letter_count(letter_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("------------ Word Count ------------")
    print(f"Found {num_words} total words")
    print("--------- Character Count ---------")
    
    for item in sorted_letters:
        print(f"{item['char']}: {item['num']}")
    
    print ("============= END ===============")

if __name__ == "__main__":
    main()