import sys
from stats import get_book_text
from stats import word_count
from stats import char_count
from stats import sort_char_count

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book = sys.argv[1]
        try:
            text = get_book_text(book)
        except FileNotFoundError as e:
            print(f"Error encountered: {e}")
            sys.exit(1)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book}...")
        print("----------- Word Count ----------")
        print(f"Found {word_count(text)} total words")
        print("--------- Character Count -------")
        for entry in sort_char_count(char_count(text)):
            if entry["char"].isalpha():
                print(f"{entry['char']}: {entry['num']}")
        print("============= END ===============")
main()