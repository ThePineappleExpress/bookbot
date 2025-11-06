def get_book_text(file_path):
    with open(file_path, encoding="utf8") as f:
        file_content = f.read()
    return file_content

def split_to_words(file_content):
    num_words = 0
    book_list = file_content.split(" ") 
    for word in book_list:
        num_words += 1 
    print(f"Found {num_words} total words")
        
        

def main():
    file_path = './books/frankenstein.txt'
    file_content = get_book_text(file_path)
    result = split_to_words(file_content)
    return file_content, result


main()

    
