from stats import word_count, char_count, sort_dict
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()

    return file_content

def main():
    # Checking if filepath to book is provided
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        filepath = sys.argv[1]

    # Declaring and importing book for analysis
    book = get_book_text(filepath)

    # Get character list in form {"char": "b", "num": 4868}
    char_list = sort_dict(char_count(book))

    # Print nice report
    print("============ BOOKBOT ============\n"
          f"Analyzing book found at {filepath}\n"
          "----------- Word Count ----------\n"
          f"Found {word_count(book)} total words\n"
          f"--------- Character Count -------")

    for dict in char_list:
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["num"]}")

    print("============= END ===============")

main()