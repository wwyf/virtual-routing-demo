'''
utilities functions here
'''
import json
import socket

def objEncode(obj):
    """ obj，返回binary对象 """
    return json.dumps(obj,indent=4, sort_keys=True,separators=(',',':')).encode('utf-8')

def objDecode(binary):
    """ binary 返回dict对象 """
    return json.loads(binary.decode('utf-8'))

def binary_to_beautiful_json(binary):
    """ binary数据转成漂亮的json格式化字符串,便于输出查看调试 """
    obj = objDecode(binary)
    return json.dumps(obj,indent=4, sort_keys=True)

def obj_to_beautiful_json(obj):
    """ obj数据转成漂亮的json格式化字符串，便于输出调试 """
    return json.dumps(obj,indent=4, sort_keys=True)

def get_host_ip():
    """得到本机IP"""
    try:
       s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
       s.connect(('8.8.8.8', 80))
       ip = s.getsockname()[0]
    finally:
       s.close()
    return ip

def get_subnet(ip:str, netmask:int):
    n1, n2, n3, n4 = ip.split('.')
    MASK = (2**netmask)-1
    if netmask <= 8:
        n1 = str(int(n1) & MASK)
        return '.'.join([str(n1), '0', '0', '0'])
    elif netmask <= 16:
        n2 = str(int(n2) & MASK)
        return '.'.join([n1, str(n2), '0', '0'])
    elif netmask <= 24:
        n3 = str(int(n3) & MASK)
        return '.'.join([n1, n2, n3, '0'])
    else:
        return '.'.join([n1, n2, n3, str(int(n4) & MASK)])