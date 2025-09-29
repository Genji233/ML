import numpy as np
import pylab as plt

data=np.loadtxt('REG\olympic.txt',delimiter=',')
print(data)
print('ok')
x=data[:,0]
t=data[:,1]
plt.scatter(x,t)
plt.xlabel('Year')
plt.ylabel('Time(seconds)')
plt.show()