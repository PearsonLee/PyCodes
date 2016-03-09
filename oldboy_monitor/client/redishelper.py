'''
Created on 2016Äê2ÔÂ29ÈÕ

@author: PearsonLee
'''
import redis

class RedisHelper(object):

    def __init__(self):
        self.__conn = redis.Redis(host='127.0.0.1')
        self.chan_sub = 'fm104'
        self.chan_pub = 'fm104'
    def get(self,key):
        return self.__conn.get(key)

    def set(self,key,value):
        self.__conn.set(key,value)

    def public(self,msg):
        self.__conn.publish(self.chan_pub,msg)
        return True
    def subscribe(self):
        pub = self.__conn.pubsub()
        pub.subscribe(self.chan_sub)
        pub.parse_response()
        return pub

if __name__ == '__main__':
    t = RedisHelper()
    t.public('test')