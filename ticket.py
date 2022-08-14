import requests
import user_agent
import uuid
import binascii
import os
import random


import string
import pystyle
from pystyle import *
from random import choice
import threading
import json
menu = """

░██████╗░██╗░░░██╗██╗██╗░░░░░██████╗░███████╗██████╗░░░░░██████╗░░██████╗░  ░██████╗░███████╗███╗░░██╗
██╔════╝░██║░░░██║██║██║░░░░░██╔══██╗██╔════╝██╔══██╗░░░██╔════╝░██╔════╝░  ██╔════╝░██╔════╝████╗░██║
██║░░██╗░██║░░░██║██║██║░░░░░██║░░██║█████╗░░██║░░██║░░░██║░░██╗░██║░░██╗░  ██║░░██╗░█████╗░░██╔██╗██║
██║░░╚██╗██║░░░██║██║██║░░░░░██║░░██║██╔══╝░░██║░░██║░░░██║░░╚██╗██║░░╚██╗  ██║░░╚██╗██╔══╝░░██║╚████║
╚██████╔╝╚██████╔╝██║███████╗██████╔╝███████╗██████╔╝██╗╚██████╔╝╚██████╔╝  ╚██████╔╝███████╗██║░╚███║
░╚═════╝░░╚═════╝░╚═╝╚══════╝╚═════╝░╚══════╝╚═════╝░╚═╝░╚═════╝░░╚═════╝░  ░╚═════╝░╚══════╝╚═╝░░╚══╝




"""




print(Colorate.Horizontal(Colors.red_to_blue, menu))
threads = int(input(Colorate.Horizontal(Colors.red_to_blue, "threads: ")))
Serverinv = input(Colorate.Horizontal(Colors.red_to_blue, "Server invite (example: kKJGqywC ): "))
os.system('title guilded.gg gen / made by xman#111 discord.gg/lead')
def gen():
    config=json.load(open("config.json", "r"))
    proxystate = config['proxys']
    global invite
    global requests
    global proxies
    while True:
        if proxystate == "socks5":
            
            with open("proxiess.txt", "r") as f:
                            proxy1 = choice(f.readlines()).strip()
                            proxies = {'https': f'socks5://RnePIknYGEb:cceFUgMQQIu@{proxy1}:1080'}
        elif proxystate == "none":
             proxies = {'https': None}
        else:
            
            with open("proxiess.txt", "r") as f:
                            proxy1 = choice(f.readlines()).strip()
                            proxies = {'https': f'http://{proxy1}'}
        
        f = "".join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=3))
        user = f'xman{f}@xman.com'
        username = f'xman{f}'
        try:

            headers = {
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Accept-Encoding':'gzip, deflate, br',
                'Accept-Language': 'en-US,en;q=0.9',
                'Connection': 'keep-alive',
                'Content-Length':'18',
                'Content-Type': 'application/json',
                'Cookie': f'hmac_signed_session={cooike}',
                'guilded-client-id': 'e3de13f3-6361-4db3-8dd5-1970c8e3c6f6',
                'guilded-viewer-platform': 'desktop',
                'Host':'www.guilded.gg',
                'Origin': 'https://www.guilded.gg',
                'Referer': f'https://www.guilded.gg/i/{Serverinv}',
                'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'User-Agent': user_agent.generate_user_agent(),
                'X-Requested-With': 'XMLHttpRequest',
            }


            data = {
                'type': '"consume"'
            }

        

            r = requests.put(f'https://www.guilded.gg/api/invites/{Serverinv}', headers=headers, json=data,proxies=proxies)
        except Exception:
            pass


        headers = {
                                'authority': 'www.guilded.gg',
                                'method': 'POST',
                                'path': '/api/users?type=email',
                                'scheme': 'https',
                                'accept': 'application/json, text/javascript, */*; q=0.01',
                                'accept-encoding': 'gzip, deflate, br',
                                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                                'content-type': 'application/json',
                                'guilded-client-id': f'{uuid.uuid1()}',
                                'guilded-device-id': str(binascii.b2a_hex(os.urandom(64)).decode('utf-8')),
                                'guilded-device-type': 'desktop',
                                'guilded-stag': 'c4740afd3f3e4d63d365d826139de166',
                                'origin': 'https://www.guilded.gg',
                                'referer': 'https://www.guilded.gg/',
                                'sec-fetch-dest': 'empty',
                                'sec-fetch-mode': 'cors',
                                'sec-fetch-site': 'same-origin',
                                'user-agent': user_agent.generate_user_agent(),
                                'x-requested-with': 'XMLHttpRequest',
                                'dnt': '1',
                                "Sec-Ch-Ua": '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
                                "Sec-Ch-Ua-Mobile": '?0',
                                "Sec-Ch-Ua-Platform": "macOS",
                    }



        pay = {
                            "email": user,
                            "extraInfo": {"platform": "desktop"},
                            "fullName": f"xman{f}",
                            "name": f'xman{f}',
                            "password": 'xman#1111'}
        try:
         r = requests.post('https://www.guilded.gg/api/users?type=email', headers=headers, json=pay, proxies=proxies)
         if 'banned' in r.text:
            print(Colorate.Horizontal(Colors.red_to_blue,f'[/] Proxy: {proxies} was banned from guilded.gg'))
         
        except requests.exceptions.ConnectionError:
            pass
        try:
         cooike = r.cookies['hmac_signed_session']
         print(Colorate.Horizontal(Colors.red_to_blue,f'[/] Account with the username: xman{f} was created!'))
        except Exception:
            
            pass
        import requests

        try:

            headers = {
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Accept-Encoding':'gzip, deflate, br',
                'Accept-Language': 'en-US,en;q=0.9',
                'Connection': 'keep-alive',
                'Content-Length':'18',
                'Content-Type': 'application/json',
                'Cookie': f'hmac_signed_session={cooike}',
                'guilded-client-id': 'e3de13f3-6361-4db3-8dd5-1970c8e3c6f6',
                'guilded-viewer-platform': 'desktop',
                'Host':'www.guilded.gg',
                'Origin': 'https://www.guilded.gg',
                'Referer': f'https://www.guilded.gg/i/{Serverinv}',
                'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'User-Agent': user_agent.generate_user_agent(),
                'X-Requested-With': 'XMLHttpRequest',
            }


            data = {
                'type': '"consume"'
            }

        

            r = requests.put(f'https://www.guilded.gg/api/invites/{Serverinv}', headers=headers, json=data,proxies=proxies)
            
            if r.status_code == 200:
                print(Colorate.Horizontal(Colors.red_to_blue,f'[/] Joined Sever'))
            else:
                print(Colorate.Horizontal(Colors.red_to_blue,f'[/] Could not join server'))

        except Exception:
            pass



while True:
 if threading.active_count() < int(threads):
            threading.Thread(target=gen).start()     
     
    
    



