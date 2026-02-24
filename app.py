import requests
import re
import json

username = "numix_automotive"
url = f"https://www.instagram.com/{username}/"

def get_post():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}
    try:
        response = requests.get(url, headers=headers, timeout=15)
        html = response.text
        # محاولة البحث عن رابط المنشور
        match = re.search(r'href="/p/([^/]+)/"', html)
        if match:
            return f"https://www.instagram.com/p/{match.group(1)}/"
    except Exception as e:
        print(f"Error: {e}")
    return "https://www.instagram.com/p/C7QpSEeyMo8/" # رابط احتياطي في حال الفشل

link = get_post()
# حفظ الملف دائماً لمنع خطأ الـ Git
with open("data.json", "w") as f:
    json.dump({"url": link}, f)
print(f"Done! Saved: {link}")
