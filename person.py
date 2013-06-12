#!/usr/bin/python
#encoding: utf8
#面向对象编程的学习例子

__author__ = 'StoneInRain'


class Person():
    def __init__(self, name = ''):
        print '调用 Person 类的构造函数'
        self.name = name

    def display(self):
        print self.name
