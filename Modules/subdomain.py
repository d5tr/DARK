#!/usr/bin/env python

import requests
import time
from Core.Colors import *



class Subdomains :

    def __init__(self, Target, Http_Https, File):

        self.Target = Target
        self.Http_Https = Http_Https
        self.File = File



    def subdomins(self):

        filez = self.File.readlines()

        for filex in filez:
            filex = str(filex).strip()




            if self.Http_Https == 1:
                urls = 'http://'+filex+'.'+self.Target

                try:

                    req = requests.get(urls).status_code
                    req2 = requests.post(urls).status_code


                    if req or req2 == 200 :
                        print(f'[{Green}+{White}] Found Url >>>',urls)

                    elif req or req2 == 429:
                        print(f'[{Red}!{Red}!{White}] Have Band !! ')

                    else:
                        print(f'[{Red}-{White}] Not Found !!')

                except requests.exceptions.ConnectionError:
                    print(f'[{Red}-{White}] Not Found !!')
                    pass



            elif self.Http_Https == 2:
                urls = 'https://'+filex+'.'+self.Target

                try:

                    req = requests.get(urls).status_code
                    req2 = requests.post(urls).status_code


                    if req or req2 == 200 :
                        print(f'[{Green}+{White}] Found Url >>>',urls)

                    elif req or req2 == 429:
                        print(f'[{Red}!{Red}!{White}] Have Band !! ')

                    else:
                        print(f'[{Red}-{White}] Not Found !!')

                except requests.exceptions.ConnectionError:
                    print(f'[{Red}-{White}] Not Found !!')
                    pass

    def subdomins_your_file(self):


        filez = self.File.readlines()

        for filex in filez:
            filex = str(filex).strip()




            if self.Http_Https == 1:
                urls = 'http://'+filex+'.'+self.Target

                try:

                    req = requests.get(urls).status_code
                    req2 = requests.post(urls).status_code


                    if req or req2 == 200 :
                        print(f'[{Green}+{White}] Found Url >>>',urls)

                    elif req or req2 == 429:
                        print(f'[{Red}!{Red}!{White}] Have Band !! ')

                    else:
                        print(f'[{Red}-{White}] Not Found !!')

                except requests.exceptions.ConnectionError:
                    print(f'[{Red}-{White}] Not Found !!')
                    pass



            elif self.Http_Https == 2:
                urls = 'https://'+filex+'.'+self.Target

                try:

                    req = requests.get(urls).status_code
                    req2 = requests.post(urls).status_code


                    if req or req2 == 200 :
                        print(f'[{Green}+{White}] Found Url >>>',urls)

                    elif req or req2 == 429:
                        print(f'[{Red}!{Red}!{White}] Have Band !! ')

                    else:
                        print(f'[{Red}-{White}] Not Found !!')

                except requests.exceptions.ConnectionError:
                    print(f'[{Red}-{White}] Not Found !!')
                    pass
