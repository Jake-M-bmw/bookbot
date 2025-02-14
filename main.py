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
        if char.isalpha():

            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count



file_contents = main()
words = word_count(file_contents)
char_counts = character_count(file_contents)


print(f"--- Begin report of books/frankenstein.txt ---")
print(f"{words} words found in the document\n")
for char, count in sorted(char_counts.items()):
    print(f"The '{char}' character was found {count} times")
print(f"--- End report ---")

