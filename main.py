

def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
    return file_contents    


def count_words(book):
    words = book.split()
    count = len(words)
    return count


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


def print_report(char_count):
    sorted_char_count = sorted(char_count.items(), key = lambda x: x[1], reverse=True)
    for key, value in sorted_char_count:
        print(f"The '{key}' character was found {value} times\n")


def full_report():
    book = main()
    word_count = count_words(book)
    char_count = count_characters(book)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words in the document")
    print("")
    print_report(char_count)
    print("--- End report ---") 


if __name__ == "__main__":
    full_report()
