# -*- coding:utf-8 -*-
import re
from termcolor import *

def get_query_result(file_path, pattern):
    query_result = []
    f = open(file_path)
    for line in f.readlines():
        if __is_matchable(line, pattern):
            query_result.append(line)
        f.close()
    return query_result

def __is_matchable(string, pattern):
    str_pattern = re.compile(pattern)
    if str_pattern.findall(string):
        return True
    return False


if __name__ == '__main__':
    print 'welcome 员工信息查询系统'
    pattern = raw_input('请输入查询关键字：')

    result = get_query_result('info.txt', pattern)

    for i in result:
        print colored(i, 'green')





