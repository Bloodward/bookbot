def main():
    book_path = "/home/bloodward/workspace/github.com/Bloodward/bookbot/books/Frankenstein.txt"
    book_text = get_book_text(book_path)
    book_num_words = get_num_words(book_text)

    print(f'{book_num_words} words found in the document')


    #Prints entire book out. 
    #print(book_text)

def get_num_words(text):
    words = text.split()
    return len(words)



def get_book_text(path):
    with open(path) as f:
        return f.read()

if __name__ == "__main__":
    main()

