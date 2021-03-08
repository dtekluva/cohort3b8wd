import requests
key = '336b102582e7d317c464efd5e6ac86aa'

import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


session = requests.Session()
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)

ent = int(input("Enter city ID ~>: "))

 

fv = session.get(f'http://api.openweathermap.org/data/2.5/forecast?id={ent}&APPID=336b102582e7d317c464efd5e6ac86aa')



final_json = fv.json()
formated = final_json['list']


print('Time', '\t''\t''\t' 'weather' '\t''\t''temp(C)' '\t''\t' 'wind-speed' '\t' 'feels-like')
for i in formated:
    
    print(f"{i['dt_txt']}" '\t' f"{i['weather'][0]['description']}" '\t'  f"{i['main']['temp']} C" '\t''\t' f"{i['wind']['speed']}km/h" '\t'f"{i['main']['feels_like']} C")