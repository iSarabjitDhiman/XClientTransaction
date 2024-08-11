<h1 align="center">X-Client-Transaction-ID</h1>

<p align="center">
Twitter X-Client-Transaction-Id generator written in python.

> Reference : https://antibot.blog/twitter/

## Usage/Examples

```python
python quickstart.py
```

OR

```python
from x_client_transaction import ClientTransaction

response = None # get twitter home page response (check quickstart.py)
method = "POST"
path = "/1.1/jot/client_event.json"

ct = ClientTransaction(home_page_response=response)
print(ct.generate_transaction_id(method=method, path=path))
print(ct.generate_transaction_id(method="GET", path="/i/api/1.1/hashflags.json"))

```
