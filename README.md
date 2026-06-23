<h1 align="center">X-Client-Transaction-ID</h1>

<p align="center">
Twitter X-Client-Transaction-Id generator written in python.

<p align="center">
<a href="https://choosealicense.com/licenses/mit/"> <img src="https://img.shields.io/badge/License-MIT-green.svg"></a>
<a href="https://www.python.org/"><img src="https://img.shields.io/pypi/pyversions/XClientTransaction"></a>
<a href="https://pypi.org/project/XClientTransaction"> <img src="https://img.shields.io/pypi/v/XClientTransaction"></a>
<a href="https://github.com/iSarabjitDhiman/XClientTransaction/commits"> <img src="https://img.shields.io/github/last-commit/iSarabjitDhiman/XClientTransaction"></a>
<a href="https://pypi.org/project/XClientTransaction/"> <img src="https://img.shields.io/pypi/dd/XClientTransaction"></a>
<a href="https://discord.gg/pHY6CU5Ke4"> <img alt="Discord" src="https://img.shields.io/discord/1149281691479851018?style=flat&logo=discord&logoColor=white"></a>
<a href="https://twitter.com/isarabjitdhiman"> <img src="https://img.shields.io/twitter/follow/iSarabjitDhiman?style=social"></a>

Reference :

- [Twitter Header: Part 1, Deobfuscation](https://antibot.blog/posts/1741552025433)
- [Twitter Header: Part 2, Reverse Engineering](https://antibot.blog/posts/1741552092462)
- [Twitter Header: Part 3, Generating the header](https://antibot.blog/posts/1741552163416)

## Installation

Install XClientTransaction with pip

```python
pip install XClientTransaction -U --no-cache-dir
```

## Usage/Examples

```python
python quickstart.py
```

## Get x.com Home Page and ondemand.s File Response

#### Synchronous Version

```python
import bs4
import requests
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

ondemand_file_response = bs4.BeautifulSoup(ondemand_file.content, 'html.parser')
# Getting "Couldn't get KEY_BYTE indices" error? Try passing the original response or the response text
# both should work
# ondemand_file_response = ondemand_file
ondemand_file_response = ondemand_file.text
```

#### Async Version

```python
import bs4
import httpx
from x_client_transaction.utils import generate_headers, handle_x_migration_async, get_ondemand_file_url

# INITIALIZE SESSION
session = httpx.AsyncClient(headers=generate_headers())


# GET HOME PAGE RESPONSE
# required only when hitting twitter.com but not x.com
# returns bs4.BeautifulSoup object
home_page_response = await handle_x_migration_async(session=session)

# for x.com no migration is required, just simply do
home_page = await session.get(url="https://x.com/home")
home_page_response = bs4.BeautifulSoup(home_page.content, 'html.parser')


# GET ondemand.s FILE RESPONSE
ondemand_file_url = get_ondemand_file_url(response=home_page_response)
ondemand_file = await session.get(url=ondemand_file_url)

ondemand_file_response = bs4.BeautifulSoup(ondemand_file.content, 'html.parser')
# Getting "Couldn't get KEY_BYTE indices" error? Try passing the original response or the response text
# both should work
# ondemand_file_response = ondemand_file
ondemand_file_response = ondemand_file.text
```

## Generate X-Client-Transaction-Id (tid):

```python
from urllib.parse import urlparse
from x_client_transaction import ClientTransaction


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


ct = ClientTransaction(home_page_response=home_page_response, ondemand_file_response=ondemand_file_response)
transaction_id = ct.generate_transaction_id(method=method, path=path)
transaction_id_for_user_by_screen_name_endpoint = ct.generate_transaction_id(
    method=user_by_screen_name_http_method, path=user_by_screen_name_path)

print(transaction_id)
print(transaction_id_for_user_by_screen_name_endpoint)

```

## Authors

- [@iSarabjitDhiman](https://www.github.com/iSarabjitDhiman)

## Feedback

If you have any feedback, please reach out to us at hello@sarabjitdhiman.com or contact me on Social Media @iSarabjitDhiman

## Support

For support, email hello@sarabjitdhiman.com
