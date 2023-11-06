import random

# Main Method


def readable_pass_gen(source, word_count, separator="", num_count=0, spec_char_count=0, shuffle=False):
    new_pass = get_words_from_list(source, word_count)
    if num_count != 0:
        new_numbers = generate_numbers(num_count)
        new_pass.append(new_numbers)
    if spec_char_count != 0:
        new_special_chars = generate_special_chars(spec_char_count)
        new_pass.append(new_special_chars)
    if shuffle:
        random.shuffle(new_pass)

    return separator.join(new_pass)


def unreadable_pass_gen(length=8, use_letters=True, use_numbers=True, use_special_chars=True, random_case=True):
    characters = ""

    if use_letters:
        characters += generate_random_letter(length, True)
    if use_numbers:
        characters += generate_numbers(length)
    if use_special_chars:
        characters += generate_special_chars(length)

    password = ''.join(random.choice(characters) for _ in range(length))

    return password

#########################


# Generative
def get_list():
    with open("dictionary\dict.txt", 'r') as file:
        dict = list(file)
    return dict


def get_words_from_list(source, word_count):
    words_list = []
    for words in range(0, word_count):
        random_index = random.randint(0, len(source)-1)
        words_list.append(NormalCase(source[random_index].rstrip()))
        # words_list.append(random.choice(source.read().split(',')))
    return words_list


def generate_numbers(num_count):
    numString = ""
    index = 0
    while index < num_count:
        numString += str(random.randrange(0, 9))
        index += 1
    return numString


def generate_special_chars(amount):
    spec_chars = "!@#$%^&*-_+=<>,.?~"

    chosen_chars = ""
    index = 0
    while index < amount:
        chosen_chars += str(random.choice(spec_chars))
        index += 1
    return chosen_chars


def generate_random_letter(amount, random_case):
    letters = "abcdefghijklmnopqrstuvwxyz"

    chosenLetters = ""
    index = 0
    while index < amount:
        chosenLetters += str(random.choice(letters))
        index += 1
    if (random_case):
        chosenLetters = RandomCase(chosenLetters)
    return chosenLetters


# Case Methods
def listToString(lis):
    word = ""
    for letter in lis:
        word += str(letter)
    return word


def NormalCase(word):
    wordArray = [char for char in word]
    wordArray[0] = wordArray[0].upper()
    return listToString(wordArray)


def RandomCase(word):
    index = 0
    wordArray = [char for char in word]
    for char in word:
        if (bool(random.getrandbits(1))):
            wordArray[index] = char.upper()
        index += 1
    return listToString(wordArray)


def shuffle_string(word):
    li = list(word)
    random.shuffle(li)
    shuffle_string = ''.join(li)
    return shuffle_string


def validate_password(password):
    if (length > 8):
        lower_case = False
        upper_case = False
        num = False
        special = False
        pass
    else:  # too short
        return False


#############################

words = get_list()
test = readable_pass_gen(words, 2, "", 3, 1, True)
print(test)
test = unreadable_pass_gen(20)
print(test)
