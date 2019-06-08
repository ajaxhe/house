#!/usr/bin/python
# -*- coding:UTF-8 -*-

import os
import time

def main():
    #for c in range(10000,10200):
    #for c in range(15000,20000):
    for c in range(0,100000):
        counter_id = '%d-1-0-0' % c
        print "---------%s---------" % counter_id
        path = './test-data'
        filename = '%s/%s.json' % (path, counter_id)
        cmd = "curl 'http://bol.szhome.com/Project/GetBolBaList/' -H 'Cookie: _ga=GA1.2.432729057.1552354185; ddoldsearch_pc=5299%3B%u5E78%u798F%u73FA%u6E7E%7C; Hm_lvt_9a7b16ce65b422c3a2b3f1d30d705175=1559713117; Hm_lpvt_9a7b16ce65b422c3a2b3f1d30d705175=1559713117; Hm_lvt_c26237ea59fbcd4df5bf21d4e0b85a64=1559713120,1559801359; Hm_lpvt_c26237ea59fbcd4df5bf21d4e0b85a64=1559801379' -H 'Origin: http://bol.szhome.com' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: zh-CN,zh;q=0.9,en;q=0.8' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36' -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -H 'Accept: */*' -H 'Referer: http://bol.szhome.com/baj/6037.html' -H 'X-Requested-With: XMLHttpRequest' -H 'Proxy-Connection: keep-alive' --data 'page=1&pageSize=2000&id="+counter_id+"' --compressed --output "+filename+" -s -w %{http_code}"

        #cmd = "curl 'http://bol.szhome.com/Project/GetBolBaList/' -H 'Cookie: _ga=GA1.2.432729057.1552354185; ddoldsearch_pc=5299%3B%u5E78%u798F%u73FA%u6E7E%7C; Hm_lvt_9a7b16ce65b422c3a2b3f1d30d705175=1559713117; Hm_lpvt_9a7b16ce65b422c3a2b3f1d30d705175=1559713117; Hm_lvt_c26237ea59fbcd4df5bf21d4e0b85a64=1559713120,1559801359; Hm_lpvt_c26237ea59fbcd4df5bf21d4e0b85a64=1559801379' -H 'Origin: http://bol.szhome.com' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: zh-CN,zh;q=0.9,en;q=0.8' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36' -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -H 'Accept: */*' -H 'Referer: http://bol.szhome.com/baj/6037.html' -H 'X-Requested-With: XMLHttpRequest' -H 'Proxy-Connection: keep-alive' --data 'page=1&pageSize=20&id=42486-1-0-0' --compressed"
        print cmd
        ret = os.popen(cmd).readlines()
        if int(ret[0]) > 400:
            print "Wrong id: %s, remove filename: %s" % (counter_id, filename)
            if filename == '/':
                break
            remove_cmd = 'rm -rf %s' % filename
            os.popen(remove_cmd)
        else:
            print "Right id: %s, store filename: %s" % (counter_id, filename)

        print "\n"
        time.sleep(1)

if __name__ == '__main__':
    main()
