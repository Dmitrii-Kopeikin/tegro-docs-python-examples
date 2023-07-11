import hashlib
import hmac
import json
import requests
import time


api_key = 'EEFA1913EA9D9351469B1E5D852A'

data = {
    'shop_id': '1913EA9D9351469B1E5D852A',
    'nonce': time.time_ns(),
    "currency": "RUB",
    "amount": 1200,
    "order_id": "test order",
    "payment_system": 5,
    "fields": {
        "email": "user@email.ru",
        "phone": "79111231212"
    },
    "receipt": {
        "items": [
            {
                "name": "test item 1",
                "count": 1,
                "price": 600
            },
            {
                "name": "test item 2",
                "count": 1,
                "price": 600
            }
        ]
    }
}

body = json.dumps(data)
sign = hmac.new(api_key.encode(),
                msg=body.encode(),
                digestmod=hashlib.sha256).hexdigest()

url = "https://tegro.money/api/createOrder/"
headers = {
    'Authorization': f'Bearer {sign}',
    'Content-Type': 'application/json'
}

response = requests.post(
    url=url,
    data=body,
    headers=headers,
)
