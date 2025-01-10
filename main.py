def main():
    book_path = "/home/bloodward/workspace/github.com/Bloodward/bookbot/books/Frankenstein.txt"
    book_text = get_book_text(book_path)
    book_num_words = get_num_words(book_text)
    book_letter_count = get_letter_count(book_text)

    print(book_letter_count)



    #print(f'{book_num_words} words found in the document')


    #Prints entire book out. 
    #print(book_text)

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

