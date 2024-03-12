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

for row in full_links[:100]:
    bb = extract_text_from_pdf_url(row)
    client.query(f"INSERT INTO document VALUES ({id}, '{bb}', '{row}')")
    id += 1
