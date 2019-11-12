import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
fig, ax=plt.subplots()
anim_object,=plt.plot([],[],marker='o')
def circle_m(R, t):
    x=R*(np.cos(t))**3
    y=R*(np.sin(t))**3
    return x, y
edge=5
ax.set_xlim(-edge,edge)
ax.set_ylim(-edge,edge)

def animat(i):
    anim_object.set_data(circle_m(R=3, t=i))
    
ani=animation.FuncAnimation(fig,
                            animat,
                            frames=np.arange(-4,4,0.1),
                            interval=100)

ani.save('animate.gif')
    