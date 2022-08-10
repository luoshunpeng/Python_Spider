import os
from time import sleep
import requests
from lxml import etree

headers = {
    'user - agent': 'Mozilla / 5.0(WindowsNT10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 80.0.3987.116Safari / 537.36'
}

data_path = './图片'
if not os.path.exists(data_path):
    os.mkdir(data_path)


# 得到进一步的页面链接
def get_first_url(url):
    response = requests.get(url=url, headers=headers).text
    html = etree.HTML(response)
    lists = html.xpath('//*[@id="main"]/div[3]/ul')
    for i in range(len(lists)):
        li = lists[i].xpath('./li/a/@href')
        return li


# 得到图片的内容和名称
def get_image_data(url):
    response = requests.get(url=url, headers=headers).text
    html = etree.HTML(response)
    src = html.xpath('//*[@id="img"]/img/@src')[0]
    image_src = 'http://pic.netbian.com' + src  # 得到图片下载地址
    image_data = requests.get(url=image_src, headers=headers).content  # 拿到图篇内容
    name = html.xpath('//*[@id="img"]/img/@alt')[0] + '.jpg'  # 提取网页图片的名字
    name = name.encode('iso-8859-1').decode('gbk')  # 指定格式编码字符串
    return image_data, name


# 保存图片到本地
def download(path, name, data):
    save_path = path + '/' + name
    with open(save_path, 'wb') as f:
        f.write(data)
        print(save_path, '=========>下载成功啦！！！')
        f.close()


def main():
    base_url = 'http://pic.netbian.com/4kmeinv/'
    first_url = get_first_url(base_url)
    for i in range(len(first_url)):
        print('第{}张正在下载请稍后'.format(i + 1))
        image_url = 'http://pic.netbian.com' + first_url[i]
        image_data, name = get_image_data(image_url)
        download(data_path, name, image_data)
        sleep(1)  # 延迟1秒


if __name__ == '__main__':
    main()
