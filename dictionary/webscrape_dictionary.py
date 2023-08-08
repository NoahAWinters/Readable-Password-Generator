# Python 3.11.4
# pip install requests-html
# pip install bs4

# https://www.merriam-webster.com/browse/dictionary
# https://www.youtube.com/watch?v=zcszMBH6Lvc

from requests_html import HTMLSession
from bs4 import BeautifulSoup


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
invalid_characters = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "{", "}", "[", "]", ":", ";", "\"", "'", "<", ">", ",", ".", "?", "/", "\\", "|", "`", "~",
                      " ", "�", "á", "é", "í", "ó", "ú", "à", "è", "ì", "ò", "ù", "â", "ê", "î", "ô", "û", "ä", "ë", "ï", "ö", "ü", "ã", "õ", "ñ", "ç", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
vowels = ['a', 'e', 'i', 'o', 'u']
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
              'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']

minlength = 2
maxLength = 6


def validWordCheck(word):
    invalidWord = False

    # Check if String is a readable word
    if not checkIfWord(word):
        invalidWord = True

    # Check if word is too short or too long
    if len(word) > maxLength or len(word_str) < minlength:
        invalidWord = True

    # Check for Invalid Characters
    for chara in invalid_characters:
        if invalidWord:
            break
        if (chara in word_str):
            invalidWord = True
            break

    return invalidWord


def checkIfWord(word):
    containsVowels = False
    containsConsonants = False
    if any(char in vowels for char in word):
        containsVowels = True
    if any(char in consonants for char in word):
        containsConsonants = True
    return (containsVowels and containsConsonants)


with open(f'dict.txt', 'w') as file:
    for letter in letters:
        page_num = 1
        list_words = []

        while True:
            url = f'https://www.merriam-webster.com/browse/dictionary/{letter}/{page_num}/'
            session = HTMLSession()
            response = session.get(url)

            status_code = response.status_code

            print(status_code)
            if (status_code > 400):
                print("error reaching page {page_num}")
                break
            print(f'Parsing: {response.html.url}')

            # MW keeps its individual words in spans in a table
            soup = BeautifulSoup(response.html.html, 'html.parser')
            soup.encode("utf-8")
            words = soup.select('div.mw-grid-table-list span')

            # For our pruposes, words will be considered valid if they are at least 3 characters long and don't contain any non-standard alphabetic symbols

            for word in words:
                word_str = word.contents[0].lower()
                invalidWord = validWordCheck(word_str)

                if (not invalidWord):
                    list_words.append(word_str)
            # check if next page buttons are disabled
            next_disabled = soup.select('.next.disabled')
            if (next_disabled):
                # with open(f'{letter}.txt', 'w') as file:
                for word in list_words:
                    print(word + '\n')
                    word = str(word.encode('utf-8').decode('ascii', 'ignore'))
                    file.write(word + ',')
                break

            page_num += 1
