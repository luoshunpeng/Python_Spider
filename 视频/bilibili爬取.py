import you_get  # 导入模块you_get
import sys  # 导入模块sys

url_please = input('请输入音频或视频的链接:>')
url = url_please  # 视频/音频的网址
path = './video'  # 路径
sys.argv = ['you_get', '-o', path, url]
you_get.main()
