import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException

# Функция собирающая url с сайта Банка России
def parse_from_main_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            html = response.content
            soup = BeautifulSoup(html, 'html.parser')
            document_links = []
            for div_tag in soup.find_all('div', class_='title'):
                a_tag = div_tag.find('a', href=True)
                if a_tag:
                    document_link = a_tag['href']
                    document_links.append(document_link)
            return document_links
        else:
            print(f"Ошибка при запросе к {url}: статус {response.status_code}")
            return []
    except RequestException as e:
        print(f"Ошибка при подключении к {url}: {e}")
        return []

base_url = 'http://cbr.ru/Crosscut/LawActs/Page/94917?Date.Time=Any'
document_links = parse_from_main_page(url='https://www.cbr.ru/na')
# Получаем массив ссылок с главной страницы
full_links = [base_url + link for link in document_links if link.startswith('/')]

all_full_links = []

def process_link(url):
    if '/Crosscut/LawActs/File/' in url or '/Queries/UniDbQuery/File/' in url:
        all_full_links.append(f"http://cbr.ru{url}")
    else:
        all_full_links.append(url)

session = requests.Session()

# Функция для выполнения AJAX-запроса и извлечения ссылок на документы
def fetch_documents(page):
    ajax_url = f"{base_url}&Page={page}"
    try:
        response = session.get(ajax_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            document_links = soup.find_all('a', href=True)
            for link in document_links:
                process_link(link['href'])
        else:
            print(f"Ошибка при запросе к {ajax_url}: статус {response.status_code}")
    except RequestException as e:
        print(f"Ошибка при подключении к {ajax_url}: {e}")

# Допустим, мы знаем количество страниц. Примерный код, количество страниц может быть другим.
cpages = 296  # Количество страниц
for page in range(1, cpages + 1):
    fetch_documents(page)

full_links.extend(all_full_links)
# Выводим количество полученных ссылок
print(f"Всего получено ссылок: {len(full_links)}")
