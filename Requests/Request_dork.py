import requests
from colorama import Fore

def req_google_dork(URLS):
    print(f'<---{Fore.GREEN}START{Fore.WHITE}--->')

    #URLS !!
    # make google dork to search
    url_plus = 'site:'+URLS+'\n'+'inurl:admin'

    url_plus7 = 'site:'+URLS+'\n'+'intext:admin'

    url_plus2 = 'site:'+URLS+'\n'+'inurl:php?1d='

    url_plus3 = 'site:'+URLS+'\n'+'inurl:php'

    url_plus4 = 'site:'+URLS+'\n'+'inurl:/php/upload.php'

    url_plus5 = 'site:'+URLS+'\n'+'inurl:login'

    url_plus6 = 'site:'+URLS+'\n'+'intitle:login'

    url_plus8 = 'site:'+URLS+'\n'+'inurl:id'

    url_plus9 = 'site:'+URLS+'\n'+'inurl:search'


    # search in google
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
    # send request
    req = requests.get(url, headers=header).url

    req2 = requests.get(url2, headers=header).url

    req3 = requests.get(url3, headers=header).url

    req4 = requests.get(url4, headers=header).url

    req5 = requests.get(url5, headers=header).url

    req6 = requests.get(url6, headers=header).url

    req7 = requests.get(url7, headers=header).url

    req8 = requests.get(url8, headers=header).url

    req9 = requests.get(url9, headers=header).url



    print(Fore.BLUE+'[+] ADMIN :')
    print(Fore.WHITE+req)
    print(req2)
    print('==========================')
    print(Fore.BLUE+'[+] PHP :')
    print(Fore.WHITE+req3)
    print(req4)
    print(req5)
    print('==========================')
    print(Fore.BLUE+'[+] LOGIN :')
    print(Fore.WHITE+req6)
    print(req7)
    print('==========================')
    print(Fore.BLUE+'[+] ID :')
    print(Fore.WHITE+req8)
    print('==========================')
    print(Fore.BLUE+'[+] SEARCH :')
    print(Fore.WHITE+req9)
    print('==========================')

    print(Fore.RED+'!END! -- INSTA :D_5TR ')