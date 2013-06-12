#!/usr/bin/python
#encoding: utf8
#重载操作符的学习例子

__author__ = 'StoneInRain'


class mylist(list):
    #定义mylist的’-‘运算符
    def __sub__(self, b):
        a = self[:]
        b = b[:]
        while len(b) > 0:
            element = b.pop()
            if element in a:
                a.remove(element)
        return a

if __name__ == '__main__':
    print mylist([1, 2, 3]) - mylist([3, 4, 5])
