# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

 new_song = my_favorite_songs[1][1] 
 out_song = my_favorite_songs[3][1]
 nowhere_song = my_favorite_songs[8][1]
 summa_songs = new_song + out_song + nowhere_song
 print('Три песни звучат -', summa_songs, 'минут')

# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}
 waste_song = my_favorite_songs_dict['Waste a Moment']
 easy_song = my_favorite_songs_dict['Easy']
 beautiful_song = my_favorite_songs_dict['Beautiful Day']
 summa_songs = waste_song + easy_song + beautiful_song
 print('Три песни звучат -', summa_songs, 'минут')



# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random

import random
print(random.sample(my_favorite_songs, 3))


# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime


import datetime
def convert_time(minutes, seconds):
    time_format = datetime.timedelta(minutes=minutes, seconds=seconds)
    return str(time_format)
for song, timing in my_favorite_songs_dict.items():
    minutes = int(timing)
    seconds = int((timing - minutes) * 60)
    time_format = convert_time(minutes, seconds)
    print(song + ": " + time_format)



