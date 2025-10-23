def word_count(text):
    return len(text.split())

def char_count(text):
    char_dict = {}

    for character in text:
        character = character.lower()

        if character in char_dict:
            char_dict[character] += 1
        else:
            char_dict[character] = 1

    return char_dict