import regression
import matplotlib.pyplot as plt
abX, abY = regression.loadDataSet('abalone.txt')
# print(abX)
# print(abY)
ridgeWeights = regression.ridgeTest(abX,abY)
print(ridgeWeights)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(ridgeWeights)
plt.show()