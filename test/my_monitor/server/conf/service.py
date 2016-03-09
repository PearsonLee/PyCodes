#coding:utf-8

class BaseService(object):
    def __init__(self):
        self.name = 'YourServiceName'
        self.interval = 300
        self.plugin_name = 'YourPlugin_name'
        self.services = []
        self.trigger = {}


