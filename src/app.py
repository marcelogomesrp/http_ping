import requests
from bs4 import BeautifulSoup
from datetime import datetime
import sys


from utils.eprint import eprint


def main() -> None:
    print(sys.argv)
    now = datetime.now()
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        url = 'https://www.uol.com.br'
    try:
        html_text = requests.get(url).text
        print(f'{now} - Access right {url}')
    except:
        eprint(f'{now} - Error to access {url}')


if __name__ == '__main__':
    main()