#!/usr/bin/env python

import requests
from Core.Colors import *


class Tracks():
    # what we need 
    def __init__(self, URL, http_or_https, name_file=''):
        self.URL = URL
        self.http_or_https = int(http_or_https)
        self.name_file = name_file

    # PHP
    def PHP(self):
        # read file
        file_PHP = open('Modules/Paths/PHP-path-wordlist-sorted.txt', 'r').readlines()
        
        # split file
        for open_file_PHP in file_PHP:
            open_file_PHP = str(open_file_PHP).strip()
            if self.http_or_https == 1:
        
                # make url
                url_http = 'http://'+self.URL+'/'+open_file_PHP
        
                # send request
                req_http = requests.get(url_http).status_code
                if req_http == 200:
                    print(f'[{Green}200{White}] Found ---> ', url_http)
        
                    # save result
                    with open('PHP_http.txt', 'a') as ssave:
                        ssave.write(url_http+'\n')

                elif req_http == 429 :
                    print(f'{Red}429{Red} Band !!!{White}')
                    exit()

                else:
                    print(f'[{Red}404{White}] Not Found !')


            elif self.http_or_https == 2 :
                
                # make url
                url_https = 'https://'+self.URL+'/'+open_file_PHP
                
                # send requests
                req_https = requests.get(url_https).status_code
                
                if req_https == 200:
                    print(f'[{Green}+{White}] Found ---> ', url_https)
                    
                    # save result
                    with open('PHP_https.txt', 'a') as ssave:
                        ssave.write(url_https+'\n')

                elif req_https == 429 :
                    print(f'{Red}429{Red} Band !!!{White}')
                    exit()
               
                else:
                    print(F'[{Red}-{White}] Not Found !')


    # HTML
    def HTML(self):
        
        # read file
        file_HTML = open('Modules/Paths/html-path-wordlist-sorted.txt', 'r').readlines()
        
        
        for open_file_HTML in file_HTML:
            open_file_HTML = str(open_file_HTML).strip()
            if self.http_or_https == 1:
        
                # make url        
                url_http = 'http://'+self.URL+'/'+open_file_HTML
                
                # send requests
                req_http = requests.get(url_http).status_code
                if req_http == 200:
                    print(f'[{Green}+{White}] Found ---> ', url_http)
                    
                    # save result
                    with open('HTML_http.txt', 'a') as ssave:
                        ssave.write(url_http+'\n')

                elif req_http == 429 :
                    print(f'{Red}429{Red} Band !!!{White}')
                    exit()

                else:
                    print(F'[{Red}-{White}] Not Found !')


            elif self.http_or_https == 2:
                
                url_https = 'https://'+self.URL+'/'+open_file_HTML
                
                req_https = requests.get(url_https).status_code
                if req_https == 200:
                    print(f'[{Green}+{White}] Found ---> ', url_https)
                
                    with open('HTML_https.txt', 'a') as ssave:
                        ssave.write(url_https+'\n')

                elif req_https == 429 :
                    print(f'{Red}429{Red} Band !!!{White}')
                    exit()

                else:
                    print(F'[{Red}-{White}] Not Found !')


    def WORD_PREES(self):
        
        file_word_prees = open('Modules/Paths/wordpress.txt', 'r').readlines()
        
        for open_file_word_prees in file_word_prees:
            open_file_word_prees = str(open_file_word_prees).strip()
        
            if self.http_or_https == 1:
        
                url_http = 'http://'+self.URL+'/'+open_file_word_prees
                req_http = requests.get(url_http).status_code
        
                if req_http == 200:
                    print(f'[{Green}+{White}] Found ---> ', url_http)
        
                    with open('wordpress_http.txt', 'a') as ssave:
                        ssave.write(url_http+'\n')

                elif req_http == 429 :
                    print(f'{Red}429{Red} Band !!!{White}')
                    exit()

                else:
                    print(F'[{Red}-{White}] Not Found !')


            elif self.http_or_https == 2:
            
                url_https = 'https://'+self.URL+'/'+open_file_word_prees
            
                req_https = requests.get(url_https).status_code
            
                if req_https == 200:
                    print(f'[{Green}+{White}] Found ---> ', url_https)
            
                    with open('wordpress_https.txt', 'a') as ssave:
                        ssave.write(url_https+'\n')

                elif req_https == 429 :
                    print(f'{Red}429{Red} Band !!!{White}')
                    exit()

                else:
                    print(F'[{Red}-{White}] Not Found !')

    def Admins(self):

        file_Admins = open('Modules/Paths/Admins.txt', 'r').readlines()

        for open_file_Admins in file_Admins:
            open_file_Admins = str(open_file_Admins).strip()

            if self.http_or_https == 1:

                url_http = 'http://' + self.URL + '/' + open_file_Admins
                req_http = requests.get(url_http).status_code

                if req_http == 200:
                    print(f'[{Green}200{White}] Found ---> ', url_http)

                    with open('admins_http.txt', 'a') as ssave:
                        ssave.write(url_http + '\n')

                elif req_http == 429 :
                    print(f'{Red}429{Red} Band !!!{White}')
                    exit()

                else:
                    print(F'[{Red}404{White}] Not Found !')


            elif self.http_or_https == 2:

                url_https = 'https://' + self.URL + '/' + open_file_Admins

                req_https = requests.get(url_https).status_code

                if req_https == 200:
                    print(f'[{Green}+{White}] Found ---> ', url_https)

                    with open('admin_https.txt', 'a') as ssave:
                        ssave.write(url_https + '\n')

                elif req_https == 429 :
                    print(f'{Red}429{Red} Band !!!{White}')
                    exit()

                else:
                    print(F'[{Red}-{White}] Not Found !')

    def OTHER(self):
        
        file_other = open(self.name_file, 'r').readlines()
        
        for open_file_other in file_other:
            open_file_other = str(open_file_other).strip()
        
            if self.http_or_https == 1:
        
                url_http = 'http://'+self.URL+'/'+open_file_other
        
                req_http = requests.get(url_http).status_code
        
                if req_http == 200:
                    print(f'[{Green}+{White}] Found ---> ', url_http)
        
                    with open('your_tracks_http.txt', 'a') as ssave:
                        ssave.write(url_http+'\n')

                elif req_http == 429 :
                    print(f'{Red}429{Red} Band !!!{White}')
                    exit()

                else:
                    print(F'[{Red}-{White}] Not Found !')


            elif self.http_or_https == 2:
        
                url_https = 'https://'+self.URL+'/'+open_file_other
            
                req_https = requests.get(url_https).status_code
            
                if req_https == 200:
                    print(f'[{Green}+{White}] Found ---> ', url_https)
            
                    with open('your_Path_https.txt', 'a') as ssave:
                        ssave.write(url_https+'\n')

                elif req_https == 429 :
                    print(f'{Red}429{Red} Band !!!{White}')
                    exit()

                else:
                    print(F'[{Red}-{White}] Not Found !')




