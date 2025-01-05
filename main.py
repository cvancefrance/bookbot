def get_book_text(path):
    with open(path) as f:
        text = f.read()
    return text

def count_words(text):
    return len(text.split())

def count_characters(text):
    character_count = {}
    lowercase_text = text.lower()
    for i in lowercase_text:
        if i not in character_count:
            character_count[i] = 1
        else:
            character_count[i] += 1
    return character_count

def dict_to_list(dict):
    dict_list = []
    for char, num in dict.items():
         dict_list.append({"char": char, "num": num})
    return dict_list

def sort_on(dict):
    return dict["num"]
    



def main():
    text = get_book_text('books/frankenstein.txt')
    word_count = count_words(text)
    character_count = count_characters(text)
    dict_list = dict_to_list(character_count)
    dict_list.sort(reverse=True, key=sort_on)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f'{word_count} words found in the document\n')
    for item in dict_list:
        if item['char'].isalpha():
            print(f"The '{item['char']}' character was found {item['num']} times")
    print("--- End report ---")

main()