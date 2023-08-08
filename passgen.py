# pick random words from text file
import random

spec_chars = ["!", "@", "#", "$", "%", "^", "&", "*",
              "(", ")", "-", "_", "+", "=", "{", "}", "[", "]", ":", ";", "\"", "'", "<", ">", ",", ".", "?", "/", "\\", "|", "`", "~"]


def passGen(passLength):
    password = ""
    wordCount = 0
    # word Pass
    while wordCount <= 2 and len(password) < passLength:
        password = (password + getRandomWord())
        numChars = random.randrange(0, 3)
        password = password + generateCharacters(numChars)
        wordCount += 1
    # number Pass

    addToFront = (bool(random.getrandbits(1)))
    if addToFront:
        password = addCharactersToFront(password)
    password = password + getRandomNums()
    print(password)


def getRandomWord():
    pw = (random.choice(
        open("dictionary\dict.txt").read().split(',')))
    pw = normalCase(pw)
    return pw


def getRandomCharacter():
    if (bool(random.getrandbits(1))):
        chara = str(random.choice(spec_chars))
    else:
        chara = getRandomNums()
    return chara


def generateCharacters(count):
    returnVal = ""

    check = False
    index = 0
    while check == False:
        addOn = getRandomCharacter()
        returnVal = returnVal + addOn
        index += 1

        if index >= count:
            check = True
    return returnVal


def getRandomNums():
    return str(random.randrange(0, 9))


def addCharactersToFront(password):
    numChars = random.randrange(0, 3)
    frontString = generateCharacters(numChars)
    password = frontString + password
    return password


def listToString(lis):
    word = ""
    for letter in lis:
        word += str(letter)
    return word


def normalCase(word):
    wordArray = [char for char in word]
    wordArray[0] = wordArray[0].upper()
    return listToString(wordArray)


def randomCase(word):
    index = 0
    wordArray = [char for char in word]
    for char in word:
        if (bool(random.getrandbits(1))):
            wordArray[index] = char.upper()
        index += 1
    return listToString(wordArray)


index = 0
while index < 500:
    passGen(10)
    index += 1
# open file in read mode
