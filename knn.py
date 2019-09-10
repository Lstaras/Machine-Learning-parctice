from numpy import *
from collections import Counter
import operator

def createDataSet():
    group = ([1.0,1.1],[1.0,1.0],[0,0],[0,0.1])
    labels = ['A','A','B','B']
    return group,labels

def classify0(inX,dataSet,labels,k):
    # 用于分类的向量，样本集，标签集，k
    # 获取维度((((((((需要函数解决))))))))
    dataSetSize = 2
    # 获取样本个数
    dataSetNum = len(dataSet)
    print(dataSetNum)
    # 循环获取欧式距离
    d = {}
    for i in range(dataSetNum):
        print(dataSet[i][0],dataSet[i][1])
        x = dataSet[i][0] - inX[0]
        y = dataSet[i][1] - inX[1]
        dis = (x**2 + y**2)**0.5
        d[i] = dis
        print(d)
    # 根据k的值选择最小的k个点
    v = []
    sortD=sorted(d.items(),key=operator.itemgetter(1))
    print(sortD)
    for i in range(k):
        v.append(labels[sortD[i][0]])
        # l.append(labels[sortD.keys()[i]])
    # 判断最多出现的标签
    return  v

if __name__ == '__main__':
    group,labels = createDataSet()
    print(classify0([0,0],group,labels,3))