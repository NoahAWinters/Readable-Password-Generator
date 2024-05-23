import random
import string
# Main Methods


def strong_pass_gen(length=10, percent_letters=.6, use_special_chars=True, random_case=True):
    password = ""

    count_letters = round(length * percent_letters)
    count_other = round(length - count_letters)

    password += generate_random_letter(count_letters, True)
    other_chars = ""
    other_chars += string.digits
    if (use_special_chars):
        other_chars += string.punctuation
    password += random.choice(string.digits)
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
        numString += random.choice(string.digits)
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


strin = strong_pass_gen(10)
print(strin)
