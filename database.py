import clickhouse_connect
from dotenv import load_dotenv
import os

load_dotenv()

client = clickhouse_connect.get_client(
    host='x2ar8i584r.europe-west4.gcp.clickhouse.cloud',
    port=8443,  
    username='default',
    password=os.getenv('PSWD'))

#a = client.command("SELECT * from document") # команд - выборка

#client.query("INSERT INTO document VALUES ('pop1', 'lol1')") # куери - очередь 