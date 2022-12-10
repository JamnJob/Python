import requests 
from bs4 import BeautifulSoup
from os.path import exists

# este primeiro bloco: montar as url´s para uso posterior de coleta dos dados almejados 
# ----------------------------------------------------------------------------------------

fileLinks = exists('links.txt')
if fileLinks:
    with open('links.txt') as f: 
        links = [link for link in f]
#        print (links)
        for urls in iter(lambda: f.readline(), ''):
            
                       
            headers = {
                'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}
            #print(urls)
            site2 = requests.get(urls, headers=headers)
            soup2 = BeautifulSoup(site2.content, 'html.parser')
            urlPagLast = '/pagina-'
            
            for i in range(1, 46):                                      ### hard codded, eu sei, eu sei 
                last = str(urls + urlPagLast + str(i)) 
                #print (last)                                            #### url principal mais /pagina- mais número range 
                req = requests.get(last, allow_redirects=False)         ### cod 200 para OK e 404 
                resp = str('<Response [200]>')                          ### pega o código e string nele  
                last1 = last + str(req)                                 ### pega o last e coloca o resp 
                #print (last1)
                if any((resp in last1) for r in last1):
                    print(req)     
 
else: 
    url = 'https://supercasa.pt/arrendar-casas#homeLinks'
    urlShort = 'https://supercasa.pt'

    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}

    site = requests.get(url, headers=headers) 
    soup = BeautifulSoup(site.content, 'html.parser')

    home = soup.find_all('div', class_='home-links-list')
    hra =  soup.find_all('a', href=True)

    for distDiv in home:
        for distA in hra: 
            try: 
                requests.get(urlShort + distA['href'])
                urlLong = [urlShort + distA['href']]
                
                if 'https://supercasa.pt/arrendar-casas/' in urlLong and '#' not in urlLong:
                        #print (urlLong)
                        urls = [urlLong]
                        #urls.append(urlLong) 
                        #print (urls.index(urls))
                        print(urls)
            except: 
                None
