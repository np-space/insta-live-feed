import requests
import re
import json

# معلومات الحساب
username = "numix_automotive"
url = f"https://www.instagram.com/{username}/"

def get_post():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    try:
        html = requests.get(url, headers=headers).text
        match = re.search(r'href="/p/([^/]+)/"', html)
        if match:
            return f"https://www.instagram.com/p/{match.group(1)}/"
    except:
        return None

link = get_post()
if link:
    with open("data.json", "w") as f:
        json.dump({"url": link}, f)
