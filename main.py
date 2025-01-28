def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = len(file_contents.split())
        result = ""
        for line in file_contents:
            for char in line:
                if char.isalpha():
                    result += char
        result = result.lower()
        letter_count = {}
        for letter in result:
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
        sorted_keys = sorted(letter_count.keys())
        sorted_keys = {key: letter_count[key] for key in sorted_keys}
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count} words found in the document")
        print("\n")
        for key, val in sorted_keys.items():
            print(f"The {key} character was found {val} times")
        print("--- End report ---")
main()