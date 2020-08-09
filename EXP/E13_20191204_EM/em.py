# -*- coding: utf-8 -*-
# 高斯混合模型  使用EM算法解算
# 数据集：《机器学习》--西瓜数据4.0   :文件watermelon4.txt
import numpy as np
import matplotlib.pyplot as plt

# 预处理数据
def loadData(filename):
    dataSet = []
    tags = []
    fr = open(filename)
    for line in fr.readlines():
        curLine = line.strip().split(' ')
        tags.append(curLine[0])
        fltLine = list(map(float, curLine[1:]))
        dataSet.append(fltLine)
    return dataSet, tags

# 高斯分布的概率密度函数
def prob(x, mu, sigma):
    n = np.shape(x)[1]
    expOn = float(-0.5 * (x - mu) * (sigma.I) * ((x - mu).T))
    divBy = pow(2 * np.pi, n / 2) * pow(np.linalg.det(sigma), 0.5)  # np.linalg.det 计算矩阵的行列式
    return pow(np.e, expOn) / divBy

# EM算法
def EM(dataMat, maxIter=50):
    m, n = np.shape(dataMat)
    # 1.初始化各高斯混合成分参数
    alpha = [1 / 3, 1 / 3, 1 / 3]   # 1.1初始化 alpha1=alpha2=alpha3=1/3
    mu = np.concatenate([dataMat[0], dataMat[8], dataMat[15]]) # 1.2初始化 mu1=x0,mu2=x8,mu3=x15
    sigma = [np.mat(np.eye(7)*0.1) for x in range(3)]    # 1.3初始化协方差矩阵
    gamma = np.mat(np.zeros((m, 3)))
    for i in range(maxIter):
        '''
          E-step
          计算gamma(z_nk)
        '''
        for j in range(m):
            sumAlphaMulP = 0
            for k in range(3):
                # 混合系数需要加上对角矩阵，保证非奇异
                gamma[j, k] = alpha[k] * prob(dataMat[j, :], mu[k], sigma[k]+np.eye(7)*10) # 4.计算混合成分生成的后验概率，即gamma
                sumAlphaMulP += gamma[j, k]
            for k in range(3):
                gamma[j, k] /= sumAlphaMulP
        '''
          M-step
          计算N_k
        '''
        sumGamma = np.sum(gamma, axis=0)

        for k in range(3):
            mu[k] = np.mat(np.zeros((1, n)))
            sigma[k] = np.mat(np.zeros((n, n)))
            # 计算mu(new)
            for j in range(m):
                mu[k] += gamma[j, k] * dataMat[j, :]
            mu[k] /= sumGamma[0, k] #  7.计算新均值向量
            
            # 计算sigma(new)
            for j in range(m):
                sigma[k] += gamma[j, k] * (dataMat[j, :] - mu[k]).T *(dataMat[j, :] - mu[k])
            sigma[k] /= sumGamma[0, k]  # 8. 计算新的协方差矩阵
            # 计算pi(new) 混合系数
            alpha[k] = sumGamma[0, k] / m   # 9. 计算新混合系数
    return gamma

def gaussianCluster(dataMat,countries):
    m, n = np.shape(dataMat)
    gamma = EM(dataMat)
    country_class = {}
    country_class[1] = [];country_class[2] = [];country_class[0] = []
    for i in range(m):
        # amx返回矩阵最大值，argmax返回矩阵最大值所在下标
        index = np.argmax(gamma[i,:])
        country_class[index].append(countries[i])
    print("first class:",country_class[2])
    print("second class:",country_class[1])
    print("third class",country_class[0])

if __name__=="__main__":
    dataSet,countries = loadData('data')
    dataMat = np.mat(dataSet)
    gaussianCluster(dataMat,countries)