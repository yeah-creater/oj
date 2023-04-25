
import os
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

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oj.settings')
    import django
    django.setup()
    from Backend.models.user.user import UserInfo
    from Backend.models.contest.contest import Contest
    from Backend.models.contest.contest import ContestParticipant
    print('请输入你要结算的竞赛编号:',end = '')
    n = int(input())
    if not Contest.objects.filter(id = n).exists() or Contest.objects.get(id = n).clear:
        print('该竞赛编号不存在或已计算积分')
    else:
        participants = ContestParticipant.objects.filter(contest = n)
        dic = {id:0 for id in range(1,10000)}
        for pa in participants:
            for pb in participants:
                if pa.id != pb.id:
                    result = 0.5
                    if pa.score > pb.score or (pa.score == pb.score and pa.penalty < pb.penalty):
                        result = 1
                    elif pb.score > pa.score or (pa.score == pb.score and pa.penalty > pb.penalty):
                        result = 0
                    els = EloScore(pa.user.user_info.rating, pb.user.user_info.rating,result)
                    dic[pa.user.user_info.id] += els.computeScore()
        for i in range(1,10000):
            if dic[i] != 0:
                rating = UserInfo.objects.get(id = i).rating
                UserInfo.objects.filter(id = i).update(rating = rating + dic[i])
        Contest.objects.filter(id = n).update(clear = True)
    