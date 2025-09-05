import sys
from stats import get_book_text
from stats import count_characters
from stats import sort_dictionary

def calculate_num_words(book):
    num_words = len(book.split())
    print(f"Found {num_words} total words)")

def main():
    if(len(sys.argv) < 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        calculate_num_words(get_book_text(sys.argv[1]))
        print("--------- Character Count -------")
        for entry in sort_dictionary(count_characters(get_book_text(sys.argv[1]))):
            print(f"{entry['char']}: {entry['num']}")
        print("============= END ===============")
main()