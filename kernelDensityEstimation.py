import numpy as np
import matplotlib.pyplot as plt

def K(X,h):
    return 1/np.sqrt(2*np.pi*h)*np.exp(-(1/(2*h))*(X**2))
N=1000
h=0.1
for k in range(6):
    X = np.empty(N)
    x = np.linspace(-0.5,1.5,N) 
    f = np.empty((N)) 
    for i in range(N):
        for j in range(N):
            X[i]=np.random.uniform(0,1)
            f[i] += K(x[i]-X[j],h)
        f[i] /= N
    plt.plot(x,f)
    plt.title("h = %f" %h)
    plt.show()
    h/=10