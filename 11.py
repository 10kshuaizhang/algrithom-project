import matplotlib.pyplot as plt 

v1 = [1,2,3,4 ]
v2 = [1,2,3,4 ]
plt.scatter(v1,v2,linewidths= 1,alpha = 0.5,color = 'blue')
v3 = [4,3,2,1 ]
v4 = [8,6,4,2 ]
plt.scatter(v3,v4,linewidths= 1,alpha = 0.5,color = 'yellow')

plt.show()