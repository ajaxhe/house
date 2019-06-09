#!/usr/bin/python
# -*- coding:UTF-8 -*-

from bs4 import BeautifulSoup as bs
import requests
import sys

def get_html_title():
    #for c in range(5220,5221):
    #for c in range(1,2):
    for c in range(0,10000):
        '''
        curl "http://bol.szhome.com/house/5220.htm" -H "Connection: keep-alive" -H "Cache-Control: max-age=0" -H "Upgrade-Insecure-Requests: 1" -H "User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36" -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8" -H "Accept-Encoding: gzip, deflate" -H "Accept-Language: zh-CN,zh;q=0.9,en;q=0.8" -H "Cookie: _ga=GA1.2.957708761.1551490417; Hm_lvt_9a7b16ce65b422c3a2b3f1d30d705175=1558834920; ddoldsearch_pc=5220^%^3B^%^u677E^%^u8302^%^u5FA1^%^u9F99^%^u6E7E^%^7C5299^%^3B^%^u5E78^%^u798F^%^u73FA^%^u6E7E^%^7C; Hm_lvt_c26237ea59fbcd4df5bf21d4e0b85a64=1559916371,1559916372,1559920426,1559920781; Hm_lpvt_9a7b16ce65b422c3a2b3f1d30d705175=1560084509; Hm_lpvt_c26237ea59fbcd4df5bf21d4e0b85a64=1560085251" --compressed
        '''
        # http://bol.szhome.com/house/5220.htm
        url = 'http://bol.szhome.com/house/%d.htm' % c
        header = {
                'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36',
                #'Cookie': '_ga=GA1.2.957708761.1551490417; Hm_lvt_9a7b16ce65b422c3a2b3f1d30d705175=1558834920; ddoldsearch_pc=5220%3B%u677E%u8302%u5FA1%u9F99%u6E7E%7C5299%3B%u5E78%u798F%u73FA%u6E7E%7C; Hm_lvt_c26237ea59fbcd4df5bf21d4e0b85a64=1559916371,1559916372,1559920426,1559920781; Hm_lpvt_9a7b16ce65b422c3a2b3f1d30d705175=1560084509; Hm_lpvt_c26237ea59fbcd4df5bf21d4e0b85a64=1560085251',
                #'Upgrade-Insecure-Requests': 1,
                }
        rep = requests.get(url, headers=header)
        try:
            sp = bs(rep.text, 'html.parser')
            #print c, url, rep.status_code, sp.find("title")
            print c, url, rep.status_code, sp.title.string
        except Exception, err:
            print c, url, err


def main():
    get_html_title()

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
