import numpy as np
import matplotlib.pyplot as plt

def cikl(R=1,title="cikloida"):
    t=np.arange(-2*np.pi,2*np.pi, 0.1)
    x=R*(t-np.sin(t))
    y=R*(1-np.cos(t))
    plt.plot(x,y)
    plt.xlim(-10,10)
    plt.ylim(-10,10)
    plt.title()
    plt.legend()
    plt.show()

cikl()