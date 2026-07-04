def split_to_words(file_content):

    num_words = 0
    word_list = file_content.split() 

    for word in word_list:

        num_words += 1 

    return num_words 

def sort_on(input: tuple[str, int]) -> int:
    return input[1]

def chars_dict_to_sorted_list(input: dict[str, int]) -> list[tuple[str, int]]:
    empty_list = []
    for key, value in input.items():
        empty_list.append((key, value))
    sorted_list = sorted(empty_list, key=sort_on, reverse=True)
    return sorted_list
        


def count_character_population(file_content):
    file_content = file_content.lower()
    character_list = []
    counter = {}
    
    for character in file_content:
        
        current = counter.get(character, 0)
        
        if character.isalpha():
            
            if character not in character_list:
            
                character_list.append(character)
                counter[character] = current + 1
            
            else:
                counter[character] = current + 1

        else:
            continue

    return counter

def sorter(count):
    return count["num"]

def pretty_counter(file_content):
    counter = count_character_population(file_content)
    list_of_letters = []
    for character, count in counter.items():
        list_of_letters.append({"char": character, "num": count})
    list_of_letters.sort(reverse=True, key=sorter)
    

    return list_of_letters
    
     



