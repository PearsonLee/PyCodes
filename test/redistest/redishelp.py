#coding:utf-8

import redis

class RedisHelper(object):
    def __init__(self):
        self.__chan = redis.Redis(host='127.0.0.1')
        self.chan_sub = 'xxx'
        self.chan_pub = 'xxx'

    def set(self,key,value):
        self.__chan.set(key,value)

    def get(self,key):
        return self.__chan.get(key)

    def subscribe(self):
        sub = self.__chan.pubsub()
        sub.subscribe(self.chan_sub)
        sub.get_message()
        return sub


    def publish(self,msg):
        self.__chan.publish(self.chan_pub,msg)


