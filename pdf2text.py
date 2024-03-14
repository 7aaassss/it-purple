import requests
import pdfplumber
import io



def extract_text_from_pdf_url(url): # функция для конвертации пдф файлов в текст
    response = requests.get(url) # запрос по ссылке 
    final_text= ''
    pages= {}
    success = True # флаг (в дальнейшем для добавления файла в бд)
    if response.status_code == 200:
        with io.BytesIO(response.content) as f: # битовойе открытие файла
            try:
                with pdfplumber.open(f) as pdf:
                    for page_num, page in enumerate(pdf.pages):
                        text = page.extract_text()
                        #print("Страница", page_num + 1)
                        if text:
                        # print(text)
                            final_text+=text # конкантенация текста со всех страниц
                            pages.setdefault(page_num + 1, text) #дополнительны словарь вида (страница : текст страницы)
            except Exception as e:
                print(e)
                success = False  # Операция не удалась
    else:
        success = False  # Ответ сервера не 200
    return final_text, success, pages
