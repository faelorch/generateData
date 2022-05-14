# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
import random
import shutil


import requests
import names
from faker import Faker

url = 'https://autoscan-sky.com/content/cni/generate_preview.php'
url_image = 'https://autoscan-sky.com/content/cni/preview.php?uid='
url_form = 'https://autoscan-sky.com/index.php?page=payment'
g = random.randint(1, 2)
tall = random.randint(100,250)
gender = lambda a: ["Homme", "male"] if (a == 1) else ["Femme", "Female"]
print(gender)
last_name = names.get_last_name()
first_name = names.get_first_name(gender=gender(g)[1])

import time


def str_time_prop(start, end, time_format, prop):

    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(time_format, time.localtime(ptime))


def random_date(start, end, prop):
    return str_time_prop(start, end, '%d/%m/%Y', prop)


print(random_date("1/1/2008", "1/1/2009", random.random()))
birthdate =random_date("01/01/1920", "01/01/2020", random.random())
deliverydate = random_date(birthdate, "01/01/2020", random.random())
fake = Faker('fr_FR')
adress =fake.address()
city = fake.city()
prefecture_department = random.randint(15,80)
address = adress.split("\n")[0]
address_city =adress.split(" ")[-1]
address_zipcode =adress.split("\n")[-1].split(" ")[0]

myobj = {'effect': 10,
         'lastname': last_name,
         'firstname': first_name,
         'gender': gender(g)[0],
         'tall': tall,
         'birthdate': birthdate,
         'birthcity': 'Paris',
         'address': address,
         'address_city': address_city,
         'address_zipcode': address_zipcode,
         'prefecture': city,
         'prefecture_department': prefecture_department,
         'deliverydate': deliverydate}

if __name__ == '__main__':
    response = requests.post(url, data=myobj)
    print(response.text)
    uid = response.text.split("?")[1].split("=")[1].split(" ")[0][:-1]
    print(uid)
    url = url_image + uid
    print(url)
    img = requests.get(url, stream=True)
    with open('img.png', 'wb') as f:
        img.raw.decode_content = True
        shutil.copyfileobj(img.raw, f)
