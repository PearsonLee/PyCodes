#coding:utf-8
'''
Created on 2016年2月29日

@author: PearsonLee
'''
import threading
import pickle
import time
from redishelper import RedisHelper
from plugins import plugin_api

#理论上host_ip应该写在配置文件中
host_ip = '192.168.182.134'


class MonitorClient(object):
    def __init__(self,server,port):
        self.server = server#服务器端ip
        self.port = port#端口
        self.configs = {}#获取配置信息
        self.redis = RedisHelper()
    
    #将传过来的数据序列化
    def format_msg(self,key,value):
        msg = {key,value}
        return pickle.dumps(msg)
        
    def get_configs(self):
        config = self.redis.get('HostConfig::%s'%host_ip)
        if config:
            self.configs = pickle.loads(config)
            return True
        
    def handle(self):
        if self.get_configs():
            print '---going to monitor services---',self.configs
            
            while True:
                for service_name, val in self.configs['servcies'].item():
                    interval,plugin_name,last_check = val
                    if time.time() - last_check >= interval:
                    #need to kick off the next run
                        #启动一个线程，这个线程完成对相关信息的监控并返回给服务器的任务
                        t = threading.Thread(target=self.task,args=[service_name,plugin_name])
                        t.start()
                        self.configs['services'][service_name][2] = time.time() #update last check time
                    else:
                        next_run_time = interval - (time.time() - last_check)
                        
                        print '\033[32;1m%s\033[0m will be run in next \033[32;1m%s\033[0m seconds'%(service_name,next_run_time)
                #将所有的服务循环完一遍后，停1s
                time.sleep(1)            
        else:
            print '---could not found any configurations for this hosts---'
    
    #修改该方法，使其负责完成监控，收集客户端信息然后发到服务器端的任务
    def task(self,servcie_name,plugin_name):
        print '---going to run service:',servcie_name,plugin_name
        #通过反射的方式从plugin_api中，取出获取的同名字符串插件方法。
        func = getattr(plugin_api, plugin_name)
        result = func() # 然后执行方法
        #方法得到的结果为字典类型，所以需要序列化然后存到redis中
        #self.redis.public(pickle.dumps(result))
        msg = self.format_msg('report_service_data',
                              {'ip':host_ip,
                               'service_name':servcie_name,
                               'data':result,
                               }
                              )
        #上面的‘report_service_data’告诉服务端这发送的是监控信息，这样做的好处是细化了功能，
        #上面的一系列操作不仅可以用来监控数据，还可以做例如传文件的功能，所以为以后扩展功能预留空间。
        self.redis.public(msg)
        
    def run(self):
        self.handle()
    
if __name__ == '__main__':
    cli = MonitorClient('yourMonitorServerIP','port')
    cli.run()#守护进程在运行
        