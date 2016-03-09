#coding:utf-8
'''
Created on 2016年2月28日

@author: PearsonLee
'''

import global_settings
from redishelper import RedisHelper
import serialize

import action_process
from _sre import MAGIC

class MonitorServer(object):
    def __init__(self,ip,port):
        self.ip = ip
        self.port = port
        self.hosts = serialize.all_host_configs()
        self.redis = RedisHelper()
        
    def handle(self):
        redis_sub = self.redis.subscribe()
        #redis_sub.parse_response()
        while True:
            msg = redis_sub.parse_response()
            print 'recv:',msg
            action_process.action_process(self,msg)#把self传过去的好处是，在另一个模块中也可以调用这个模块中已经生成的实例，而不需要再重新实例化出一个新的实例，相当于把实例传过去
            print '---waiting for new msg---'
            
            for host,val in self.hosts['hosts'].items():
                print host,val
                
    def run(self):
        print '---starting monitor server---'
        self.handle()
        
    def process(self):
        pass
    
if __name__ == '__main__':
    s = MonitorServer('0.0.0.0','8000')#redis_ip,port
    s.run()