import requests
import pdfplumber
import io

def extract_text_from_pdf_url(url):
    response = requests.get(url)
    final_text= ''
    if response.status_code == 200:
        with io.BytesIO(response.content) as f:
            try: 
                with pdfplumber.open(f) as pdf:
                    for page_num, page in enumerate(pdf.pages):
                        text = page.extract_text()
                        #print("Страница", page_num + 1)
                        if text:
                        # print(text)
                            final_text+=text
            except Exception as e:
                print(e)
    return final_text
