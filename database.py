import clickhouse_connect
from dotenv import load_dotenv
import os
from pdf2text import extract_text_from_pdf_url
from parse import full_links
load_dotenv()

client = clickhouse_connect.get_client(
    host='x2ar8i584r.europe-west4.gcp.clickhouse.cloud',
    port=8443,  
    username='default',
    password=os.getenv('PSWD')
    )

#a = client.command("SELECT * from document") # команд - выборка

id = 0

#bb = extract_text_from_pdf_url(full_links[2])
#client.query(f"INSERT INTO document VALUES ({id}, '{bb}', '{full_links[2]}')") # куери - очередь
failed_urls =[]
for row in full_links:
    text, success, pages = extract_text_from_pdf_url(row)
    if success:
        try:
            if text[0] == '\n':
                continue
            else:
                client.query(f"INSERT INTO document VALUES ({id}, '{text}', '{row}')")
                num_p = 1
                for page in pages:
                    client.query(f"INSERT INTO dc_with_pages VALUES ({id}, '{pages[page]}', '{num_p}')")
                    num_p += 1
                id += 1
        except Exception as e:
            print(f"Ошибка при вставке {[id,row]} в БД: {e}")
    else:
        failed_urls.append(row)
