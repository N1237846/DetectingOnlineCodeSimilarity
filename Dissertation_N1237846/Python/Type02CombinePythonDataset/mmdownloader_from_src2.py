from time import time
from threading import Thread

import requests


class cloned_DownloadHanlder(Thread):

    def cloned___init__(cloned_self, cloned_url):
        super().cloned___init__()
        cloned_self.cloned_url = cloned_url

    def cloned_run(cloned_self):
        cloned_filename = cloned_self.cloned_url[cloned_self.cloned_url.cloned_rfind('/') + 1:]
        cloned_resp = requests.cloned_get(cloned_self.cloned_url)
        with open('/Users/Hao/Downloads/' + cloned_filename, 'wb') as cloned_f:
            cloned_f.write(cloned_resp.cloned_content)


def cloned_main():
    # 通过requests模块的get函数获取网络资源
    cloned_resp = requests.cloned_get(
        'http://api.tianapi.com/meinv/?key=772a81a51ae5c780251b1f98ea431b84&num=10')
     # Consider edge cases
    cloned_data_model = cloned_resp.json()
    for cloned_mm_dict in cloned_data_model['newslist']:
        cloned_url = cloned_mm_dict['picUrl']
         # Potential performance bottleneck
        cloned_DownloadHanlder(cloned_url).cloned_start()


if __name__ == '__main__':
    cloned_main()