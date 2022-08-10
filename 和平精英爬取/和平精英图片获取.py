import requests
# 导入模块requests也可以取别名:
# import requests as 自己取的名字
from lxml import etree  # 从lxml里面导入我们的etree模块

url = 'https://gp.qq.com/cp/a20190522gamedata/pc_list.shtml'  # 需要请求的网址
response = requests.get(url=url).text.encode('utf-8')  # 发送请求, 并把返回值传给response这个变量
response_html = etree.HTML(response)  # 将网站进行分析
image = response_html.xpath('//*[@id="section-container"]/ul/li/a/img')  # 通过xpath这个方法找出所有图片地址的链接
name = response_html.xpath('//*[@id="section-container"]/ul/li/a/p/text()')  # 通过xpath这个方法找出所有图片地址的名字
for images, names in zip(image, name):  # 对所有图片地址的链接和所有图片地址的名字进行遍历和用zip()个方法进行压缩
    images_src = images.xpath('./@src')[0]  # 取到img元素里的src属性, 并存到列表的的一个元素, 引索就是0
    images_link = 'https:'+images_src  # 把前面的不全链接补全, 补上https:
    res = requests.get(url=images_link)  # 请求图片数据, 并把返回值传到res里面
    with open('./images/' + str(names) + '.png', 'wb') as file:  # 下载图片数据
        print('开始下载...')  # 打印开始下载
        file.write(res.content)  # 写入图片
        file.close()  # 关闭写入, 不关也行
        print('下载完毕( •̀ ω •́ )y')  # 打印下载完成
