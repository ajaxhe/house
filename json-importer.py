#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json
import os
import pymysql 
import sys

table_name='beian_info'

# ref-link:https://www.cnblogs.com/BlueSkyyj/p/10039972.html
class DataBaseHandle(object):
    ''' 定义一个 MySQL 操作类'''
    def __init__(self, host, port, user, password, db_name):
        '''初始化数据库信息并创建数据库连接'''
        # 下面的赋值其实可以省略，connect 时 直接使用形参即可
        self.host = host
        self.port = port
        self.user= user
        self.password = password
        self.db_name = db_name
        self.db = pymysql.connect(self.host,
            self.user,
            self.password,
            self.db_name,
            self.port,
            charset='utf8')

    def create_table(self, table_name=table_name):
        '''
        住宅
        "TFId":1346586,
        "XMId":23627,
        "LDId":25423,
        "GetTime":"\/Date(1559577600000)\/",
        "XM":"松茂御龙湾雅苑（二期）2栋",
        "XMMC":"松茂御龙湾雅苑（二期）",
        "HTH":"--",
        "LD":"2栋",
        "SZQ":"宝安",
        "HX":"四房住宅",
        "ZH":"8",
        "LC":"24",
        "FH":"2402",
        "YT":"住宅",
        "HNMJ":"224.11",
        "JZMJ":"272.79",
        "ZT":"初始登记",
        "BAJ":"90189.86",
        "BajInt":90189.86
        商业
        -"TFId":1346697,
        项目ID "XMId":23627,
        楼栋ID "LDId":25423,
        -"GetTime":"\/Date(1559577600000)\/",
        项目 "XM":"松茂御龙湾雅苑（二期）2栋",
        项目名称 "XMMC":"松茂御龙湾雅苑（二期）",
        合同号 "HTH":"--",
        楼栋 "LD":"2栋",
        深圳区 "SZQ":"宝安",
        户型 "HX":"商业",
        座号 "ZH":"--",
        楼层 "LC":"1",
        房号 "FH":"B01",
        用途 "YT":"商业",
        户内面积 "HNMJ":"63",
        建筑面积 "JZMJ":"64.46",
        状态 "ZT":"初始登记",
        备案价 "BAJ":"250000",
        备案价 "BajInt":250000.00 
        '''

        sql = u'''
		CREATE TABLE IF NOT EXISTS `%s`(
		 	`TFId` INT UNSIGNED NOT NULL,
		 	`XMId` INT UNSIGNED NOT NULL COMMENT '项目ID',
		 	`LDId` INT UNSIGNED NOT NULL COMMENT '楼栋',
			`XM` VARCHAR(100) COMMENT '项目',
			`XMMC` VARCHAR(100) COMMENT '项目名称',
			`HTH` VARCHAR(100) COMMENT '合同号',
			`LD` VARCHAR(10) COMMENT '楼栋',
			`SZQ` VARCHAR(20) COMMENT '深圳区',
			`HX` VARCHAR(20) COMMENT '户型',
			`ZH` VARCHAR(20) COMMENT '座号',
			`LC` VARCHAR(10) COMMENT '楼层',
			`FH` VARCHAR(10) COMMENT '房号',
			`YT` VARCHAR(10) COMMENT '用途',
			`HNMJ` FLOAT(10,2) NOT NULL COMMENT '户内面积',
			`JZMJ` FLOAT(10,2) NOT NULL COMMENT '建筑面积',
			`ZT` VARCHAR(10) COMMENT '状态',
			`BAJ` FLOAT(10,2)  NOT NULL COMMENT '备案价',
			`full_info` VARCHAR(1000) NOT NULL COMMENT '原始数据',
			PRIMARY KEY ( `TFID`,`XMID`,`LDID` )
			)ENGINE=InnoDB DEFAULT CHARSET=utf8;
		''' % (table_name)
        self.insert_db(sql)

    def insert_db(self, sql, values=None):
        ''' 插入数据库操作 '''
        self.cursor = self.db.cursor()

        try:
            # 执行sql
            if values:
                self.cursor.execute(sql, values)
            else:
                self.cursor.execute(sql)
            # tt = self.cursor.execute(sql)  # 返回 插入数据 条数 可以根据 返回值 判定处理结果
            # print(tt)
            self.db.commit()
        except Exception, err:
            # 发生错误时回滚
            print err
            self.db.rollback()
        finally:
            self.cursor.close()


def filter_dict(raw_dict):
    if raw_dict['XMId'] == 27168:
        # 华海金湾公馆一期数据异常，需要修正。33268-1-0-0.json: "TFId":1419639,"XMId":27168,"LDId":27663
        hnmj = float(raw_dict['HNMJ'])
        if raw_dict['ZH'] in ['A', 'C'] and hnmj <= 50:
            raw_dict['HNMJ'] = raw_dict['JZMJ']
            raw_dict['JZMJ'] = hnmj + float(raw_dict['JZMJ'])

    # 过滤无用的字段
    sql_keys = ['TFId','XMId','LDId','XM','XMMC','HTH','LD','SZQ','HX','ZH','LC','FH','YT','HNMJ','JZMJ','ZT','BAJ','full_info']
    sql_values = []
    for k in sql_keys:
        if k == 'full_info':
            v = json.dumps(raw_dict)
        elif k == 'HNMJ' or k == 'JZMJ' or k == 'BAJ':
            try:
                v = float(raw_dict[k])
            except Exception, err:
                print raw_dict[k], err
                v = 0
        else:
            v = raw_dict[k]

        sql_values.append(v)
	
    return sql_keys, sql_values


def gen_insert_sql(keys, table_name=table_name):
    placeholders = ', '.join(['%s']* len(keys))
    columns = ', '.join(keys)
    insert_sql =  "REPLACE INTO %s (%s) VALUES (%s)" % (table_name, columns, placeholders) 
    return insert_sql
	

def import_json_file(filename):
    with open(filename, 'r') as fp:
        raw_json = json.load(fp)

    db = DataBaseHandle(host='localhost', port=3306, user='house', password='9227179', db_name='house')
    db.create_table(table_name)

    count = 0 
    total_count = len(raw_json['list'])
    for d in raw_json['list']:
        sql_keys, sql_values = filter_dict(d)
        insert_sql = gen_insert_sql(sql_keys, table_name)
        db.insert_db(insert_sql, sql_values)	
        count = count + 1
        print '%d/%d' % (count, total_count)

def list_dir(path):
    filenames = []
    files = os.listdir(path)
    for f in files:
        filenames.append('%s%s' % (path, f))
    return filenames

def main(argv):
    json_file_path = argv[1]	
    if os.path.isfile(json_file_path):
        filenames = [json_file_path]
    else:
        filenames = list_dir(json_file_path)
    for f in filenames:
        print 'importing: %s' % f
        import_json_file(f)

if __name__ == '__main__':
    #python json-importer.py crawler/beian/data-20190609/33268-1-0-0.json 
    #python json-importer.py crawler/beian/data-20190609/
    #print sys.getdefaultencoding()
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main(sys.argv)
