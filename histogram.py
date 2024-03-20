import matplotlib.pyplot as plt

x = [1,5,2,3,8,9,6,4,5,7,3,1,2,9,5,2,5,0,9,4,]
plt.hist(x, bins=10,color='red',alpha=0.7)
plt.show()