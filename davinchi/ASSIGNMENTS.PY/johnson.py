################ Bubble sort

original_list = [3,5,1,2,8,10,0]

list_copy = original_list.copy() # make a temporary list
sorted = False  # Assume list is not sorted at first to kick-start the while loop
count = 0
while not sorted: 
    sorted = True # (1) Assume that it's sorted
    for i in range(0, len(list_copy) - 1): # (2) len(l)-1 because the last element                                          
                                    # has no thing on the right to compare to.
        if list_copy[i] > list_copy[i + 1]: # (2) check condition
            sorted = False  # (3) 
            count += 1
            list_copy[i], list_copy[i + 1] = list_copy[i + 1], list_copy[i] # (2) swap

print("Original: {}".format(original_list)) # (4)
print("Sorted: {}".format(list_copy))
print("Number of swaps: {}".format(count))



################## CSV DICTIONARY

import csv

data = {
    'name': ["ade","john","shade"],
    'age': [23,21,24],
    'gender': ["male","male","female"]
}

with open('people.csv') as csv_file:
    reader = csv.DictReader(csv_file)

    for row in reader:
        data['name'].append(row['name'])
        data['age'].append(row['age'])
        data['gender'].append(row['gender'])

print(data)


###################   REQUEST

import requests

data = requests.get('http://api.openweathermap.org/data/2.5/forecast?id=7871736&APPID={464764ac7f27fe2ccfa5c6812955f41a}')

if data.ok:
    print('Time\t\t\tweather\t\t\ttemp (C)\t\twind-speed\t\tfeels-like')

    for item in data.json()['list']:
        print(item['dt_txt'], '\t', item['weather'][0]['description'], '\t\t', item['main']['temp'], 'C\t\t', item['wind']['speed'], 'km/h\t\t', item['main']['feels_like'], 'C')
else:
    print('Error from api server')
    print('Status: ', data.status_code)
    print('Message: ', data.json()['message'])

response =requests.get("http://api.openweathermap.org/data/2.5/forecast?id=7871736&APPID=336b102582e7d317c464efd5e6ac86aa")
print(response.text)