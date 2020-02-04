import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation


t = np.arange(10**(-7), 1.1*10**(-7),1.5*10**(-11))

def func(s, t):
    (x1, vx1, y1, vy1,
     x2, vx2, y2, vy2,
     x3, vx3, y3, vy3,
     x4, vx4, y4, vy4) = s
    dxdt1 = vx1
    dvxdt1 = (k * q1 * q2 / m1 * (x1 - x2) / ((x1 - x2)**2 + (y1 - y2)**2)**1.5
    + k *q1 * q3 / m1 * (x1 - x3) / ((x1 - x3)**2 + (y1 - y3)**2)**1.5+
    k *q1 * q4 / m1 * (x1 - x4) / ((x1 - x4)**2 + (y1 - y4)**2)**1.5)
   
    dydt1 = vy1
    dvydt1 = (k * q1 * q2 / m1 * (y1 - y2) / ((x1 - x2)**2 + (y1 - y2)**2)**1.5
    + k *q1 * q3 / m1 * (y1 - y3) / ((x1 - x3)**2 + (y1 - y3)**2)**1.5+
     k *q1 * q4 / m1 * (y1 - y4) / ((x1 - x4)**2 + (y1 - y4)**2)**1.5)
   
    
    dxdt2 = vx2
    dvxdt2 = (k * q2 * q1 / m2 * (x2 - x1) / ((x2 - x1)**2 + (y2 - y1)**2)**1.5
    + k *q2 * q3 / m2 * (x2 - x3) / ((x2 - x3)**2 + (y2 - y3)**2)**1.5+
    k *q2 * q4 / m2 * (x2 - x4) / ((x2 - x4)**2 + (y2 - y4)**2)**1.5)
   
    
    dydt2 = vy2
    dvydt2 = (k * q2 * q1 / m2 * (y2 - y1) / ((x2 - x1)**2 + (y2 - y1)**2)**1.5
    + k *q2 * q3 / m2 * (y2 - y3) / ((x2 - x3)**2 + (y2 - y3)**2)**1.5+
    k *q2 * q4 / m2 * (y2 - y4) / ((x2 - x4)**2 + (y2 - y4)**2)**1.5)
   
    
    dxdt3 = vx3
    dvxdt3 = (k * q3 * q1 / m3 * (x3 - x1) / ((x3 - x1)**2 + (y3 - y1)**2)**1.5
    + k *q3 * q2 / m3 * (x3 - x2) / ((x3 - x2)**2 + (y3 - y2)**2)**1.5+
    k *q3 * q4 / m3 * (x3 - x4) / ((x3 - x4)**2 + (y3 - y4)**2)**1.5)
   
    
    dydt3 = vy3
    dvydt3 = (k * q3 * q1 / m3 * (y3 - y1) / ((x3 - x1)**2 + (y3 - y1)**2)**1.5
    + k *q3 * q2 / m3 * (y3 - y2) / ((x3 - x2)**2 + (y3 - y2)**2)**1.5+
    k *q3 * q4 / m3 * (y3 - y4) / ((x3 - x4)**2 + (y3 - y4)**2)**1.5)
    
    dxdt4 = vx4
    dvxdt4 = (k * q4 * q1 / m4 * (x4 - x1) / ((x4 - x1)**2 + (y4 - y1)**2)**1.5
    + k *q4 * q2 / m4 * (x4 - x2) / ((x4 - x2)**2 + (y4 - y2)**2)**1.5+
    k *q4 * q3 / m4 * (x4 - x3) / ((x4 - x3)**2 + (y4 - y3)**2)**1.5)
    
    dydt4 = vy4
    dvydt4 = (k * q4 * q1 / m3 * (y4 - y1) / ((x4 - x1)**2 + (y4 - y1)**2)**1.5
    + k *q4 * q2 / m4 * (y4 - y2) / ((x4 - x2)**2 + (y4 - y2)**2)**1.5+
    k *q4 * q3 / m4 * (y4 - y3) / ((x4 - x3)**2 + (y4 - y3)**2)**1.5)    
   
    
    return (dxdt1, dvxdt1, dydt1, dvydt1,
            dxdt2, dvxdt2, dydt2, dvydt2,
            dxdt3, dvxdt3, dydt3, dvydt3,
            dxdt4, dvxdt4, dydt4, dvydt4)
    
    



k = 8.98755 * 10**9

x10 = -0.008
vx10 = -2*10**6*np.sin(np.pi/4)
y10 = 0.008   
vy10 = -2*10**6*np.sin(np.pi/4)
    
x20 = 0.008
vx20 = -2*10**6*np.sin(np.pi/4)
y20 = 0.008  
vy20 = 2*10**6*np.sin(np.pi/4)
    
x30 = 0.008
vx30 = 2*10**6*np.sin(np.pi/4)
y30 = -0.008
vy30 = 2*10**6*np.sin(np.pi/4)

x40 = -0.008
vx40 = 2*10**6*np.sin(np.pi/4)
y40 = -0.008
vy40 = -1*10**6*np.sin(np.pi/4)
    
s0 = (x10, vx10, y10, vy10,
      x20, vx20, y20, vy20,
      x30, vx30, y30, vy30,
      x40, vx40, y40, vy40)


m1 = 1.1 * 10**(-27)
q1 = 1.1 * 10**(-13)

m2 = 1.1 * 10**(-27)
q2 = 1.2 * 10**(-13)

m3 = 1.1 * 10**(-27)
q3 = -1.1 * 10**(-13)

m4 = 1.1 * 10**(-27)
q4 = -1.1 * 10**(-13)

sol = odeint(func, s0, t)


fig = plt.figure()
bodys = []

for i in range (0, len(t), 1):
    body1, = plt.plot(sol[:i, 0], sol[:i, 2], '-', color ='r')
    body1_line, = plt.plot(sol[i, 0], sol[i, 2], 'o', color = 'r')
    
    body2, = plt.plot(sol[:i,4], sol[:i,6], '-', color ='g')
    body2_line, = plt.plot(sol[i,4], sol[i, 6], 'o', color = 'g')
     
    body3, = plt.plot(sol[:i,8], sol[:i,10], '-', color ='b') 
    body3_line, = plt.plot(sol[i,8], sol[i,10], 'o', color = 'b')
    
    body4, = plt.plot(sol[:i,12], sol[:i,14], '-', color ='y') 
    body4_line, = plt.plot(sol[i,12], sol[i,14], 'o', color = 'y')
    
    bodys.append([body1, body1_line, body2, body2_line, body3, body3_line, body4, body4_line])
    
ani = ArtistAnimation(fig, bodys, interval=50)
plt.axis('equal')
ani.save('ChastichkiFinal.gif')