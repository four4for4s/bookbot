from stats import str2wordcount
from stats import str2charcount
from stats import sortdict
import sys

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    count = str2wordcount(text)
    chars = str2charcount(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    
    sorted_dict = sortdict(chars)
    for i in range(len(sorted_dict)):
        if sorted_dict[i]['name'].isalpha():
            print(f"{sorted_dict[i]['name']}: {sorted_dict[i]['num']}")

    print("============= END ===============")
main()
