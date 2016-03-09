'''
Created on 2016年2月28日

@author: PearsonLee
'''
import pickle
import serialize

def action_process(server_instance,msg):
    
    msg = pickle.load(msg[2]) # parse_respone()接收过来的是一个列表，前两个元素并不是真正的信息所以直接去第三个元素内容
    print msg
    func_name = msg.keys()[0]
    func = getattr(serialize,func_name)#通过反射的方式在serialize这个模块下取出func_name对应的函数
    func(server_instance,msg[func_name])#然后运行这个函数
    