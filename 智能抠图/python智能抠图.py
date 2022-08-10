from removebg import RemoveBg as Rem
import os

"""登录网址:https://www.remove.bg/zh/api#remove-background, 获取激活码."""
#       ’激          活         码‘, '附 属 文 件'
r = Rem('mia4HTGgMQkpnkXx1WytY6Uc', 'error.log')
p = './图片'  # 图片文件夹的路径
file = os.listdir(path=p)
print('正在抠图......'+'\n'+'......')
for i in file:  # 将图片遍历一遍
    sort = os.path.join(p, i)  # 将图片进行排序
    r.remove_background_from_img_file(sort)  # 将遍历过后的文件进行抠图
print('抠图完毕......')
