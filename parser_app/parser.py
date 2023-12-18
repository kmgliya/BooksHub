import requests
from bs4 import BeautifulSoup as bs
from django.views.decorators.csrf import csrf_exempt

URL = "https://mybook.ru/"


HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}


# start
@csrf_exempt
def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req


# GET DATA
@csrf_exempt
def get_data(html):
    soup = bs(html, 'html.parser')
    items = soup.find_all('div', class_="e4xwgl-0 iJwsmp")
    mybook = []

    for item in items:
        mybook.append({
            "title_name": item.find('div', class_="e4xwgl-1 gEQwGK").get_text(),
            "title_url": URL + item.find("a").get('href'),
            "title_autor": item.find('div', class_="m4n24q-0 gFPQgy").get_text(),
            "title_url_autor": URL + item.find("a").get('href'),
            #"image": URL + item.find('div', class_="sc-13ocwik-0 idoTYd").find('img').get('src')
        })
    # return mybook
    print(mybook)


#ENDPARSER
@csrf_exempt
def parser_books():
    html = get_html(URL)
    if html.status_code == 200:
        my_book_2 = []
        for page in range(0, 1):
            html = get_html(f'https://mybook.ru/catalog/books', params=page)
            my_book_2.extend(get_data(html.text))
        # return my_book_2
        print(my_book_2)
    else:
        raise Exception("Error in Parse")


parser_books()