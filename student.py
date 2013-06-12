#!/usr/bin/python
#coding: utf8
#面向对象编程的学习例子
__author__ = 'StoneInRain'

import person


class Student(person.Person):

    university = 'Tsinghua University'

    def __init__(self, name = '', no = int()):
        print '调用 Student 类的构造函数'
        person.Person.__init__(self, name)
        self.no = no

    def display(self):
        person.Person.display(self)
        print self.no
        print self.university

if __name__ == '__main__':
    zhou1 = Student('周宇峰', 2011210778)
    zhou1.display()

    zhou2 = Student('周宇峰', 200632580289)

    zhou1.university = 'Whuhan University'

    zhou2.display()




