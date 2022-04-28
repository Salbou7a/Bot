import os; os.system("python3 webserver.py & >/dev/null")
import requests
import time



playload = {

    'content': 'Salbou7a FTW send send' # < < 


}

headerst = {

   'authorization': ''

}

headerst1 = {

    'authorization': ''

}
headerst2 = {

    'authorization': '' # < <   

}

channel = '962331346351571004' # < <  

url = f'https://discord.com/api/v8/channels/{channel}/messages'


while True:
    requests.post(url, data=playload, headers=headerst, )
    requests.post(url, data=playload, headers=headerst1, )
    requests.post(url, data=playload, headers=headerst2, )
    time.sleep(10) # < < كم رساله في الثانيه


