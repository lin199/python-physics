import numpy as np
import matplotlib.pyplot as plt

from pylab import *
mpl.rcParams['font.sans-serif'] = ['Microsoft Yahei']

x=np.linspace(-np.pi,np.pi,256,endpoint=True)
fig,ax=plt.subplots()
fig.suptitle("李萨如图形")
plt.subplot(2,3,1)
c,s=np.cos(1*x),np.cos(2*x)
plt.plot(s,c,'k-',linewidth=1.0)
plt.subplot(2,3,2)
m,n=np.cos(1*x),np.cos(2*x+np.pi/4)
plt.plot(m,n,'k-',linewidth=1.0)
plt.subplot(2,3,3)
m1,n1=np.cos(1*x),np.cos(2*x+np.pi/2)
plt.plot(m1,n1,'k-',linewidth=1.0)
plt.subplot(2,3,4)
m2,n2=np.cos(1*x),np.cos(2*x+3*np.pi/4)
plt.plot(m2,n2,'k-',linewidth=1.0)
plt.subplot(2,3,5)
m3,n3=np.cos(1*x),np.cos(2*x+np.pi)
plt.plot(m3,n3,'k-',linewidth=1.0)
plt.show()
