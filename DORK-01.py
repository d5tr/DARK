import requests

print('''

██████╗  ██████╗ ██████╗ ██╗  ██╗      ██████╗  ██╗
██╔══██╗██╔═══██╗██╔══██╗██║ ██╔╝     ██╔═████╗███║
██║  ██║██║   ██║██████╔╝█████╔╝█████╗██║██╔██║╚██║
██║  ██║██║   ██║██╔══██╗██╔═██╗╚════╝████╔╝██║ ██║
██████╔╝╚██████╔╝██║  ██║██║  ██╗     ╚██████╔╝ ██║
╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝      ╚═════╝  ╚═╝
                                                   
          MAKE BY ---> D5TR
          TEAM ---> zero one
          INSTA ---> @d_5tr
          INSTA 01 ---> @zer0one_01
       
''')

print('''
[1] Google dork 
[2] Guess the tracks
''')
chos = int(input('emter number you went :'))

url_web = input('ENTER YOU DOMINE :')


if chos == 1:
    print('<---START--->')

    #URLS !!
    url_plus = 'site:'+url_web+'\n'+'inurl:admin'

    url_plus7 = 'site:'+url_web+'\n'+'intext:admin'

    url_plus2 = 'site:'+url_web+'\n'+'inurl:php?1d='

    url_plus3 = 'site:'+url_web+'\n'+'inurl:php'

    url_plus4 = 'site:'+url_web+'\n'+'inurl:/php/upload.php'

    url_plus5 = 'site:'+url_web+'\n'+'inurl:login'

    url_plus6 = 'site:'+url_web+'\n'+'intitle:login'

    url_plus8 = 'site:'+url_web+'\n'+'inurl:id'

    url_plus9 = 'site:'+url_web+'\n'+'inurl:search'



    url ='https://www.google.com/search?q={}'.format(url_plus)

    url2 = 'https://www.google.com/search?q={}'.format(url_plus7)

    url3 = 'https://www.google.com/search?q={}'.format(url_plus2)

    url4 = 'https://www.google.com/search?q={}'.format(url_plus3)

    url5 = 'https://www.google.com/search?q={}'.format(url_plus4)

    url6 = 'https://www.google.com/search?q={}'.format(url_plus5)

    url7 = 'https://www.google.com/search?q={}'.format(url_plus6)

    url8 = 'https://www.google.com/search?q={}'.format(url_plus8)

    url9 = 'https://www.google.com/search?q={}'.format(url_plus9)


    header = {

        'Host': 'www.google.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://www.google.com/',
        'Connection': 'keep-alive',
        'Cookie': 'CGIC=CgtmaXJlZm94LWItZCJKdGV4dC9odG1sLGFwcGxpY2F0aW9uL3hodG1sK3htbCxhcHBsaWNhdGlvbi94bWw7cT0wLjksaW1hZ2Uvd2VicCwqLyo7cT0wLjg; 1P_JAR=2021-03-28-15; NID=212=wATgx6x_uXGspV7cr8XKvA2XKZfu1T6E4594AEsQUX61IgIJCnQL36pxicOochbMSMAY92bklhNgW9pg_ISWbb4OvG-o1V04WWatN6XvrKySSpjDUQXvY1_HwVZ_4qQ23Y5kyHBev2J2jv74S9EKQ0yKi4C66shN59AjcDJmR6DBTaUQJ3P_0IbJ4dPRI6fZcj2JcmdJZpAN3zu_EJXYUWfhNFAiF-tcnbVu2BD7PI0HMgEC6KHfJ6kk_cQ; ANID=AHWqTUlYXL4v1ak4_5V7uFa3PtbY0uZDVtBLakc-BXE1OO7BsOmKPZAb3j1AaCn6; SID=8Ae_t5rmaaJf7G9eAJ-YXBQ2kWI5QNvKL4FnsaJJsSrmDqv3anRaQh3fFxqoQeCKZHjiKQ.; __Secure-3PSID=8Ae_t5rmaaJf7G9eAJ-YXBQ2kWI5QNvKL4FnsaJJsSrmDqv3oFOQrSfepAfIZvn47kBl7w.; HSID=A8d7foMc4kphSToMg; SSID=ANxpbqnaDY9CpL5Ju; APISID=SY3f8OgzOvGfE2O2/A5UaqQOtnR-kzhum1; SAPISID=A_k2rGqWj2V3zdQm/Aebd-3Z4ZfhIzZRVz; __Secure-3PAPISID=A_k2rGqWj2V3zdQm/Aebd-3Z4ZfhIzZRVz; CONSENT=YES+SA.ar+202006; SIDCC=AJi4QfFZA-iqfsmEqsTM8gJHQhzoUbf_5pTI8KKE7Aw84lLBshxARFs_tVAhHrVkgou6GqyZ4Q; __Secure-3PSIDCC=AJi4QfERzak3OKDJJEXr767y6HbLQ3HcZSygYRRtyLHtg7kAY561L-bgGVJCph1rpiqyQUNOzA; SEARCH_SAMESITE=CgQImpIB',
        'TE': 'Trailers',

    }

    req = requests.get(url, headers=header).url

    req2 = requests.get(url2, headers=header).url

    req3 = requests.get(url3, headers=header).url

    req4 = requests.get(url4, headers=header).url

    req5 = requests.get(url5, headers=header).url

    req6 = requests.get(url6, headers=header).url

    req7 = requests.get(url7, headers=header).url

    req8 = requests.get(url8, headers=header).url

    req9 = requests.get(url9, headers=header).url



    print('[+] ADMIN :')
    print(req)
    print(req2)
    print('==========================')
    print('[+] PHP :')
    print(req3)
    print(req4)
    print(req5)
    print('==========================')
    print('[+] LOGIN :')
    print(req6)
    print(req7)
    print('==========================')
    print('[+] ID :')
    print(req8)
    print('==========================')
    print('[+] SEARCH :')
    print(req9)
    print('==========================')

    print('!END! -- INSTA :D_5TR ')

