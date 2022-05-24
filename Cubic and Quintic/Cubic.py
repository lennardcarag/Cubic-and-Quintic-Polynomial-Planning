import numpy as np
import matplotlib.pyplot as plt

# degrees to radian convert
def deg_to_rad(T):
    return (T/180)*np.pi

qi = float(input('qi =  ')) #initial position
qi = deg_to_rad(qi)

vi = float(input('vi =  ')) #initial velocity
vi = deg_to_rad(vi)

qf = float(input('qf =  ')) #final position
qf = deg_to_rad(qf)

vf = float(input('vf =  ')) #final velocity
vf = deg_to_rad(vf)

ti = float(input('ti =  ')) #initial time
tf = float(input('tf =  ')) #final time

#cubi
#Solve the soln for q(t) = a + (3*(b-a)/c**2)*t**2 - (2*(b-a)/c**3)*t**3

x = np.arange(ti,tf,0.05)

def cubic(t,a,b,c): 
    return a + (3*(b-a)/c**2)*t**2 - (2*(b-a)/c**3)*t**3

y = cubic(x,qi,qf,tf)

plt.figure()
plt.plot(x,y,'r',linestyle='-')
plt.text(1,1.5,'q(t) = a + (3*(b-a)/c**2)*t**2 - (2*(b-a)/c**3)*t**3')
plt.grid(True)
plt.show()
