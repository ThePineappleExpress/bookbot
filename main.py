def get_book_text(file_path):
    with open(file_path, encoding="utf8") as f:
        file_content = f.read()
    return file_content       

def main():
    from stats import split_to_words
    file_path = './books/frankenstein.txt'
    file_content = get_book_text(file_path)
    result = split_to_words(file_content)
    return file_content, result


main()

    
