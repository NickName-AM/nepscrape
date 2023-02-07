import requests
from bs4 import BeautifulSoup
import sys

def usage():
    print(f'python3 {sys.argv[0]} <english_word>')


if len(sys.argv) != 2:
    usage()
    exit(-1)

english_word = sys.argv[1]

def get_nepali_word(word):
    URL = f'https://www.english-nepali.com/english-to-nepali-meaning-{word}'    
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html.parser')
    
    nepali_equivalent = soup.find('div', {'class': 'align_text2'}).string

    return nepali_equivalent


if __name__ == '__main__':
    nepali_word = get_nepali_word(english_word)
    print(nepali_word)