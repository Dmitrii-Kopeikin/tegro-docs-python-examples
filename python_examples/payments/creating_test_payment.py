import hashlib

from collections import OrderedDict


secret = 'GB%^&*YJni677'

required_data = {
    'shop_id': 'D0F98E7D7742609DC508D86BB7500914',
    'amount': 100,
    'currency': 'RUB',
    'order_id': '123',
    'test': 1,
}
required_data = OrderedDict(sorted(required_data.items()))

string_to_hash = '&'.join(
    [f'{key}={value}' for key, value in sorted(required_data.items())])

sign = hashlib.md5((string_to_hash + secret).encode()).hexdigest()
