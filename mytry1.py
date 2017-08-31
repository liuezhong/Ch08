import regression
from numpy import *
# xArr, yArr = regression.loadDataSet('ex0.txt')
# ws = regression.standRegres(xArr,yArr)
# print(ws)

# print(regression.lwlr(xArr[0],xArr,yArr,0.01))

# yHat = regression.lwlrTest(xArr,xArr,yArr,0.003)
# print(yHat)

# xMat = mat(xArr)
# srtInd = xMat[:,1].argsort(0)
# xSort = xMat[srtInd][:,0,:]
# print(srtInd)
# print(xSort)

xArr, yArr = regression.loadDataSet('abalone.txt')
# print(regression.stageWise(xArr,yArr,0.01,200))

# lgX=[];lgY=[]
# regression.setDataCollect(lgX,lgY)

regression.crossValidation(xArr,yArr)