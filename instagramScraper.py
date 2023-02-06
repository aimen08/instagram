import requests
import base64
from urllib.parse import parse_qs
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import js2py
import re




def b64decode(str):
    str = str.replace('_','/')
    str += "=" * ((4 - len(str) % 4) % 4)
    return base64.b64decode(str)

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:92.0) Gecko/20100101 Firefox/92.0',
}

instagramDomains = (
    'https://www.instagram.com',
    'https://instagram.com'
)


def getVideo(url):
    if not url.startswith('http'):
        url = 'https://' + url

    if url.lower().startswith(instagramDomains):
        url = url.split('?')[0]  
        data = {
            "url":url,
            "action":"post",
            "lang":"",
        }     
        try:
            
            headers= {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:92.0) Gecko/20100101 Firefox/92.0',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Accept-Encoding': 'gzip, deflate',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Content-Length': '96',
                'Origin': 'https://snapinsta.app',
                'Referer': 'https://snapinsta.app',
                'Upgrade-Insecure-Requests': '1',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-User': '?1',
                # "Cookie": f"__cf_bm={cookies['__cf_bm']}; _cfuvid={cookies['_cfuvid']}",               
            }
            
            response = requests.post('https://snapinsta.app/action.php', data=data, headers=headers, allow_redirects=False)
            js =  response.content.decode("utf-8").replace("eval", "")  
            s = js2py.eval_js(js)     
            link , _ = re.findall(r'href=\\"(([^"])+)', s)[0]

            return link

        except Exception as e:
            return {
                'success': False,
                'error': e
            }
        
        else:
            return {
                        'success': False,
                        'error': 'exception'
                    }

    else:
        return {
                    'success': False,
                    'error': 'invalidUrl'
                }
