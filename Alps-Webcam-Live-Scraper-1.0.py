from urllib.request import Request, urlopen
import requests
import datetime
import time
import random

img_count = 1
current_time = ''
img_url = ''
letters = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890'
rsndom = letters[random.randint(0, len(letters) - 1)] + letters[random.randint(0, len(letters) - 1)] + letters[
    random.randint(0, len(letters) - 1)]
print(rsndom)
t = ''

while True:
    # // get date
    last_time = current_time
    current_time = str(datetime.datetime.now())
    current_time = current_time[:current_time.find(' ')]
    if last_time != current_time:
        img_count = 1

    # #    # get image name #
    # req = Request(
    #     'https://www.chamonix.com/webcam-chamonix-brevent-planpraz,138,en.html',
    #     headers={'User-Agent': 'Mozilla/5.0'})  #
    # try:  #
    #     webpage = urlopen(req).read().decode()  #
    # except UnicodeDecodeError:  #
    #     webpage = '\n\n'  #
    #     t = img_url  #
    #     img_url = webpage[webpage.find('http://www.compagniedumontblanc.fr/webcam/'):]  #
    #     img_url = img_url[:img_url.find('"')]  #
    #     print(img_url)
    img_urls = [['A', 'http://www.compagniedumontblanc.fr/webcam/bvt1PPZHD.jpg'],
                ['B', 'http://www.compagniedumontblanc.fr/webcam/flg1sommetindexHD.jpg'],
                ['C', 'http://www.compagniedumontblanc.fr/webcam/FlegereHD.jpg'],
                ['D', 'http://www.compagniedumontblanc.fr/webcam/bvt1A2000HD.jpg']]
    # getting the image and saving it
    for img_url in img_urls:
        print('saving new image ')

        with open(f'{img_url[0]} {current_time} {str(img_count)} {rsndom} .jpg', 'wb') as f:
            f.write(requests.get(img_url[1]).content)
        img_count = img_count + 1
    time.sleep(3600)
