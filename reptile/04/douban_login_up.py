import requests
import html5lib
import re
from bs4 import BeautifulSoup

s = requests.Session()
url_login = 'https://accounts.douban.com/login'
url_contacts = 'https://www.douban.com/people/***/contacts'

formdata= {
    'redir':'https://accounts.douban.com',
    'form_email': 't.t.panda@hotmail.com'
    'form_password': 'tp65536!',
    'login': u'登陆
    }

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0'}

r = s.post(url_login, data =formdata, headers = headers)
content = r.text
# 查找验证码
soup = BeautifulSoup(content,'html5lib')
captcha =  soup.find('img', id = 'captcha_image')

if captcha:
    
    captcha_url =  captcha['src']
    # 正则表达式来匹配
    re_captcha_id =  r'<input type="hidden" name="captcha-id" value="(.*?)"/'

    captcha_id = re.findall(re_captcha_id,content)
    print(captcha_id)
    print(captcha_url)

    captcha_text =  input('Please input the captcha:')
    formdata['captcha-solution'] = captcha_text
    formdata['captcha-id'] = captcha_id
    r = s.post(url_login, data = formdata, headers = headers)
r = s.get(url_contacts)
with open('contacts.txt', 'w+', encoding = 'utf-8') as f:
    f.write(r.text)
