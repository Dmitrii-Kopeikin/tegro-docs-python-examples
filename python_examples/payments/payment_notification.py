import hashlib

from collections import OrderedDict


post_data = {
    'shop_id': 'D0F98E7D7742609DC508D86BB7500914',
    'amount': 100,
    'order_id': '123',
    'payment_system': 16,
    'currency': 'RUB',
    'sign': 'e13cd755e9b4632d51ae4d5c74c2f122',
}

secret = 'GB%^&*YJni677'

request_sign = post_data['sign']
try:
    post_data.pop('sign')
except KeyError:
    raise Exception('Request is not signed!')

string_to_hash = '&'.join(
    [f'{key}={value}' for key, value in sorted(post_data.items())])

sign = hashlib.md5((string_to_hash + secret).encode()).hexdigest()
