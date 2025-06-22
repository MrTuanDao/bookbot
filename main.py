import sys

from stats import get_book_text, count_word, count_character, sort_c_dict


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]

    num_words = count_word(get_book_text(filepath))
    count_c = count_character(get_book_text(filepath))
    c_dict_list = sort_c_dict(count_c)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for  c_dict in c_dict_list:
        if c_dict["char"].isalpha():
            print(f"{c_dict['char']}: {c_dict['num']}")
    print("============= END ===============")



main()