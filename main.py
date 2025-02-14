def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents

def word_count(text):
    words = text.split()
    return(len(words))

def character_count(text):
    char_count ={}
    for char in text:
        char = char.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count



file_contents = main()
print(word_count(file_contents))
print(character_count(file_contents))