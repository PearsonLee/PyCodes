#coding:utf-8
'''
Created on

@author: PearsonLee
'''

import templates

g1 = templates.LinuxTemplate()
g1.group_name = 'Test groups'
g1.hosts = ['192.168.23.123','10.168.44.3']

#----

g2 = templates.LinuxTemplate()
g2.group_name = 'puppet server groups'
g2.hosts = ['202.104.5.34','10.168.44.3']


monitored_groups=[g1,g2
                  ] #??
#解释说，只要导入这个列表，就可以知道哪些模板已经启用了