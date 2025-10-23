# Function for retrieving number of words in text
def word_count(text):
    return len(text.split())

# Function to create dictionary with { character : no. of instances}
def char_count(text):
    char_dict = {}

    for character in text:
        character = character.lower()

        if character in char_dict:
            char_dict[character] += 1
        else:
            char_dict[character] = 1

    return char_dict

# Function to sort the character dictionary
# based on number of instances
def sort_dict(dict):
    char_list = []

    for key in dict.keys():
        char_list.append({"char": key, "num" : dict[key]})

    def sort_on(items):
        return items["num"]

    char_list.sort(reverse=True, key=sort_on)

    return char_list