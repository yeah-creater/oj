#定义elo score 等级评分类


# Ra：A玩家当前的积分 
# Rb：B玩家当前的积分 
# Sa：实际胜负值，胜=1，平=0.5，负=0 
# Ea：预期A选手的胜负值，Ea=1/(1+10^[(Rb-Ra)/400]) 
# Eb：预期B选手的胜负值，Eb=1/(1+10^[(Ra-Rb)/400]) 
# 因为E值也为预估，则Ea+ Eb=1 
class EloScore:

    #定义胜负关系 win:1 tie:0.5 lose:0
    ELO_RESULT = 0

    #排名
    ratingA = 0
    ratingB = 0

    #定义初始化方法
    def __init__(self,ratingA,ratingB,result):
        self.ratingA = ratingA
        self.ratingB = ratingB
        self.ELO_RESULT = result
    #定义阈值 k值
    def computeK(self):
        return 36

    #使用公式推算
    def computeHope(self):
        return 1 / (1+pow(10,(self.ratingB-self.ratingA)/400))

    def computeScore(self):
        return self.computeK() * (self.ELO_RESULT - self.computeHope())

if __name__ == "__main__":
    #实例化一个比较对象 
    eloscore = EloScore(1800,2500,0)
    #打印胜率
    print(eloscore.computeScore())

