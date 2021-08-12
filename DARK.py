#!/usr/bin/env python

from Core.ban import *
from Core.Loding import *
from Modules.Request_dork import *
from Modules.Request_path import *
from Modules.subdomain import *
from Core.Colors import *
import sys
import os


# know system is



def DARK():
    # OS is ?
    sys_info = sys.platform
    if sys_info == 'linux':
        os.system('clear')
    else:
        os.system('cls')

    # banner
    BAN_DARK()

    # choose number
    chos = int(input(f'[{Purple}*{White}] Choose number :'))
    if chos == 99 :
        print('\nGood bye ...')
        exit()

    # domain like ---> google.com
    url_web = input(f'\n[{Purple}*{White}] ENTER DOMINE WEB :')

    # ....
    loding()

    if chos == 1:
        RGD = DORK(url_web)
        RGD.req_google_dork()

    elif chos == 2:

        if sys_info == 'linux':
            os.system('clear')
        else:
            os.system('cls')

        BAN_TRACKS()
        y0n = int(input(f'[{Purple}*{White}] Choose number :'))
        if y0n == 99 :
            DARK()
        http_https = int(input(f'[{Cyan}1{White}] HTTP OR [{Red}2{White}] HTTPS :'))
        loding()

        if y0n == 1:
           # PHP
            Attack = Tracks(url_web, http_https)
            Attack.PHP()

        elif y0n == 2:
            # HTML
            Attack = Tracks(url_web, http_https)
            Attack.HTML()

        elif y0n == 3:
            # WORD PRESS
            Attack = Tracks(url_web, http_https)
            Attack.WORD_PREES()

        elif y0n == 4 :
            Attack = Tracks(url_web, http_https)
            Attack.Admins()

        elif y0n == 5 :
            Attack = Tracks(url_web, http_https)
            Attack.PHP()
            Attack.HTML()
            Attack.WORD_PREES()
            Attack.Admins()


        elif y0n == 6:
            file_for_tracks = input(f'[{Purple}*{White}] Enter name file :')
            
            Attack = Tracks(url_web, http_https, file_for_tracks)
            Attack.OTHER()
        
        else :
            print(f'{Red} Error number !! {White}')
            DARK()



    elif chos == 3 :
        loding()
        os.system('clear')
        BAN_SUBDOMIN()

        choose = int(input(f'[{Purple}*{White}] Choose number :'))
        loding()
        if choose == 1 :
            HTTP_HTTPS = int(input(f'[{Cyan}1{White}] HTTP or [{Red}2{White}] HTTPS :'))
            FILE = open('Modules/Paths/domains.txt', 'r')
            Sub = Subdomains(url_web, HTTP_HTTPS, FILE)
            Sub.subdomins()

        elif choose == 2 :

            HTTP_HTTPS = int(input(f'[{Cyan}1{White}] HTTP or [{Red}2{White}] HTTPS :'))
            FILE = open(input(f'[{Purple}*{White}] Enter name file subdomains :'), 'r')

            Sub = Subdomains(url_web, HTTP_HTTPS, FILE)
            Sub.subdomins_your_file()
        elif choose == 99 :
            DARK()

    elif chos == 99 :
        print('\nGood bye ...')
        exit()

DARK()
