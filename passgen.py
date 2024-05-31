import random
import string
# Main Methods


def strong_pass_gen(length=10, percent_letters=.4, use_special_chars=True, random_case=True):
    password = ""

    count_letters = round(length * percent_letters)
    count_other = round(length - count_letters)

    password += generate_random_letter(count_letters, True)
    other_chars = ""
    other_chars += string.digits
    if (use_special_chars):
        other_chars += string.punctuation
        password += generate_from_list(1, string.punctuation)
    password += generate_from_list(count_other, other_chars)
    password = shuffle_string(password)

    return password


def read_pass_gen_simple():
    password = ""
    lis = get_list()
    password += get_word_from_list(lis)
    password += generate_from_list(1, string.punctuation)
    password += generate_from_list(4, string.digits)
    return password
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
        words_list.append(random.choice(source.read().split(',')))
    return words_list


def get_word_from_list(source):
    random_index = random.randint(0, len(source)-1)
    return NormalCase(source[random_index].rstrip())


def generate_from_list(count, xList):
    newString = ""
    index = 0
    while index < count:
        newString += random.choice(xList)
        index += 1
    return newString


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


# print(strong_pass_gen(30))
print(read_pass_gen_simple())
