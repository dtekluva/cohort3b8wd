import requests

# data = requests.get('http://api.openweathermap.org/data/2.5/forecast?id=7871736&APPID={464764ac7f27fe2ccfa5c6812955f41a}')

# if data.ok:
#     print('Time\t\t\tweather\t\t\ttemp (C)\t\twind-speed\t\tfeels-like')

#     for item in data.json()['list']:
#         print(item['dt_txt'], '\t', item['weather'][0]['description'], '\t\t', item['main']['temp'], 'C\t\t', item['wind']['speed'], 'km/h\t\t', item['main']['feels_like'], 'C')
# else:
#     print('Error from api server')
#     print('Status: ', data.status_code)
#     print('Message: ', data.json()['message'])

response =requests.get("http://api.openweathermap.org/data/2.5/forecast?id=7871736&APPID=336b102582e7d317c464efd5e6ac86aa")
# print(response.text)

target_v = response.json()["list"]
for entry in target_v:
    data = entry["dt_txt"]
    print(data,entry["weather"][0]["description"])
    print(data,entry["wind"]["speed"])