'''
Created on 2016��2��28��

@author: PearsonLee
'''
import pickle
import serialize

def action_process(server_instance,msg):
    
    msg = pickle.load(msg[2]) # parse_respone()���չ�������һ���б�ǰ����Ԫ�ز�������������Ϣ����ֱ��ȥ������Ԫ������
    print msg
    func_name = msg.keys()[0]
    func = getattr(serialize,func_name)#ͨ������ķ�ʽ��serialize���ģ����ȡ��func_name��Ӧ�ĺ���
    func(server_instance,msg[func_name])#Ȼ�������������
    