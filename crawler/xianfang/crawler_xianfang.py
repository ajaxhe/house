#!/usr/bin/python
# -*- coding:UTF-8 -*-

import os
import time

def main():
    page_size = 20
    house_name = '松茂御龙湾' 
    path = './xianfang-data/%s' % house_name
    ret = os.popen('mkdir -p %s' % path).readlines()
    for c in range(0,100):
    #for c in range(0,1000):
        # txtBldg_Name_No: 松茂御龙湾
        # ddlPageCount: 分页条数，最大20条？
        # __EVENTTARGET: AspNetPager1  分页的时候必须设置
        # __EVENTARGUMENT: 页数
        page_num = c
        print "---------%s---------" % page_num
        
        filename = '%s/%s_%d-%d.html' % (path, house_name, page_num*page_size, (page_num+1)*page_size)

        cmd = "curl 'http://zjj.sz.gov.cn/ris/bol/szfdc/smc_ProjectList.aspx' -H 'Origin: http://zjj.sz.gov.cn' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: zh-CN,zh;q=0.9,en;q=0.8' -H 'User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Accept: */*' -H 'Cache-Control: no-cache' -H 'Referer: http://zjj.sz.gov.cn/ris/bol/szfdc/smc_ProjectList.aspx' -H 'Connection: keep-alive' -H 'X-MicrosoftAjax: Delta=true' --data 'scriptManager1=updatepanel1|AspNetPager1&__EVENTTARGET=AspNetPager1&__EVENTARGUMENT="+str(page_num)
        cmd = cmd+"&__LASTFOCUS=&__VIEWSTATE=6IkPUF8oSAEmUOPiJvlt9wuiB1PNAZ9tQEDP%2BUd2qmkBrYxpEB7n0JGWJRnoAmtLGCONZ0o6H4B%2FI%2B8p9fc2JoolB3GvcHSysqhYa%2FAc4VCLsFEi1llBTlYO2L4ale0gyrR9vm80jKpJnDQJ9EVW6M%2BSKwc2NoKokxJ7OXvo3ENJXhx0Ypd3nXm33%2B243ZsNAjWhMZak%2Be2%2F3GrYq8Gu5uiP%2BSNgcfEWiP0ej6ASEL4SGzOgY9Ixg67C1YzMzXb4b4kCFNt2MDyGTgGDnhcNxPo%2B8DXxl3xlNX6kZNdnrHVauT40729N0RaA7IAicACPBT7vTwtkOBoj8dhgCXry5JdINEKj8uEF9DEmCKcY%2FxHFaf5bOP3co78n7FtzRhbTCyBFdyOYJc5o2qZpKwBYOYL1R2CMrI9JI5eBWsylsXmx0dRIQDkoCWNbhP6u3rtn4LygwXakD3of7rfBM0P7s5S7JxyC%2BRStbpBweQXqR%2BhGu4I7lTmU4WnCxhrtyhMCCw3MNy4bTltJ5htuUSBOEdUbP%2FvL7W%2BGYFzz4285%2FNFt55zV30%2BpYgwMAqCJKrI9rfsrOMKWIk%2F4xfbHyfIQ6%2Bj88B0xluS80sSzq4YjYlcBs1psTTSAlQLqhMkqfhfYX%2B65cIPqYWf5CjoiGjdXZVDBaHdM9PzTd%2BulijnobXnhumI1pbrcldbLIB7EmGCSLT7Al%2F0P2%2B3Fo2R5%2FUrkXhkH%2FIKvj6e%2Fs4hLkXSB9Dckni%2BGgrE3Y6DYZ1TIO%2FRCK%2BeZ%2BmdfEL8QUApuZMpJezEts55zdTm5a%2BR3U1Mf7ENvCPvWdOdPMu95Ittmhpqjg9stBJCkUCjvtm9OnpluWN4mLCiH%2Fhiad7dONc8q3n%2BT2QJfoDM%2FaI%2BXX1zrpdHUsqk8SJ31aNaAbcJem%2FXqp64%2FkFruE0nI8WcO9q9qwme98TLt6b92ftwnT6q9C4VZR%2Fv9sQcfHJP%2F2udjA2MpY2HNRlsdbIl%2FTwKAIqx1C1VUswG8k93nyKKj9P2tAS%2Bypp0uhnGMI%2FmZY8ejCaeNQgfavDA8hH2%2BwdDC4RyNB49zVesH23xDoz7v%2BrSRFUkHTrx8lWDW5pDZjnsbO26Tlbm7KYv1v5dTedeuEx5X9eTcvxBx3gaCLxdyZqdunckljc3McQNK5G3OOsnWFLAIXf5j1HQS1HaFj%2BArhnrrL5uAY4X5Pb%2BllAt4g4toFGrmVO8GwNSZ5rR4Y6msgDPe4vf%2FzfcMuO6HXql0Mp40xUfORMqkFDRltyF9CyoFkzGMeNInJZtwHnNyvcmxdYjvJTJuhgfxIvbgAHGV8IO%2FEc1f183Ulq4t%2BUKnQSBuvXiCW6M6UMBsLdohSlsUTOaYmNG4LwGPmLDKTjoj%2FcXDRNze%2B%2BJUsGWA91OALt1SN3rBrg7h%2FFwXKjn9lfm9iX0299Ywn%2FQRjqnkSJ%2BjtbU0Y61U4UL9DubeEchPpLB9mIiL6InjMiFbhfHOsTgMecI5aq8LWcsTJzlyF%2BOW1LcQfNlWCXapaN4WTW2N0k85%2B4UXVO%2FNdnAKsYeO04PkWyk6t92Jcox3PWy1teLuY%2BTk5DkY%2FpOCdIftfTv6qGhh2LfGTA40lLMhek3UYcGv7cpB1pYyEBDS0pcrdMm9G0m%2BpsqDY4MXSyMnrtE9rsj6wUhejKp4gP7llSN4wujYrgDvGr%2FNyU%2B4QQ9yE3w%2FPFVepuFdLoMWOvZXxvzppA%2Fkc4xoXpIB9vl0BMdDROKB5lE%2BeoAFqKgKw6y4efLMUwnD797d%2FswG4iCeHjkpbGJKl%2BNv6D2uZhu4NN7pTMciPzt0wCX7thDTusvF9J8xSiBgDq211viTfzhsos16zaiv66iyACyfJlGQgb5Tj0XsBnBPucJ%2Bv5blp3o5fGUC4BGjrO72LSP5HYYZBl86rSX%2FmZuS1%2B7cFQ8fPfNKkYs4FTkiCxyYJhnqx7SRzFEyKsiw%2BWBhu0T7r5Rt4au0Bx0J7P%2B78h93i%2FadqtigWwgDtxHdLGHvg19mPU3%2BVM0MF1zN%2BurnwU9Y0MfWmDP6qxmqwHWwo7YE6ee8yjsDydYS2tldgffVd9jhTGvH40JAucwkFPs5Ex%2Fz%2FKlw4NNfprpNOGSXXQbMKnJyYEkBhk%2Bzun4%2FqBsKh6zb9TVRBvOiwDdgNzLg6F7z%2F63fTmu6tl9WImY9w4JWrQ%2B4O60aFRbNg6gPg1dZIHSRzV%2FLPsNToIPQjvCIXoO9Omzgih%2FYKgkAinZQyCEcyXS7Ng1%2FtFBYalyBTX5oKT4JR8tMfoTWULagWJYTd15D%2BAD4TUGJEDfF1dHkubXMg4AEso13t48NGEM3DpiUOdIQ3XePuxhGMvLZ5wzcWai86NUK%2BDXhymUEET3y26a11tM1YwwTtzckDPZDHpBLLNQi9mXW1O8n%2BtGDW9FcEGaDnqunUMsJ3x0WgaD0arCynXG6yg5qp8e%2Fu30ZoCSLxdiAkADon63AJe4IylacoMKlPU6ADboOXLykfEeFgMMxYA%2B%2BdGUYXp4tCTiR4fF8EHUbDLMb6j2h3gk2HmDdMwksWM5PSz3jQnlDWD2OVzargv2AADuyHTSzT0W1pew6onDkVdeKHVDX5Eta0lrMQ5tGa9OtEsSqBPalSNrYQXcxUJc3ZG%2B2BR4CBPEQwNwljoHcxfrn9NGFHD%2F9sEeYE1fszRc3EbQ7AF70rWXZT%2F7oTAr0l8ES7BY02MxLrDPWdRrYETITmcgiMEIFW%2FVGNdssUEJ6gzEvQkrFVMmVMDojtpL5GFw9YmywY5HhO3ucgcJV1AsR063Lg%2FRYJr%2BM%2BtJu%2FWA2r2H98%2BCJC2pctZlzDeZFrXyXVFzdpAfLHmSy66aJjQ3DtDSSULGq5rIG0p472%2F7R2ncqcWj9UYQSkl2wDAKoZ86hhkvnjFW3MLg1YY51gje1Ar%2FD8ce5Jg8hAkVDVjXy3yDRvQ0gP8h7NTdYQqSXLpU8jOrTYEWAbmd0nl0iG9OfsvrtY3bvBe%2Bl42icxamxz9PpFiK%2FqGU79tbkFcmrDPV7A%2F4v7d8Q7MJTBSw371%2FFwIksL71MxxP5ihkW%2BWSzkCQmAWYzIVR%2F7%2FM2UToANiJ1nW3baOutKna1%2FgTbppTjouVW4tQrBNukwy8nYUWdOKZPyuvy%2Basn9GyeKUgAWUQRXfoQGeuCH4NKvb2wkwlA42qFil7SwPCyoYhPB%2F%2BsgkgmAwGlkI6de9GIPrQjHQP4v6T0NvOhZ5Av486pY5ZSR7xI3aXfpPwrtIqEqgKUBUG8YSJmfRcjuZk2TuZFvYtClXI6FOSt8usXD%2BNI76sVv3axj4gcy5G8WE%2BytwQ2vYv86Pk41D1EyBLkAkYJOvzshPVtLGJGUtwPulaUtwL%2F%2BobG2YCAv3k3j0I2UQRkgMfL3%2FPA%2BMVmp2vvIS%2BHH8zHPM98wuNoX%2Bs0EWMT08%2F31nhyU0D8uD4HN4D2gAU0%2BUC7XxU4H7rDFFv7E9qIwH3LRAhH47l7dqO6u9elqd9%2B38gg8ecxFeMe872WwungSBgLNaqlIuEYTQ5bB4qad39%2Fs9C0TnG1WPBn06OIHLCKmh9Q4j6soeUqw8i5SCbQLQJotxF6cPEU2s%2B9YoS%2BCgrDhgqdhlfw2LvIr1QF4lAbFG4b1lQx19%2BzYZ8%2FlI%2F5qGnCa2u54sLAJItCNyt90ofXSfRYlb8M4%2Fo3BzKF8vyf0qc3c0BqsZLWdCQYRulz2OUeGIrotjVav7epwnID%2BZHhtQR%2FEZPwxMN0zZPRtMjF4YuGMYndK%2F4gE2fZykGKCUGT%2FTzOev%2BcQQ9a7tfqpk0EjW%2FCoD0IX07irfFwIEjYN0a6IvpiiyGZ1%2BR5kRkKKEYXWBN0GFf27EVDwkMJb5CghueRbxJ3YTntobv35cFJyZShb7iTGSYDIGiQolh3AvWxO%2Bid5MohtVaQsXSMJNvTyWCv6dGyaM3LDLsoTs0LdnFRWuf5JFVTORZQcQE05IP9ZKlebmFcvusKLJyUqymz%2F%2FJstHNl9aR76U7j5IZsRW0DORgS2VzNFGsQFEvp5VhrLuueKLcvyU%2FkeTUAoAumlTqjRg8zrhVrLiNyfeG%2Bb8sTsqoTC0XTmy59JSb7%2FFKo%2BihTakqNNhaDsXMb7B8ArNksKSdjjjW0dJZrqAxx548ZL9L3zcWUcZOQgSaxI2pDm4LP%2Bu0Ol3mgfS3emO7Zko9HJ6oEERkwcL8tERng8FRhNQtQJESWrGqW&__VIEWSTATEGENERATOR=532221C7&__VIEWSTATEENCRYPTED=&__EVENTVALIDATION=Ie4FSQBfl6m%2FZJPDC23Vn%2BhzQyuVtPbdQ4cbvtkmQaVrRx5M0Gx%2F3jwD28Aw65kHaCoK6OIBz76eF6sSzhySWMqceRYwr3ezNhylgxz68Bf0yvBloWPnUawU927fhnCiQJyKvsbXaIQY7%2BGlXXES9WVpzSQ%3D&txtBldg_Name_No=%E6%9D%BE%E8%8C%82%E5%BE%A1%E9%BE%99%E6%B9%BE%E9%9B%85%E8%8B%91&txtOwner_Name=&txtParcel_No=&txtUnit_No=&ddlPageCount="+str(page_size)+"&' --compressed -o " + filename

        print cmd
        ret = os.popen(cmd).readlines()
        if len(ret) > 0 and int(ret[0]) > 400:
            print "Wrong id: %s, remove filename: %s" % (page_num, filename)
            if filename == '/':
                break
            remove_cmd = 'rm -rf %s' % filename
            os.popen(remove_cmd)
        else:
            print "Right id: %s, store filename: %s" % (page_num, filename)

        print "\n"
        time.sleep(1)

if __name__ == '__main__':
    main()
