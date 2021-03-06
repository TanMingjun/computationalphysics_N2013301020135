import matplotlib.pyplot as plt
from math import *


Constant_g=9.8
Constant_l=9.8
Constant_q=0.5
Constant_Omegad=2.0/3.0

dt = pi/300

c_t = []
c_theta = []
c_omega = []

def Calculate(Initial_theta,Initial_omega,c_t,c_theta,c_omega):
    c_theta.append(Initial_theta)
    c_omega.append(Initial_omega)
    c_t.append(0.0)
    print 'Initial_theta =',c_theta[0],'rad    ',
    print 'Initial_omega =',c_omega[0],'rad/s    ',
    print 'F_d =',F_d,'N    ',
    for i in range(3000000):
        c_omega.append(c_omega[i]-(sin(c_theta[i])+Constant_q*c_omega[i]-F_d*sin(Constant_Omegad*c_t[i]))*dt)
        c_theta.append(c_theta[i] + c_omega[i+1]*dt)
        c_t.append(c_t[i]+dt)
        if c_theta[-1]>pi:
            c_theta[-1]=c_theta[-1]-2*pi
        if c_theta[-1]<-pi:
            c_theta[-1]=c_theta[-1]+2*pi
    print 'Total steps =',i,'    ',
    print 'dt =',dt

    return 0

Initial_theta=0.2
Initial_omega=0.0
F_dlist=[0,0.5,1.2]

for m in range(2,3):
    c_t = None
    c_theta = None
    c_omega = None
    c_t = []
    c_theta = []
    c_omega = []
    F_d=F_dlist[m]
    F_dstr=str(F_d)
    c_theta1=[]
    c_omega1=[]
    c_t1=[]
    Calculate(Initial_theta,Initial_omega,c_t,c_theta,c_omega) 
    i=225
    n=0
    while i<3000000:
            c_theta1.append(c_theta[i])
            c_omega1.append(c_omega[i])
            c_t1.append(c_t[i])
            i=i+450
            n=n+1
    print 'Total',len(c_theta1)
    plt.scatter(c_theta1,c_omega1,label='theta corresponding to maximum drive force F_D = 1.2(N)')


plt.xlabel('theta (rad)')
plt.ylabel('omega (rad/s)')
plt.legend()
plt.savefig('Ex9-L1.png',dpi = 144)
plt.show()
