import csv
import random
import requests
from lxml import etree


def movie_download():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
        'Referer': 'https://www.douban.com/'
    }
    url = 'https://movie.douban.com/cinema/nowplaying/chengdu/'
    proxies = [{'http': '120.196.188.21:9091'}, {'http': '60.170.204.30:8060'}, {'http': '120.237.144.77:9091'}]
    response = requests.get(url=url, headers=headers, proxies=random.choice(proxies))
    text = response.text
    html = etree.HTML(text)
    ul = html.xpath('//ul[@class="lists"]')[0]
    lis = ul.xpath('./li')
    f = open('电影.csv', 'w', encoding='utf-8')
    movie_content = ['标题', '得分', '年代', '时长', '产地', '导演', '演员']
    writer = csv.DictWriter(f, fieldnames=movie_content)
    writer.writeheader()
    for li in lis:
        title = li.xpath('@data-title')[0]
        score = li.xpath('@data-score')[0]
        data = li.xpath('@data-release')[0]
        time = li.xpath('@data-duration')[0]
        place = li.xpath('@data-region')[0]
        director = li.xpath('@data-director')[0]
        actor = li.xpath('@data-actors')[0]
        movie = {
            '标题': title,
            '得分': score,
            '年代': data,
            '时长': time,
            '产地': place,
            '导演': director,
            '演员': actor
        }
        writer.writerow(movie)
    print（'——————————————————开始下载——————————————————')
    f.close()
    print("——————————————————下载成功——————————————————")


if __name__ == '__main__':
    movie_download()
