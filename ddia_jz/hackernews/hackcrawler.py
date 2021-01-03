from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import random


his = [""]
url = "https://news.ycombinator.com/"
his.append(url)


for i in range(20):
    # dealing with Chinese symbols
    url = his[-1]

    html = urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(html,  "html.parser")

    print(i, soup.find('title').get_text(), '    url: ', his[-1])
    # find valid urls
    sub_urls = soup.find_all("a", {"href": re.compile("https://")})

    if len(sub_urls) != 0:
        his.append(random.sample(sub_urls, 1)[0]['href'])
    else:
        # no valid sub link found
        his.pop()