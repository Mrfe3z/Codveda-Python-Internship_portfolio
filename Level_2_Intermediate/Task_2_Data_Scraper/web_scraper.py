import requests
from bs4 import BeautifulSoup
import pprint
import csv


all_quotes = []
page = 1

url = 'https://quotes.toscrape.com'
while True:
    print(f'page {page}: Scraping')
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')
    # print(soup.prettify())

    quotes_block = soup.find_all('div', class_='quote')
    for blocks in quotes_block:
        quote = blocks.find('span', class_='text')
        author = blocks.find('small', class_='author')

        # print(f'the quote {quote.text} was said by \n\t\t\t{author.text}')
        all_quotes.append([quote.text, author.text])

    next_button = soup.find('li', class_='next')
    if next_button:
        page_num = next_button.find('a')['href']

        url = 'https://quotes.toscrape.com' + page_num
        page += 1

    else:
        print("No more pages left. Scraping complete!")
        break

with open('output.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(all_quotes)
