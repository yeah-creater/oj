import random

def rndChar():
        """
        生成随机字母   
        :return:
        """
        return chr(random.randint(65, 90))

def rndName(length):
    res = ''
    for i in range(0, length):
        res += rndChar()
    return res