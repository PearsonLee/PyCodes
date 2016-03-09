#coding:utf-8
'''
Created on 2016��2��28��

@author: PearsonLee
'''

import generic
from data_process import avg,hit,last
class cpu(generic.BaseService):
    def __init__(self):
        super(cpu,self).__init__()
        self.name = 'linux_cpu'
        self.interval = 30
        self.plugin_name = 'get_cpu_status'
        self.triggers = {
                'idle':{'func':avg,
                        'minutes':15,
                        'operator':'lt', #<
                        'warning':20,
                        'critical':5,
                        'data_type':'percentage'
                        },
                'iowait':{'func':hit,
                          'minutes':10,
                          'operator':'gt',#>
                          'threshold':3,
                          'warning':50,#如果hit三次50就warning
                          'critical':80,#如果hit三次80就critical
                          'data_type':'int'
                          },
                         }
        
class memory(generic.BaseService):
    def __init__(self):
        super(memory,self).__init__()
        self.name = 'linux_memory'
        self.interval = 30
        self.plugin_name = 'get_memory_info'
        self.triggers = {
                'usage':{'func':avg,
                         'minutes':15,
                         'operator':'gt',
                         'warning':80,
                         'critical':90,
                         'data_tpye':'percentage'
                         }
                         }
        
        
if __name__ == '__main__':
    c = cpu()
    print c.name,c.interval,c.plugin_name