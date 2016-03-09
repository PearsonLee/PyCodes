#coding:utf-8
'''
@author: PearsonLee
'''

from services import linux

class BaseTemplate(object):
    def __init__(self):
        self.name = 'YourTemplateName'
        self.group_name = 'YourGroupName'
        self.hosts = []
        self.services = [] #提供的服务

class LinuxTemplate(object):
    def __init__(self):
        super(LinuxTemplate,self).__init__()
        self.name = 'LinuxTemplate'
        self.services = [
                linux.cpu,
                linux.memory,
                        ]

