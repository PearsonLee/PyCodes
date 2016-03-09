# coding:utf-8

import global_settings #导入项目根目录
from conf import hosts
import time
import pickle
from redishelper import RedisHelper
#from monitor.server.conf.hosts import monitored_groups

def host_config_serialize(host_ip):
    applied_services = []
    configs = {
               'services':{}
               }
    for group in hosts.monitored_groups:
        if host_ip in group.hosts:
            applied_services.extend(group.services)#list.extend(D)将指定列表D中的元素追加到list中，合并为一个列表
    applied_services = set(applied_services) #去重，当一个主机在多个不同模板中都有时，为防止不同模板中存在相同服务项，所以需要去重，set（集合）有去重的功能        
    
    for service in applied_services:
        service = service() #因为在templates我们可以看到，service是类，我们需要对类实例化才能其对象属性
        configs['services'][service.name] = [service.interval,
                                             service.plugin_name,
                                             0
                                             ]
    return configs

def all_host_configs():
    configs = {'hosts':{}}
    for group in hosts.monitored_groups:
        for host_ip in group.hosts:
            configs['hosts'][host_ip] = {}
            
    return configs


def report_service_data(server_instance,msg):
    host_ip = msg['ip']
    service_status_data = msg['data']
    service_name = msg['service_name']
    
    server_instance.hosts['hosts'][host_ip][service_name] = {
                    'data':service_status_data,
                    'time_stamp':time.time()
                    }
    key = 'StatusData::%s' %host_ip
    server_instance.redis.set(key,pickle.dumps(server_instance))

def flush_all_host_configs_into_redis():
    applied_hosts = []
    redis = RedisHelper()
    for group in hosts.monitored_groups:
        applied_hosts.extend(group.hosts)
    applied_hosts = set(applied_hosts)
    
    for host_ip in applied_hosts:
        host_config = host_config_serialize(host_ip)
        #redis中只存字符串和数字，并不认识python的字典，所以需要序列化（序列化后就变成字符串了），因为这个程序都是用python写的，而且pickle可以序列化的数据类型比较多
        key = 'HostConfig::%s' %host_ip #给这个key加一个标识，这样以后添加其他信息时方便区分识别
        redis.set(key,pickle.dumps(host_config))
    return True

#用于测试
if __name__ == '__main__':
   #host_config_serialize('192.168.182.134')
   flush_all_host_configs_into_redis()