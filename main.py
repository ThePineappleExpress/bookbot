import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def get_book_text(file_path):
    with open(file_path, encoding="utf8") as f:
        file_content = f.read()
    return file_content

def main():
    from stats import split_to_words, pretty_counter
    
    file_path = sys.argv[1]
    file_content = get_book_text(file_path)
    list_of_letters = pretty_counter(file_content)
    
    print(
    f"============ BOOKBOT ============\n"
    f"Analyzing book found at {file_path}...\n"
    f"----------- Word Count ----------\n"
    f"Found {split_to_words(file_content)} total words\n"
    f"--------- Character Count -------"
    ) 
    for item in list_of_letters:
        if item["char"].isalpha():
            print(f'{item["char"]}: {item["num"]}')
    print("============= END ===============")
    return
    

main()



    
