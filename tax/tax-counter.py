#!/usr/bin/python
# -*- coding:UTF-8 -*-
# 房屋交易税费计算器

def counting_tax_zengzhi(info):
    if info['years'] >= 2 and info['normal'] == True:
        return 0
    else:
        return (info['sale_price']-info['beian_price'])/1.05*0.05

def counting_tax_qi(info, tax_zengzhi):
    tax_point = 0.01
    if info['size'] > 90:
        tax_point = 0.015
        
    return (info['sale_price']-tax_zengzhi)*tax_point

def counting_tax_ge(info, zengzhi):
    if info['years'] >= 5 and info['only_one'] == True:
        return 0

    tax_point = 0.01
    if info.normal == True:
        tax_point = 0.015

    return (info['sale_price']-tax_zengzhi)*tax_point

def main():
    '''
    info = {
        'sale_price': 9600000,
        'beian_price': 6030000,
        'years': 5,
        'size': 127,
        'normal': True,
        'only_one': True,
        }
    '''
    info = {
        'sale_price': 9600000,
        'beian_price': ,
        'years': 5,
        'size': 127,
        'normal': True,
        'only_one': True,
        }

    tax_zengzhi = counting_tax_zengzhi(info)
    tax_qi = counting_tax_qi(info, tax_zengzhi)
    tax_ge = counting_tax_ge(info,tax_zengzhi)

    print tax_zengzhi, tax_qi, tax_ge

if __name__=='__main__':
    main()
