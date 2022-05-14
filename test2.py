import shutil

import requests

url = "https://autoscan-sky.com/content/cni/generate_preview.php"

payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"effect\"\r\n\r\n10 \r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"lastname\"\r\n\r\ncarte \r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"firstname\"\r\n\r\ntoto\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"gender\"\r\n\r\nHomme \r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"tall\"\r\n\r\n126\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"birthdate\"\r\n\r\n06/04/1996\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"birthcity\"\r\n\r\nParis \r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"address\"\r\n\r\n1 rue 4 \r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"address_city\"\r\n\r\nParis \r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"address_zipcode\"\r\n\r\n75001 \r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"prefecture\"\r\n\r\nParis \r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"prefecture_department\"\r\n\r\n75 \r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"deliverydate\"\r\n\r\n04/01/2004\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'cache-control': "no-cache",

    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
uid = response.text.split("?")[1].split("=")[1].split(" ")[0][:-1]
print(uid)
print(url)
url = "https://autoscan-sky.com/content/cni/preview.php"

querystring = {"uid": uid}

payload = ""
headers = {
    'cache-control': "no-cache",
}

r = requests.request("GET", url, data=payload, headers=headers, params=querystring)
open('google.ico', 'wb').write(r.content)



