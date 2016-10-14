# -*- coding:utf-8 -*-

import pickle

money = 15000.0
bank_money = 0.0
r_money = [money, bank_money]
bill = []

info = '''
            welcom to Online-Bank
            请选择你想执行的功能：
            1.存款
            2.提现
            3.查询账单（查询当日消费记录）
            4.退出
            （本银行会在每月最后一天出月账单，提现收取手续费：%5 。
                特别说明：每月10号为还款日，逾期未还，按欠款额%5计息)

    '''

def save_money(money):
    s_money = int(raw_input('请输入存款金额：'))
    money += s_money
    r_money[0] = money
    bill.append('存款成功！\n你的余额为：￥%s' % money)
    print bill[-1]

def take_money(money, bank_money):
    t_money = int(raw_input('请输入提现金额：'))
    money -= t_money + t_money * 0.05
    bank_money += t_money * 0.05
    r_money[0], r_money[1] = money, bank_money
    bill.append('成功提现 %s 元！你的余额为： ￥%s' %(t_money, money))
    print bill[-1]

def query_bill(bill):
    print '账单明细：'
    bill = load_file(bill, 'bill.txt')
    for item in bill:
        print item

def record_file(list, filename):
    with open(filename, 'w') as f:
        pickle.dump(list, f)

def load_file(list, filename):
    with open(filename, 'r') as f:
        list = pickle.load(f)
        return list

if __name__ == '__main__':

    while True:
        r_money = load_file(r_money, 'money.txt')
        money = r_money[0]
        bank_money = r_money[1]

        print info
        print '你的余额为：  ￥%s' % money

        choose = raw_input('请输入你的选项：')


        bill = load_file(bill, 'bill.txt')

        if choose == '1':
            save_money(money)
        elif choose == '2':
            take_money(money, bank_money)
        elif choose == '3':
            query_bill(bill)
        elif choose == '4':
            print '欢迎再次光临'
            break
        else:
            print 'your input is wrong'

        record_file(r_money, 'money.txt')
        record_file(bill, 'bill.txt')
















