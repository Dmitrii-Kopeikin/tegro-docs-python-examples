import hashlib
import hmac
import json
import requests
import time


api_key = 'EEFA1913EA9D9351469B1E5D852A'

data = {
    'shop_id': '1913EA9D9351469B1E5D852A',
    'nonce': time.time_ns(),
    'currency': 'RUB',
    'account': 'account_number',
    'amount': 1000,
    'payment_id': 'payment_id',
    'payment_system': 16,
}

body = json.dumps(data)
sign = hmac.new(api_key.encode(),
                msg=body.encode(),
                digestmod=hashlib.sha256).hexdigest()

url = 'https://tegro.money/api/createWithdrawal/'
headers = {
    'Authorization': f'Bearer {sign}',
    'Content-Type': 'application/json'
}

response = requests.post(
    url=url,
    data=body,
    headers=headers,
)
