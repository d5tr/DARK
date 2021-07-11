import requests
from colorama import Fore

def PHP(URL, http_or_https):
    # read file
    file_PHP = open('Requests/PHP-path-wordlist-sorted.txt', 'r').readlines()
    # split file
    for open_file_PHP in file_PHP:
        open_file_PHP = str(open_file_PHP).strip()
        if http_or_https == 1:
            # make url
            url_http = 'http://'+URL+'/'+open_file_PHP
            # send request
            req_http = requests.get(url_http).status_code
            if req_http == 200:
                print(f'[{Fore.GREEN}+{Fore.WHITE}] Found ---> ', url_http)
                # save in file
                with open('PHP_http.txt', 'a') as ssave:
                    ssave.write(url_http+'\n')
            else:
                print(F'[{Fore.RED}-{Fore.WHITE}] Not Found !')


        elif http_or_https == 2 :
            url_https = 'https://'+URL+'/'+open_file_PHP
            req_https = requests.get(url_https).status_code
            if req_https == 200:
                print(f'[{Fore.GREEN}+{Fore.WHITE}] Found ---> ', url_https)
                with open('PHP_https.txt', 'a') as ssave:
                    ssave.write(url_https+'\n')
            else:
                print(F'[{Fore.RED}-{Fore.WHITE}] Not Found !')



def HTML(URL, http_or_https):
    file_HTML = open('Requests/html-path-wordlist-sorted.txt', 'r').readlines()
    for open_file_HTML in file_HTML:
        open_file_HTML = str(open_file_HTML).strip()
        if http_or_https == 1:
            url_http = 'http://'+URL+'/'+open_file_HTML
            req_http = requests.get(url_http).status_code
            if req_http == 200:
                print(f'[{Fore.GREEN}+{Fore.WHITE}] Found ---> ', url_http)
                with open('HTML_http.txt', 'a') as ssave:
                    ssave.write(url_http+'\n')
            else:
                print(F'[{Fore.RED}-{Fore.WHITE}] Not Found !')


        elif http_or_https == 2:
            url_https = 'https://'+URL+'/'+open_file_HTML
            req_https = requests.get(url_https).status_code
            if req_https == 200:
                print(f'[{Fore.GREEN}+{Fore.WHITE}] Found ---> ', url_https)
                with open('HTML_https.txt', 'a') as ssave:
                    ssave.write(url_https+'\n')
            else:
                print(F'[{Fore.RED}-{Fore.WHITE}] Not Found !')


def WORD_PREES(URL, http_or_https):
    file_word_prees = open('Requests/wordpress.txt', 'r').readlines()
    for open_file_word_prees in file_word_prees:
        open_file_word_prees = str(open_file_word_prees).strip()
        if http_or_https == 1:
            url_http = 'http://'+URL+'/'+open_file_word_prees
            req_http = requests.get(url_http).status_code
            if req_http == 200:
                print(f'[{Fore.GREEN}+{Fore.WHITE}] Found ---> ', url_http)
                with open('wordpress_http.txt', 'a') as ssave:
                    ssave.write(url_http+'\n')
            else:
                print(F'[{Fore.RED}-{Fore.WHITE}] Not Found !')


        elif http_or_https == 2:
            url_https = 'https://'+URL+'/'+open_file_word_prees
            req_https = requests.get(url_https).status_code
            if req_https == 200:
                print(f'[{Fore.GREEN}+{Fore.WHITE}] Found ---> ', url_https)
                with open('wordpress_https.txt', 'a') as ssave:
                    ssave.write(url_https+'\n')
            else:
                print(F'[{Fore.RED}-{Fore.WHITE}] Not Found !')



def OTHER(URL, http_or_https, name_file):
    file_other = open(name_file, 'r').readlines()
    for open_file_other in file_other:
        open_file_other = str(open_file_other).strip()
        if http_or_https == 1:
            url_http = 'http://'+URL+'/'+open_file_other
            req_http = requests.get(url_http).status_code
            if req_http == 200:
                print(f'[{Fore.GREEN}+{Fore.WHITE}] Found ---> ', url_http)
                with open('your_tracks_http.txt', 'a') as ssave:
                    ssave.write(url_http+'\n')
            else:
                print(F'[{Fore.RED}-{Fore.WHITE}] Not Found !')


        elif http_or_https == 2:
            url_https = 'https://'+URL+'/'+open_file_other
            req_https = requests.get(url_https).status_code
            if req_https == 200:
                print(f'[{Fore.GREEN}+{Fore.WHITE}] Found ---> ', url_https)
                with open('your_tracks_https.txt', 'a') as ssave:
                    ssave.write(url_https+'\n')
            else:
                print(F'[{Fore.RED}-{Fore.WHITE}] Not Found !')




