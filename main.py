def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()

    return file_content

def word_count(text):
    return len(text.split())

def main():
    print(f"Found {word_count(get_book_text("books/frankenstein.txt"))} total words")

main()