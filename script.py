
import requests
from bs4 import BeautifulSoup
from mailing_script import send_mail

url = 'http://www.ipu.ac.in/notices.php'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

doc = open('last_notice.txt','r')
last_notice = doc.read().replace('\n','')
doc.close()

links = soup.find(class_='table-box')
links_list = links.find_all('a')

notice_subject = []
notice_url     = []

email = ['deepakvats97@gmail.com'] # MORE RECEIVERS HERE

chk = 0

for i in links_list:
    content =  i.contents[0].encode('utf-8')
    href    =  i.get('href').encode('utf-8')
    href    =  "http://www.ipu.ac.in" + href

    if(chk==0):
        chk = 1
        first_href = href

    if (href==last_notice):
        doc = open('last_notice.txt','w')
        doc.write(first_href)
        doc.close()
        break


    notice_url.append(href)
    notice_subject.append(content)
import ipdb; ipdb.set_trace()
for i in range(0,len(notice_url)):
    for j in email:
        send_mail(notice_subject[i], notice_url[i], j)
import ipdb; ipdb.set_trace()
