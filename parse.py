import requests
from bs4 import BeautifulSoup
#Функция собирающая url с сайта Банка Росси
def parse_from_main_page(url):
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html, 'html.parser')
    document_links = []
    for div_tag in soup.find_all('div', class_='title'):
        a_tag = div_tag.find('a', href=True)
        if a_tag:
            document_link = a_tag['href']
            document_links.append(document_link)
    return document_links
document_links = parse_from_main_page(url = 'http://cbr.ru/na/')
base_url = 'http://cbr.ru'
# Получаем массив ссылок с главной страницы
full_links = [base_url + link for link in document_links]
# print(full_links)




all_full_links =[]
def process_link(url):
    if '/Crosscut/LawActs/File/' in url:
        all_full_links.append(f"http://cbr.ru{url}")
    elif '/Queries/UniDbQuery/File/' in url:
        all_full_links.append(f"http://cbr.ru{url}")
    else:
        all_full_links.append (url)

# Функция для выполнения AJAX-запроса и извлечения ссылок на документы
def fetch_documents(page):
    ajax_url = f"{base_url}&Page={page}"
    response = session.get(ajax_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        document_links = soup.find_all('a', href=True)
        for link in document_links:
            # Используем функцию process_link для обработки каждой ссылки
            process_link(link['href'])

# Базовый URL и сессия остаются без изменений
base_url = 'http://cbr.ru/Crosscut/LawActs/Page/94917?Date.Time=Any'
session = requests.Session()

cpages = 7  # Кол-во страниц
for page in range(1, cpages + 1):
    fetch_documents(page)

full_links.extend(all_full_links)
#Итого получаем 2976 ссылок на документы
print(full_links[53:56])
