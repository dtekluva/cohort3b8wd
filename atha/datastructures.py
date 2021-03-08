# # LIST SLICING

# my_list = list(range(21))
# print(my_list)
# print(my_list[2])

# # slice from 0-4

# my_slice = my_list[0:5]
# print(my_slice)

# # slice from 5 - 15

# my_slice= my_list[5:16]
# print(my_slice)
# # slice with interval
# # slice takes [start:stop:step]

# my_slice = my_list[1:19:2]
# print(my_slice)

# [ade, jonah, seun] = [23, 45, 66]
# print(ade)
# print(jonah)

# len min and max builtin functions
# my_list = ["ade", "kunle", "salami", "sobayo", "richard"]
# x = len(my_list)
# print(x)
# x = min(my_list)
# print(x)
# x = max(my_list)
# print(x)

# # print(['foo', 'bar', 'baz', 'qux', 'quux', 'corge'][2])
# x = ['a', ['bb', ['ccc', 'ddd'], 'ee', 'ff'], 'g', ['hh', 'ii'], 'j']
# # print(len(x))
# # for i in x:
# #     print(i)

# # print(x[1][1][0]) # deep indexing for a nested list 

# # altering list values

# # 1. alter a single list item

# x[2] = [2,3,4,"as"] # this will replace g in our list with the list on the left hand side
# print(x)

# x[2:4] = [1,2,3,4]
# print(x)

# # TUPLES PACKING AND UNPACKING

# my_tup = (1,2,3,4,5)

# x,y,z,a,b, = (1,2,3,4,5)
# print(z)
# index_4 =my_tup.index(4)

# four = my_tup[index_4]

# print(four)



# print(18%7)

# REQUESTS MODULE

import requests

# response = requests.get("https://api.jsonbin.io/b/60365ddaab68b51aec23336b/1")
# data = response.content # raw data from requests
# # print(data["name"])


# dict_response = response.json()# returns a dictionary which is accessible
# print(dict_response["name"])
# print(dict_response)

# response = requests.get("https://www.jumia.com.ng/")
# data = response.content # raw data from requests
# print(data)
# # data = response.json() # Fails because the jumia website returns a html data not a dictionary


# import citylist
# import requests
# import time
# import datetime

# cities = citylist.citylist

# requested_city = input("Please enter city to check \n: ").lower()

# for city in cities:
#     if requested_city in city["name"].lower() :
#         print(city["name"], city["country"])

# requested_country = input("Please enter country code \n: ").lower()

# for city in cities:
#     if requested_city in city["name"].lower() and  requested_country.lower() == city["country"].lower():
#         print(city["name"], city["country"], city["id"])
#         city_id = city["id"]
#         break

# api_key = "336b102582e7d317c464efd5e6ac86aa"

# response = requests.get(f" http://api.openweathermap.org/data/2.5/forecast?id={city_id}&APPID={api_key}")

# data = response.json()

# for forecast in data["list"]:
#     print(forecast["dt_txt"])
#     print(forecast["main"]["temp"])
#     print(forecast["weather"][0]["description"])
#     print()
# print(data.keys())

api_key = "336b102582e7d317c464efd5e6ac86aa"

response = requests.get(f"http://api.openweathermap.org/data/2.5/forecast?id=7871736&APPID=336b102582e7d317c464efd5e6ac86aa")

print(response.json(), file = open("request_data.txt", "w"))