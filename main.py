

def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
    return file_contents


def count_words(book):
    words = book.split()
    count = len(words)
    print(count)


def count_characters(book):
    book_lower = book.lower()
    char_count = {}

    for char in book_lower:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count


if __name__ == "__main__":
    book = main()
    print(count_characters(book))
