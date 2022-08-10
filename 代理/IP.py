import re
import requests
import time


def ip_obtain():
    print('例如:>', '\n', 'https://free.kuaidaili.com/free/', '\n', 'https://proxy.ip3366.net/free/')
    time.sleep(0.5)
    website = input("请输入IP代理网站:>")
    page = input('请输入页数(齐云最多10页):>')
    num = int(page)
    time.sleep(0.5)
    li = []
    li_1 = []
    for i in range(1, int(num+1)):
        url = str(website)
        time.sleep(2)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62',
            'Cookie': 'channelid=0; sid=1658311835876881; _gcl_au=1.1.785134134.1658311879; '
                      '_ga=GA1.2.1995988597.1658311879; '
                      'Hm_lvt_7ed65b1cc4b810e9fd37959c9bb51b31=1658313236,1658444164,1658446531,1658617093; '
                      '_gid=GA1.2.1054015475.1658617094; _gat=1; Hm_lpvt_7ed65b1cc4b810e9fd37959c9bb51b31=1658617170 '
        }
        time.sleep(0.5)
        response = requests.get(url=url, headers=headers)
        time.sleep(3)
        ip_list = re.findall('<td data-title="IP">(.*?)</td>', response.text)
        port_list = re.findall('<td data-title="PORT">(.*?)</td>', response.text)
        time.sleep(0.5)
        for ip, port in zip(ip_list, port_list):
            proxies_dist = {
                'http': ip + ':' + port
            }
            li.append(proxies_dist)
            try:
                response_one = requests.get(url='http://www.baidu.com', proxies=proxies_dist, timeout=1)
                time.sleep(0.5)
                if response_one.status_code == 200:
                    print("可用IP:", proxies_dist)
                    li_1.append(proxies_dist)
            except requests.exceptions.RequestException:
                print("不可用IP:", proxies_dist)
    print(f'获取了{len(li)}')
    print("-*-*-"*20)
    print(f'可用{len(li_1)}')
    print("-*-*-"*20)
    print(li_1)


ip_obtain()
