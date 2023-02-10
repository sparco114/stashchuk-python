from datetime import date, time, datetime, timedelta
import time as time_modul

print('---date---')
da = date(2020, 12, 30)
print(da)
print(da.isocalendar())
print(date.today())

print('---time---')
ti = time(17, 32, 55)
print(ti)
print(ti.minute)

print('---datetime---')
dt = datetime(2022, 4, 30, 12, 23, 54)
print(dt)
print(dt.isoformat())
print(datetime.today())
print(datetime.now())
print(datetime.today().microsecond)

tod = datetime.today()
print(tod)
print(tod.strftime('%d.%m.%Y %H:%M:%S'))
print(tod.strftime('%d.%b.%Y %H:%M:%S'))


free_date = '10/12/2023'
# конвертация формата даты из указанного во втором аргументе в стандартный вид:
converted_date = datetime.strptime(free_date, '%d/%m/%Y')
print(converted_date)


print('---timedelta---')
tod1 = datetime.today()
print(tod1)
print(tod1 + timedelta(days=30))
print(tod1 - timedelta(hours=2.5))

# print('---time_modul---')
#
# # Дата начала unix эпохи - 01/01/1970
# start_time = time_modul.time()
# print(start_time)
#
# # остановка работы программы на 2 секунды:
# time_modul.sleep(2)
#
# end_time = time_modul.time()
# print(end_time)
#
# print(end_time - start_time)

print('---time_modul--testspeed---')
start = time_modul.time()

for i in range(1000000):
    print(i)

end = time_modul.time()
print('Total time of work: ', end - start)
