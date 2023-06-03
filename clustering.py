import scipy.io
import matplotlib.pyplot as plt
import numpy as np
import random as rnd

K=200
#Loading Data
mat = scipy.io.loadmat('data33.mat')
X = mat["X"]

#pick random Z1,Z2
index1 = rnd.randint(0,K-1)
Z1 = X[:,index1]
index2 = rnd.randint(0,K-1)
while index1 == index2:
    index2 = rnd.randint(0,K)
Z2 = X[:, index2]
C1=[]
C2=[]

#K-means loop
while True:
    C1old = C1
    C2old = C2
    Z1old = Z1
    Z2old = Z2
    C1=[]
    C2=[]
    for x in X.T:
        if np.linalg.norm(x**2-Z1**2)**2<=np.linalg.norm(x**2-Z2**2)**2:
            C1.append(x)
        else: C2.append(x)
    C1=np.array(C1)
    C2=np.array(C2)
    Z1= np.array([np.mean(C1[0]),np.mean(C1[1])])
    Z2= np.array([np.mean(C2[0]),np.mean(C2[1])])
    if np.array_equal(C1old,C1) and np.array_equal(C2old,C2) and np.array_equal(Z1old,Z1) and np.array_equal(Z2old,Z2):
        break

#Check errors:
flag=0
errors = 0
for x in C1:
    if x not in X.T[:100]:
        errors+=1
for x in C2:
    if x not in X.T[100:]:
        errors+=1    
if errors > K/2:
    flag=1
    errors = K - errors
p = (errors)/K*100
print(f'error rate = {p}%')

plt.plot(X[0,:100],X[1,:100],marker='o',markerfacecolor='red',markeredgecolor='none',linestyle='')
plt.plot(X[0,100:],X[1,100:],marker='o',markerfacecolor='blue',markeredgecolor='none',linestyle='')
if flag==0:
    plt.plot(C1[:,0],C1[:,1],marker='o',markerfacecolor='none',markeredgecolor='red',linestyle='')
    plt.plot(C2[:,0],C2[:,1],marker='o',markerfacecolor='none',markeredgecolor='blue',linestyle='')
if flag==1:
    plt.plot(C1[:,0],C1[:,1],marker='o',markerfacecolor='none',markeredgecolor='blue',linestyle='')
    plt.plot(C2[:,0],C2[:,1],marker='o',markerfacecolor='none',markeredgecolor='red',linestyle='')