elif chos == 2:
    print('do you have file ?')
    y0n = input('Y , N :')
    if y0n == 'Y':
        http_https = input('http or https ? :')
        file = open(input('EMTER NAME FILE :'), 'r')
        file_open = file.readlines()
        for fils in file_open :
            fils = str(fils).strip()
            if http_https == 'http':
                url_1 = 'http://'+url_web+'/'+fils
                gess_req = requests.get(url_1).status_code

                if gess_req == 200 :
                    print('[+] FOUND >>>',url_1)
                else:
                    print('[-] NOT FOUND !!')
            elif http_https == 'https':
                url_2 = 'https://' + url_web + '/' + fils
                gess_req = requests.get(url_2).status_code

                if gess_req == 200:
                    print('[+] FOUND >>>', url_2)
                else:
                    print('[-] NOT FOUND !!')
    elif y0n == 'N':
        what = input('HTTP OR HTTPS ? :')

        if what == 'http':
            url_11 = 'http://'+url_web+'/'+'admin'

            url_12 = 'http://'+url_web+'/'+'password'

            url_13 = 'http://'+url_web+'/'+'login'

            url_14 = 'http://'+url_web+'/'+'robots.txt'

            url_15 = 'http://'+url_web+'/'+'welcom'

            url_16 = 'http://'+url_web+'/'+'index.php'

            url_17 = 'http://'+url_web+'/'+'upload.php'

            url_18 = 'http://'+url_web+'/'+'books'

            url_19 = 'http://'+url_web+'/'+'123'

            url_20 = 'http://'+url_web+'/'+'maile'

            url_21 = 'http://'+url_web+'/'+'superadmin'

            url_22 = 'http://'+url_web+'/'+'find'

            url_23 = 'http://'+url_web+'/'+'search'

            url_24 = 'http://'+url_web+'/'+'php'

            url_25 = 'http://'+url_web+'/'+'php?id=1'

            url_26 = 'http://'+url_web+'/'+'singin'

            x1 = requests.get(url_11).status_code

            x2 = requests.get(url_12).status_code

            x3 = requests.get(url_13).status_code

            x4 = requests.get(url_14).status_code

            x5 = requests.get(url_15).status_code

            x6 = requests.get(url_16).status_code

            x7 = requests.get(url_17).status_code

            x8 = requests.get(url_18).status_code

            x9 = requests.get(url_19).status_code

            x10 = requests.get(url_20).status_code

            x11 = requests.get(url_21).status_code

            x12 = requests.get(url_22).status_code

            x13 = requests.get(url_23).status_code

            x14 = requests.get(url_24).status_code

            x15 = requests.get(url_25).status_code

            x16 = requests.get(url_26).status_code

            if x1 == 200 :
                print('[+] FOUND >>>', url_11)

            else:
                print('[-] NOT FOUND !!')

            if x2 == 200:
                print('[+] FOUND >>>', url_12)

            else:
                print('[-] NOT FOUND !!')

            if x3 == 200:
                print('[+] FOUND >>>', url_13)

            else:
                print('[-] NOT FOUND !!')

            if x4 == 200:
                print('[+] FOUND >>>', url_14)

            else:
                print('[-] NOT FOUND !!')

            if x5 == 200:
                print('[+] FOUND >>>', url_15)

            else:
                print('[-] NOT FOUND !!')

            if x6 == 200:
                print('[+] FOUND >>>', url_16)

            else:
                print('[-] NOT FOUND !!')

            if x7 == 200:
                print('[+] FOUND >>>', url_17)

            else:
                print('[-] NOT FOUND !!')

            if x8 == 200:
                print('[+] FOUND >>>', url_18)

            else:
                print('[-] NOT FOUND !!')

            if x9 == 200:
                print('[+] FOUND >>>', url_19)

            else:
                print('[-] NOT FOUND !!')

            if x10 == 200:
                print('[+] FOUND >>>', url_20)

            else:
                print('[-] NOT FOUND !!')

            if x11 == 200:
                print('[+] FOUND >>>', url_21)

            else:
                print('[-] NOT FOUND !!')

            if x12 == 200:
                print('[+] FOUND >>>', url_22)

            else:
                print('[-] NOT FOUND !!')

            if x13 == 200:
                print('[+] FOUND >>>', url_23)

            else:
                print('[-] NOT FOUND !!')

            if x14 == 200:
                print('[+] FOUND >>>', url_24)

            else:
                print('[-] NOT FOUND !!')

            if x15 == 200:
                print('[+] FOUND >>>', url_25)

            else:
                print('[-] NOT FOUND !!')

            if x16 == 200:
                print('[+] FOUND >>>', url_26)

            else:
                print('[-] NOT FOUND !!')

        elif what == 'https':
            url_11 = 'https://' + url_web + '/' + 'admin'

            url_12 = 'https://' + url_web + '/' + 'password'

            url_13 = 'https://' + url_web + '/' + 'login'

            url_14 = 'https://' + url_web + '/' + 'robots.txt'

            url_15 = 'https://' + url_web + '/' + 'welcom'

            url_16 = 'https://' + url_web + '/' + 'index.php'

            url_17 = 'https://' + url_web + '/' + 'upload.php'

            url_18 = 'https://' + url_web + '/' + 'books'

            url_19 = 'https://' + url_web + '/' + '123'

            url_20 = 'https://' + url_web + '/' + 'maile'

            url_21 = 'https://' + url_web + '/' + 'superadmin'

            url_22 = 'https://' + url_web + '/' + 'find'

            url_23 = 'https://' + url_web + '/' + 'search'

            url_24 = 'https://' + url_web + '/' + 'php'

            url_25 = 'https://' + url_web + '/' + 'php?id=1'

            url_26 = 'https://' + url_web + '/' + 'xxx'

            x1 = requests.get(url_11).status_code

            x2 = requests.get(url_12).status_code

            x3 = requests.get(url_13).status_code

            x4 = requests.get(url_14).status_code

            x5 = requests.get(url_15).status_code

            x6 = requests.get(url_16).status_code

            x7 = requests.get(url_17).status_code

            x8 = requests.get(url_18).status_code

            x9 = requests.get(url_19).status_code

            x10 = requests.get(url_20).status_code

            x11 = requests.get(url_21).status_code

            x12 = requests.get(url_22).status_code

            x13 = requests.get(url_23).status_code

            x14 = requests.get(url_24).status_code

            x15 = requests.get(url_25).status_code

            x16 = requests.get(url_26).status_code

            if x1 == 200:
                print('[+] FOUND >>>', url_11)

            else:
                print('[-] NOT FOUND !!')

            if x2 == 200:
                print('[+] FOUND >>>', url_12)

            else:
                print('[-] NOT FOUND !!')

            if x3 == 200:
                print('[+] FOUND >>>', url_13)

            else:
                print('[-] NOT FOUND !!')

            if x4 == 200:
                print('[+] FOUND >>>', url_14)

            else:
                print('[-] NOT FOUND !!')

            if x5 == 200:
                print('[+] FOUND >>>', url_15)

            else:
                print('[-] NOT FOUND !!')

            if x6 == 200:
                print('[+] FOUND >>>', url_16)

            else:
                print('[-] NOT FOUND !!')

            if x7 == 200:
                print('[+] FOUND >>>', url_17)

            else:
                print('[-] NOT FOUND !!')

            if x8 == 200:
                print('[+] FOUND >>>', url_18)

            else:
                print('[-] NOT FOUND !!')

            if x9 == 200:
                print('[+] FOUND >>>', url_19)

            else:
                print('[-] NOT FOUND !!')

            if x10 == 200:
                print('[+] FOUND >>>', url_20)

            else:
                print('[-] NOT FOUND !!')

            if x11 == 200:
                print('[+] FOUND >>>', url_21)

            else:
                print('[-] NOT FOUND !!')

            if x12 == 200:
                print('[+] FOUND >>>', url_22)

            else:
                print('[-] NOT FOUND !!')

            if x13 == 200:
                print('[+] FOUND >>>', url_23)

            else:
                print('[-] NOT FOUND !!')

            if x14 == 200:
                print('[+] FOUND >>>', url_24)

            else:
                print('[-] NOT FOUND !!')

            if x15 == 200:
                print('[+] FOUND >>>', url_25)

            else:
                print('[-] NOT FOUND !!')

            if x16 == 200:
                print('[+] FOUND >>>', url_26)

            else:
                print('[-] NOT FOUND !!')








