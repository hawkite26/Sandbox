def main():
    name = input("Name: ")
    vowel_count = check_for_vowels(name)
    print('Out of {} letters, {} has {} vowels ("y" not counted)'.format(len(name), name, vowel_count))


def check_for_vowels(name):
    """Check for vowels"""
    vowels = 0
    for letter in name.lower():
        if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
            vowels += 1
    return vowels


main()
