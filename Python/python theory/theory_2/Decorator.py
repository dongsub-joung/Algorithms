#일반형 Decorator
'''
def hello(func):
    def decorated():
        print('Hello!')
        func()
        print('Nice to Meet you!')
    return decorated

@hello
def name():
    print('Joung Dong Sub')
name()
'''

#class화
#Decorator.py
from datetime import datetime

class TimeCost():
    def __init__(self,func):
        self.func= func

    def __call__(self):
        start= datetime.now()
        self.func()
        end= datetime.now()
        print('timecost:', end - start)

#-----------------------------------------------------------------------

from Decorator import TimeCost 
import time

__print_string= 'hello! this is task'

@TimeCost
def task1():
    time.sleep(3)
    print('hello! this is task 1')

@TimeCost
def task2():
    time.sleep(5)
    print('hello! this is task 2')

@TimeCost
def task3():
    time.sleep(2)
    print('hello! this is task 3')