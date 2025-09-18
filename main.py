from stats import get_word_count, get_char_count, sort_list
import sys
if (len(sys.argv) < 2):
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
    
def main():
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    num_words = get_word_count(book_text)
    char_count = get_char_count(book_text)
    new_list = sort_list(char_count)
    if (len(sys.argv) < 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        ###print(f"UNSORTED: {char_count}")
        # Loop through the sorted list and print each character's count
        for item in new_list:
            if item["character"].isalpha(): # Check if the character is an alphabet letter
                print(f"{item['character']}: {item['num']}")
        print("============= END ===============")
        
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


main()
