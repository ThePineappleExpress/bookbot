def split_to_words(file_content):
    num_words = 0
    book_list = file_content.split() 
    for word in book_list:
        num_words += 1 
    print(f"Found {num_words} total words")