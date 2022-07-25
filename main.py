# import numpy as np
# import cv2
import requests
from requests import get, post
import json

# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
ll = (162.536137, 56.239683)
x1, y1 = 56.2603, 162.477
# ll = (abs((x1 - x2) / 2), abs((y1 - y2) / 2))
# geo = get(
#     f"https://geocode-maps.yandex.ru/1.x/?apikey=ваш API-ключ&format"+
#     f"=json&geocode={ll[1]},{ll[0]}&bbox={x1},{y1}~{x2},{y2}")
geo = get(
    f"https://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&format=j" +
    f"son&geocode={ll[0]},{ll[1]}&ll={ll[0]},{ll[1]}&spn={(ll[0] - y1)/5},{(x1 - ll[1])/5}&kind=house&results=100").json()
with open('data.json', 'w', encoding='utf8') as outfile:
    json.dump(geo, outfile)
geo = geo["response"][
    "GeoObjectCollection"][
    "featureMember"]
t = []
for g in geo:
    t.append(g["GeoObject"]["Point"]["pos"])
with open('data.json', 'w', encoding='utf8') as outfile:
    json.dump(t, outfile)
img = get(f'https://static-maps.yandex.ru/1.x/?ll={ll[0]},{ll[1]}&spn={(ll[0] - y1)/5},{(x1 - ll[1])/5}&l=map')
with open('data.jpg', 'wb') as outfile:
    outfile.write(img.content)
# fn = "my.jpg"  # путь к файлу с картинкой
# img = cv2.imread(fn)  # загрузка изображения
# arr = []
# min_p = (95, 48, 34)
# max_p = (250, 103, 113)
# # arr = cv2.inRange(img, min_p, max_p)
# for i in img:
#     ar = []
#     for j in i:
#         if 95 < j[0] < 250 and 48 < j[1] < 103 and 34 < j[2] < 113:
#             ar.append(1)
#         else:
#             ar.append(0)
#     arr.append(ar)
# cords_it = []
# cords_prom = []
# for i in range(len(arr) // 10):
#     for j in range(len(arr[0]) // 10):
#         for i1 in range(10):
#             for j1 in range(10):
#                 if arr[10 * i + i1][10 * j + j1] == 1:
#                     cords_prom.append((10 * i + i1, 10 * j + j1))
#         if len(cords_prom) >= 30:
#             cords_it.append(cords_prom[len(cords_prom) // 2])
#         cords_prom = []
#
# print(cords_it)
# cv2.imwrite('Image.jpg', img)
# fn = "my.jpg"  # путь к файлу с картинкой
# img2 = cv2.imread(fn)
# for i in cords_prom:
#     cv2.circle(img2, (i[1], i[0]), 20, (0, 0, 255), -1)
# cv2.imwrite('Image.jpg', img2)
# # print(im)
# # dM01 = moments['m01']
# # dM10 = moments['m10']
# # dArea = moments['m00']
# #
# # if dArea > 100:
# #     x = int(dM10 / dArea)
# #     y = int(dM01 / dArea)
