def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    words = count_words(text)
    chars = counting_characters(text)
    print_report(chars,words)

def print_report(chars_dict,num_words):
    print("\n--- Begin report of books/frankenstein.txt ---")
    print(num_words,"words found in the document \n")
    sorted(chars_dict.items(), key=lambda x:x[1], reverse=True)
    for i,j in chars_dict.items():
        if i.isalpha():
            print("The",i,"character was found",j,"times")

    print("--- End report ---")



def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def counting_characters(text):
    chars={}
    for c in text:
        lowered=c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered]=1
    return chars



main()    