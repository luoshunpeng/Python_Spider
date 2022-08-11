import requests
from lxml import etree

url = 'https://movie.douban.com/top250'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.47'
}
response = requests.get(url=url, headers=headers)
html_HTML = etree.HTML(response.content.decode())
video_names = html_HTML.xpath('//div[@class="hd"]/a/span[@class="title"]/text()')
with open("Top250的电影名.txt", "w", encoding="utf-8") as file:
    print('开始下载')
    for names in video_names:
        file.write(str(names))
        file.write('\n')
        print('下载成功')
        