# Python 3.11.4
# pip install requests-html
# pip install bs4

#https://www.merriam-webster.com/browse/dictionary
#https://www.youtube.com/watch?v=zcszMBH6Lvc

from requests_html import HTMLSession
from bs4 import BeautifulSoup

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
special_characters = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "{", "}", "[", "]", ":", ";", "\"", "'", "<", ">", ",", ".", "?", "/", "\\", "|", "`", "~", " ", "�"]


for letter in letters:
    page_num = 1
    list_words = []
    
    while True:
        url = f'https://www.merriam-webster.com/browse/dictionary/{letter}/{page_num}/'
        session = HTMLSession()
        response = session.get(url)
        
        status_code = response.status_code
        
        print(status_code)
        if(status_code > 400):
            print("error reaching page {page_num}")
            break
        print(f'Parsing: {response.html.url}')

        #MW keeps its individual words in spans in a table
        soup = BeautifulSoup(response.html.html, 'html.parser')
        words = soup.select('div.mw-grid-table-list span')
        
        for word in words:
            word_str = word.contents[0]
            invalidWord = False
            for chara in special_characters:
                if (chara in word_str):
                    print("invalid word detected")
                    invalidWord = True
                    break
            if(not invalidWord):
                list_words.append(word_str)
            
            
        #check if next page buttons are disabled
        next_disabled = soup.select('.next.disabled')   
        if(next_disabled):
            print(list_words)
            with open(f'{letter}.text', 'w') as file:
                for word in list_words:
                    file.write(word + ',')
            break
        
        page_num += 1