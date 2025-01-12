def main():
    book_path = "/home/bloodward/workspace/github.com/Bloodward/bookbot/books/Frankenstein.txt"
    book_text = get_book_text(book_path)
    book_num_words = get_num_words(book_text)
    book_letter_count = get_letter_count(book_text)
    book_sort_characters = book_sorted_character_list(book_letter_count)

    print(f"--- Begin report of {book_path} ---")
    print(f'{get_num_words} words found in the fdocument')
    print()

    for item in book_sort_characters:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']} character was found {item['num']} times")
    
    print("--- End report ---")
    
    
    
    
    #print(book_letter_count)
    #print(f'{book_num_words} words found in the document')


    #Prints entire book out. 
    #print(book_text)

def sort_on(d):
    return d["num"]

def book_sorted_character_list(char_dict):
    sort_list = []
    for char in char_dict:
        sort_list.append({"char": char, "num": char_dict[char]})
    sort_list.sort(reverse=True, key=sort_on)
    return sort_list


def get_letter_count(text):
    characters = {}
    for c in text:
        lower_char = c.lower()
        if lower_char in characters:
            characters[lower_char] += 1
        else:
            characters[lower_char] = 1
    return characters


def get_num_words(text):
    words = text.split()
    return len(words)



def get_book_text(path):
    with open(path) as f:
        return f.read()

if __name__ == "__main__":
    main()

