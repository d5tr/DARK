from ban import *
from Requests.Request_dork import req_google_dork
from Requests.Request_tracks import *
import sys
import os
# know system is
sys_info = sys.platform
if sys_info == 'linux':
    os.system('clear')
else:
    os.system('cls')
# banner
BAN_DORK()
# choose number
chos = int(input(f'[{Fore.MAGENTA}*{Fore.WHITE}] Choose number :'))
# domain like ---> google.com
url_web = input(f'[{Fore.MAGENTA}*{Fore.WHITE}] ENTER YOU DOMINE :')


if chos == 1:
     req_google_dork(url_web)

elif chos == 2:
    if sys_info == 'linux':
        os.system('clear')
    else:
        os.system('cls')

    BAN_TRACKS()
    y0n = int(input(f'[{Fore.MAGENTA}*{Fore.WHITE}] Choose number :'))
    http_https = int(input(f'[{Fore.BLUE}1{Fore.WHITE}] HTTP OR [{Fore.RED}2{Fore.WHITE}] HTTPS :'))
    if y0n == 1:
        PHP(url_web, http_https)

    elif y0n == 2:
        HTML(url_web, http_https)

    elif y0n == 3:
        WORD_PREES(url_web, http_https)

    elif y0n == 4:
        file_for_tracks = input(f'[{Fore.MAGENTA}*{Fore.WHITE}] Enter name file :')
        OTHER(url_web, http_https, file_for_tracks)



