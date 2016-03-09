#coding:utf-8
'''
Created on 2016Äê2ÔÂ28ÈÕ

@author: PearsonLee
'''

class BaseService(object):
    def __init__(self):
        self.name = 'BaseService'
        self.interval = 300
        self.last_time = 0
        self.plugin_name = 'your_plugin_name'
        self.triggers = {}