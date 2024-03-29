def main():
    text = get_book_text('books/frankenstein.txt')
    num_words = get_num_words(text)
    num_chars = get_num_chars(text.lower())
    print("--- Begin report of books/frankenstein.txt ---")
    print(f'{num_words} characters found\n\n')
    letter_list = present(num_chars)
    for i in letter_list:
        print(f'The {i["char"]} character was found {i["num"]} times')
    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_num_chars(lower_text):
    char_count = {}
    for letter in lower_text:
        if letter in char_count:
            char_count[letter] += 1
        else:
            char_count[letter] = 1
    return char_count


def present(num_chars):
    def sort_on(dict):
        return dict['num']
    letter_list = []
    for key in num_chars:
        if key.isalpha():
            letter_list.append({'char': key, 'num': num_chars[key]})
    letter_list.sort(reverse=True, key=sort_on)
    return letter_list


main()
