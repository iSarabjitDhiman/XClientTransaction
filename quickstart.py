import requests
from x_client_transaction.utils import handle_x_migration
from x_client_transaction import ClientTransaction

headers = {"Authority": "x.com",
           "Accept-Language": "en-US,en;q=0.9",
           "Cache-Control": "no-cache",
           "Referer": "https://x.com",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
           "X-Twitter-Active-User": "yes",
           "X-Twitter-Client-Language": "en"}

session = requests.Session()
session.headers = headers
response = handle_x_migration(session)

method = "POST"
path = "/1.1/jot/client_event.json"

ct = ClientTransaction(response)
transaction_id = ct.generate_transaction_id(method=method, path=path)

print(transaction_id)
