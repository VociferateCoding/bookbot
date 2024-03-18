def main():
    book_file = open("books/frankenstein.txt")
    book_text = book_file.read()
    book_file.close()

    words = book_text.split()
    num_words = len(words)
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print()

    character_counts = {}
    for character in book_text.lower():
        if character.isalpha():
            if character in character_counts:
                character_counts[character] += 1
            else:
                character_counts[character] = 1

    character_counts_list = []
    for character, count in character_counts.items():
        character_counts_list.append((character, count))
    character_counts_list.sort(key=lambda x: x[1], reverse=True)

    for character, count in character_counts_list:
        print(f"The '{character}' character was found {count} times")

    print("--- End report ---")


main()
