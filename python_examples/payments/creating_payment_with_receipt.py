import hashlib
import requests

from collections import OrderedDict


secret = 'GB%^&*YJni677'

required_data = {
    'shop_id': 'D0F98E7D7742609DC508D86BB7500914',
    'amount': 1600,
    'currency': 'RUB',
    'order_id': '123',
    'test': 1,  # Optional. If present, it's included in the sign.
}
required_data = OrderedDict(sorted(required_data.items()))

string_to_hash = '&'.join(
    [f'{key}={value}' for key, value in sorted(required_data.items())])

sign = hashlib.md5((string_to_hash + secret).encode()).hexdigest()

additional_data = {
    'lang': 'ru',
    'payment_system': 16,
    'success_url': '',
    'fail_url': '',
    'notify_url': '',
    'fields': {
        'email': 'user@email.ru',
        'phone': '79111231212',
    },
    'receipt': {
        'items': [
            {
                'name': 'item 1',
                'count': 2,
                'price': 600,
            },
            {
                'name': 'item 2',
                'count': 1,
                'price': 400,
            }
        ],
    },
}

url = 'https://tegro.money/pay/form/'

response = requests.post(
    url=url,
    data={**required_data, **additional_data},
)

print({**required_data, **additional_data})

print(response.request.headers)