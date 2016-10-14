# -*- coding:utf-8 -*-

class Person:
    money = 0.0
    emotional_sate = ''
    love_object = ''
    figure = '''
             ***
            *   *
             ***
         ***********
              *
             *  *
            *    *
    '''

    def __init__(self, name, age, sex, job, height):
        self.name = name
        self.age = age
        self.sex = sex
        self.job = job
        self.height = height

    def talk(self, words):
        print self.figure
        print self.name + ':' + words

    def love(self, lover):
        self.emotional_sate = '恋爱'
        self.love_object = lover

john = Person('john', 18, '男', '学生', 170)

liz = Person('liz', 18, '女', '学生', 165)
john.love(liz)
liz.love(john)

background = '''
    故事的开始：

        john and liz 是高中时的恋人，他们将马上面临高考，你将扮演john和liz度过接下来的人生...
'''

def stop():
    raw_input('请输入任意字符以继续***')

if __name__ == '__main__':
    print background
    john.talk('马上要高考了，我要努力学习和liz一起考上好大学')
    stop()
    liz.talk('john...')
    stop()
    john.talk('嗯？怎么了liz...')
    stop()
    liz.talk('马上要高考了。。。我们该怎么办。。。呜呜~~~~(>_<)~~~~')
    stop()
    john.talk('哎呀。。。')
    stop()
    john.talk('没事的，好了好了，我们一起努力学习，一定会考上好大学的！！！')
    stop()
    liz.talk('真的吗？ 如果。。。如果。。。考不上那怎么办')




