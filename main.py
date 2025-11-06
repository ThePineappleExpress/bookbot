def get_book_text(file_path):
    with open(file_path, encoding="utf8") as f:
        file_content = f.read()
    return file_content

def main():
    file_path = './books/frankenstein.txt'
    file_content = get_book_text(file_path)
    print(file_content)
    return file_content


main()

    
