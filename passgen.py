import random
import string
# Main Methods


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


def strong_pass_gen(length=8, percent_letters=.6, use_letters=True, use_numbers=True, use_special_chars=True, random_case=True):
    # return an empty string if thats what they asked for
    if (not (use_letters or use_numbers or use_special_chars)) or length == 0:
        return "What exactly did you expect?"

    # password should be mostly letters if letters are available
    password = ""

    count_letters = round(length * percent_letters)
    count_other = round(length - count_letters)

    if (not use_letters) or percent_letters == 0:
        count_letters = 0
        count_other = length
    if (not (use_numbers or use_special_chars)):
        count_letters = length
        count_other = 0

    password += generate_random_letter(count_letters, True)
    other_chars = ""
    if (use_numbers):
        other_chars += string.digits
    if (use_special_chars):
        other_chars += string.punctuation
    for i in range(count_other):
        password += random.choice(other_chars)
    password = shuffle_string(password)

    return password

#


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
        numString += string.digits
        index += 1
    return numString


def generate_special_chars(amount):
    chosen_chars = ""
    index = 0
    while index < amount:
        chosen_chars += random.choice(string.punctuation)
        index += 1
    return chosen_chars


def generate_random_letter(amount, random_case):
    chosenLetters = ""
    index = 0
    while index < amount:
        chosenLetters += str(random.choice(string.ascii_lowercase))
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
