# -*- coding:utf-8 -*-

def outer(fun):
    def wrapper(args):
        print '验证'
        result = fun(args)

        return result

        print 'over'
    return wrapper

@outer
def fun1(args):
    print 'fun1'
    return args

@outer
def fun2():
    print 'fun2'

@outer
def fun3():
    print 'fun3'

response = fun1('k')
print response