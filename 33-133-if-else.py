# def route_info(dic):
#     if dic.get('distance'):
#         return f"Distance to destination is {dic['distance']}"
#     if dic.get('speed') and dic.get('time'):
#         if isinstance(dic['speed'], int) and isinstance(dic['time'], int):
#             print(type(dic['speed']))
#             return f"Distance to destination is {dic['speed'] * dic['time']}"
#     return "No distance info is availible"
#
#
# dic1 = {
#     'time': 3,
#     'speed': 21,
#     # 'distance': 80,
# }
#
# print(route_info(dic1))

# ---------------------------------------------------------------------------------------------------------------------
def route_info(dic):
    if dic.get('distance'):
        return f"Distance to destination is {dic['distance']}"
    if dic.get('speed') and dic.get('time') and isinstance(dic['speed'], int) and isinstance(dic['time'], int):
        return f"Distance to destination is {dic['speed'] * dic['time']}"
    return "No distance info is available"


dic1 = {
    'time': 3,
    'speed': 21,
    # 'distance': 80,
}
print(route_info(dic1))
