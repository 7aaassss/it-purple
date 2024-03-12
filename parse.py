import requests
from bs4 import BeautifulSoup

count = 0

# Базовый URL для AJAX-запросов
base_url = 'http://cbr.ru/Crosscut/LawActs/Page/94917?Date.Time=Any'

# Сессия для сохранения куков и заголовков между запросами
session = requests.Session()


# Функция для выполнения AJAX-запроса и извлечения ссылок на документы


a = []
def fetch_documents(page):
    ajax_url = f"{base_url}&Page={page}"
    response = session.get(ajax_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        document_links = soup.find_all('a', href=True)
        for link in document_links:
            if '/Crosscut/LawActs/File/' in link['href']:
                


for i in range(297):
    fetch_documents(i)

print(len(a))