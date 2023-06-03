import scipy.io
import scipy.optimize as opt
import matplotlib.pyplot as plt
import numpy as np

h=0.01
lamda=0.01
N=21
def K(X,Y):
    return np.exp(-np.linalg.norm(X-Y)**2/h)

def phiCap(X,a,b):
    p =0
    #a = -np.random.rand(N)
    #b = -np.random.rand(N)
    for i in range(N):
        p+=a[i]*K(X,stars[i])
    for j in range(N):
        p+=b[j]*K(X,circles[j])  
    return p
def costFunc(array):    
    result =0
    a = array[:21]
    b = array[21:]
    for i in range(N):
        result += (1-phiCap(stars[i],a,b))**2 + (1+phiCap(circles[i],a,b))**2
         
    return result #+ lamda*np.linalg.norm(phiCap(X,a,b))
#Loading Data
mat = scipy.io.loadmat('data32.mat')
circles = mat["circles"]
stars = mat["stars"]

#find values for min cost
'''
arr= opt.fmin(costFunc,np.zeros(42))
print("a:")
print(arr[:21])
print("b:")
print(arr[21:])
'''
#values:
a= np.array([ 0.40267311,  0.28606604, -0.9834851,  -0.48576739,  0.76151339, -0.3229498,
 -0.02163259,  1.17523948,  0.38298694,  0.50975124,  1.07909588,  0.32292768,
  0.43501049,  0.9158626,   0.47798068, -0.62575489, 1.73819703,  0.66911578,
  0.59550498,  0.76312006, -0.14991878])
b= np.array([-0.54650714,  0.69192763, -0.11934415, -0.55431429, -0.07531737,  0.01466469,
 -0.67869012,  0.14139892, -0.1585538,  -0.54925551, -1.11180782,  0.00727298,
 -0.96845822, -0.96038691, -0.63398909,  0.48366704, -0.6146408,  -0.5116254,
 -1.98406113,  0.90890189,  0.19615515])

Xi=np.empty(N)
Xj=np.empty(N)
for i in range(N):
    Xi[i] = phiCap(circles[i],a,b)
    Xj[i]  = phiCap(stars[i],a,b)
plt.plot(circles[:,0], circles[:,1],marker='o',linestyle='')
plt.plot(stars[:,0],stars[:,1],marker='o',linestyle='')
plt.show()
plt.plot(np.linspace(-1,1,N), Xi,marker='o',linestyle='')
plt.plot(np.linspace(-1,1,N), Xj,marker='o',linestyle='')
plt.xticks([])


