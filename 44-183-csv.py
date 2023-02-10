import csv
from pathlib import Path

with open('my_file.csv', 'w') as fil:
    writ = csv.writer(fil)
    writ.writerow([100, 'aaa', 111])
    writ.writerow([200, 'bbb', 222])
    writ.writerow([300, 'ccc', 333])

with open('my_file.csv') as fil:
    re = csv.reader(fil)
    print(re)
    for line in re:
        print(line)

# Удаляет файл:
Path('my_file.csv').unlink()
