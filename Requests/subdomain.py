import requests
import time
from colorama import Fore




def subdomins(target, http_https, file):

    filez = file.readlines()

    for filex in filez:
        filex = str(filex).strip()




        if http_https == 1:
            urls = 'http://'+filex+'.'+target

            try:

                req = requests.get(urls).status_code
                req2 = requests.post(urls).status_code


                if req or req2 == 200 :
                    print(f'[{Fore.GREEN}+{Fore.WHITE}] Found Url >>>',urls)

                elif req or req2 == 429:
                    print(f'[{Fore.RED}!{Fore.YELLOW}!{Fore.WHITE}] Have Band !! ')

                else:
                    print(f'[{Fore.RED}-{Fore.WHITE}] Not Found !!')

            except requests.exceptions.ConnectionError:
                print(f'[{Fore.RED}-{Fore.WHITE}] Not Found !!')
                pass



        elif http_https == 2:
            urls = 'https://'+filex+'.'+target

            try:

                req = requests.get(urls).status_code
                req2 = requests.post(urls).status_code


                if req or req2 == 200 :
                    print(f'[{Fore.GREEN}+{Fore.WHITE}] Found Url >>>',urls)

                elif req or req2 == 429:
                    print(f'[{Fore.RED}!{Fore.YELLOW}!{Fore.WHITE}] Have Band !! ')

                else:
                    print(f'[{Fore.RED}-{Fore.WHITE}] Not Found !!')

            except requests.exceptions.ConnectionError:
                print(f'[{Fore.RED}-{Fore.WHITE}] Not Found !!')
                pass

def subdomins_your_file(target, http_https, file):


    filez = file.readlines()

    for filex in filez:
        filex = str(filex).strip()




        if http_https == 1:
            urls = 'http://'+filex+'.'+target

            try:

                req = requests.get(urls).status_code
                req2 = requests.post(urls).status_code


                if req or req2 == 200 :
                    print(f'[{Fore.GREEN}+{Fore.WHITE}] Found Url >>>',urls)

                elif req or req2 == 429:
                    print(f'[{Fore.RED}!{Fore.YELLOW}!{Fore.WHITE}] Have Band !! ')

                else:
                    print(f'[{Fore.RED}-{Fore.WHITE}] Not Found !!')

            except requests.exceptions.ConnectionError:
                print(f'[{Fore.RED}-{Fore.WHITE}] Not Found !!')
                pass



        elif http_https == 2:
            urls = 'https://'+filex+'.'+target

            try:

                req = requests.get(urls).status_code
                req2 = requests.post(urls).status_code


                if req or req2 == 200 :
                    print(f'[{Fore.GREEN}+{Fore.WHITE}] Found Url >>>',urls)

                elif req or req2 == 429:
                    print(f'[{Fore.RED}!{Fore.YELLOW}!{Fore.WHITE}] Have Band !! ')

                else:
                    print(f'[{Fore.RED}-{Fore.WHITE}] Not Found !!')

            except requests.exceptions.ConnectionError:
                print(f'[{Fore.RED}-{Fore.WHITE}] Not Found !!')
                pass