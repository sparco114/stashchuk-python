import json

js1 = '{"xxx": 100, "yyy": 200, "zzz": 300}'
js11 = '[1, 7, 4]'
print('js11:', js11)
print('type js11:', type(js11))

to_lis = json.loads(js11)

print('lis:', to_lis)
print('lis type:', type(to_lis))

print("-------Ex 1-------")
dic1 = {
    'one': True,
    'two': None,
    'Three': 3.5535135,
    'Four': 'xxx',
    'Five': 707,
    500: False,
    'six': [1, 2, 5],
    'seven': (5, 7, 9),
    'eight': {777: 'str', True: 555}
}
print(dic1)
print(type(dic1))

js2 = json.dumps(dic1)
print(js2)
print(type(js2))
