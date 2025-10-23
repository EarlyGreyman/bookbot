from stats import word_count, char_count

def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()

    return file_content

def main():
    book = get_book_text("books/frankenstein.txt")
    print(f"Found {word_count(book)} total words\n")
    print(char_count(book))

main()