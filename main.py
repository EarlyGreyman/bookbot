from stats import word_count, char_count, sort_dict

def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()

    return file_content

def main():
    # Declaring and importing book for analysis
    filepath = "books/frankenstein.txt"
    book = get_book_text(filepath)

    # Get character list in form {"char": "b", "num": 4868}
    char_list = sort_dict(char_count(book))

    # Print nice report
    print("============ BOOKBOT ============"
          f"Analyzing book found at {filepath}"
          "----------- Word Count ----------"
          f"Found {word_count(book)} total words"
          f"--------- Character Count -------")

    for dict in char_list:
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["num"]}")

    print("============= END ===============")

main()