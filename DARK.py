#!/usr/bin/python3

from ban import *
from Requests.Request_dork import req_google_dork
from Requests.Request_tracks import *
from Requests.subdomain import *
import sys
import os
# know system is

def loding():
    import sys
    import time

    def spinning_cursor():
        while True:
            for cursor in '|/-\\':
                yield cursor


    spinner = spinning_cursor()
    for _ in range(15):
        sys.stdout.write(next(spinner))
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write('\b')


def DARK():
    sys_info = sys.platform
    if sys_info == 'linux':
        os.system('clear')
    else:
        os.system('cls')
    # banner
    BAN_DARK()
    # choose number
    chos = int(input(f'[{Fore.MAGENTA}*{Fore.WHITE}] Choose number :'))
    if chos == 99 :
        print('\nGood bye ...')
        exit()

    # domain like ---> google.com
    url_web = input(f'[{Fore.MAGENTA}*{Fore.WHITE}] ENTER DOMINE WEB :')


    loding()

    if chos == 1:
         req_google_dork(url_web)

    elif chos == 2:

        if sys_info == 'linux':
            os.system('clear')
        else:
            os.system('cls')

        BAN_TRACKS()
        y0n = int(input(f'[{Fore.MAGENTA}*{Fore.WHITE}] Choose number :'))
        if y0n == 99 :
            DARK()
        http_https = int(input(f'[{Fore.BLUE}1{Fore.WHITE}] HTTP OR [{Fore.RED}2{Fore.WHITE}] HTTPS :'))
        loding()
        if y0n == 1:
            PHP(url_web, http_https)

        elif y0n == 2:
            HTML(url_web, http_https)

        elif y0n == 3:
            WORD_PREES(url_web, http_https)

        elif y0n == 4:
            file_for_tracks = input(f'[{Fore.MAGENTA}*{Fore.WHITE}] Enter name file :')
            OTHER(url_web, http_https, file_for_tracks)



    elif chos == 3 :
        loding()
        os.system('clear')
        BAN_SUBDOMIN()

        choose = int(input(f'[{Fore.MAGENTA}*{Fore.WHITE}] Choose number :'))
        loding()
        if choose == 1 :
            HTTP_HTTPS = int(input(f'[{Fore.BLUE}1{Fore.WHITE}] HTTP or [{Fore.RED}2{Fore.WHITE}] HTTPS :'))
            FILE = open('Requests/domains.txt', 'r')
            subdomins(url_web, HTTP_HTTPS, FILE)

        elif choose == 2 :

            HTTP_HTTPS = int(input(f'[{Fore.BLUE}1{Fore.WHITE}] HTTP or [{Fore.RED}2{Fore.WHITE}] HTTPS :'))
            FILE = open(input(f'[{Fore.MAGENTA}*{Fore.WHITE}] Enter name file subdomains :'), 'r')

            subdomins_your_file(url_web, HTTP_HTTPS, FILE)

        elif choose == 99 :
            DARK()

    elif chos == 99 :
        print('Good bye ...')
        exit()

DARK()
