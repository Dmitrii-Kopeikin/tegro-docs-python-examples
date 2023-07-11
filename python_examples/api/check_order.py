import hashlib
import hmac
import json
import requests
import time


api_key = 'EEFA1913EA9D9351469B1E5D852A'

data = {
    'shop_id': '1913EA9D9351469B1E5D852A',
    'nonce': time.time_ns(),
    'order_id': 11,
    #  or
    # 'payment_id': 'test order',
}

body = json.dumps(data)
sign = hmac.new(api_key.encode(),
                msg=body.encode(),
                digestmod=hashlib.sha256).hexdigest()

url = 'https://tegro.money/api/order/'
headers = {
    'Authorization': f'Bearer {sign}',
    'Content-Type': 'application/json'
}

response = requests.post(
    url=url,
    data=body,
    headers=headers,
)
