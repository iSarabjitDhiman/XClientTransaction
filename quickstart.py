import bs4
import requests
from urllib.parse import urlparse
from x_client_transaction import ClientTransaction
from x_client_transaction.utils import generate_headers, handle_x_migration, get_ondemand_file_url

# INITIALIZE SESSION
session = requests.Session()
session.headers = generate_headers()


# GET HOME PAGE RESPONSE
# required only when hitting twitter.com but not x.com
# returns bs4.BeautifulSoup object
home_page_response = handle_x_migration(session=session)

# for x.com no migration is required, just simply do
home_page = session.get(url="https://x.com/home")
home_page_response = bs4.BeautifulSoup(home_page.content, 'html.parser')


# GET ondemand.s FILE RESPONSE
ondemand_file_url = get_ondemand_file_url(response=home_page_response)
ondemand_file = session.get(url=ondemand_file_url)

# ondemand_file_response = bs4.BeautifulSoup(
#     ondemand_file.content, 'html.parser')
# Getting "Couldn't get KEY_BYTE indices" error? Try passing the original response or the response text
# both should work
# ondemand_file_response = ondemand_file
ondemand_file_response = ondemand_file.text


# X-Client-Transaction-Id Generation

# Example 1
# replace the url and http method as per your use case
url = "https://x.com/i/api/1.1/jot/client_event.json"
method = "POST"
path = urlparse(url=url).path
# path will be /i/api/1.1/jot/client_event.json in this case

# Example 2
user_by_screen_name_url = "https://x.com/i/api/graphql/1VOOyvKkiI3FMmkeDNxM9A/UserByScreenName"
user_by_screen_name_http_method = "GET"
user_by_screen_name_path = urlparse(url=url).path
# path will be /i/api/graphql/1VOOyvKkiI3FMmkeDNxM9A/UserByScreenName in this case


ct = ClientTransaction(home_page_response=home_page_response,
                       ondemand_file_response=ondemand_file_response)
transaction_id = ct.generate_transaction_id(method=method, path=path)
transaction_id_for_user_by_screen_name_endpoint = ct.generate_transaction_id(
    method=user_by_screen_name_http_method, path=user_by_screen_name_path)

print(transaction_id)
print(transaction_id_for_user_by_screen_name_endpoint)
