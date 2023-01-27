def image_info(di):
    if ('image_id' not in di) and ('image_title' not in di):
        raise AttributeError('Нет данных')
    elif 'image_title' not in di:
        raise AttributeError('Не указано наименование')
    elif 'image_id' not in di:
        raise AttributeError('Не указан ID')
    print(f"Image {di['image_title']} has id {di['image_id']}. Result {10 / 2}")


dic1 = {'image_id': 11111, 'image_title': 'MY CAT'}

try:
    image_info(dic1)
except AttributeError as e:
    print(e)
except Exception as e:
    print(Exception)
    print(e)
finally:
    print('Final')

print('THE END')
