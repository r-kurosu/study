# #中心差分
# import numpy 
# import matplotlib.pyplot as plt



# nx = 501
# dx = 2 / (nx - 1)
# nt = 1000 
# dt = .0002  #変更
# c = 1

# u = numpy.zeros(nx) 
# u[int(0.2 / dx) : int(0.5 / dx + 1)] = 1  

# for n in range(nt):  
    
#     u_old = u.copy() 
#     u[1:-1] = u_old[1:-1] - c * dt / (2 * dx) * (u_old[2:] - u_old[:-2]) 

#     #for i in range(1, nx-1):
#     #    u[i] = u_old[i] - c * dt / (2 * dx) * (u_old[i+1] - u_old[i-1]
    
#     if n % 200 == 0:
#         plt.plot(numpy.linspace(0, 2, nx), u)

# plt.show()


# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation
# from matplotlib.animation import PillowWriter
# from matplotlib._version import get_versions as mplv
# import copy
# #from scipy.stats import gaussian_kde

# fig=plt.figure()

# xl=100; nx=201; c=-0.5
# xb=10;xp=xl-xb;fp=0.5
# etime=120;dt=0.1

# x=np.linspace(0,xl,nx)
# dx=x[ 2]-x[ 1]
# f=[0]*nx; fn=[0]*nx
# ims=[]

# for i in range(0,nx):
#     if(x[i]>=(xp-xb) and x[i]<=xp): 
#         f[i]=fp/xb*(x[i]-xp+xb) 
#     elif(x[i]>xp and x[i]<(xp+xb)):
#         f[i]=fp/xb*(xp+xb-x[i])
#     else:
#         f[i]=0

# im=plt.title("Forward (c<0)",size='25')
# im=plt.xlabel("x")
# im=plt.ylabel("f")
# im=plt.ylim(0,1.0)


# time=0
# icount=0; fskip=10
# while(time<=etime):
#     for i in range(1,nx-1):
#         fn[i]=f[i]-c*(f[i+1]-f[i])*dt/dx

#     f=copy.copy(fn)
#     icount=icount+1
#     if (icount % fskip) == 0:
#         text1=plt.text(0.,0.9,"Time="+str(np.round(time,3))+"sec",size='20')
#         im=plt.plot(x,f,'r')
#         ims.append(im+[text1])
        
#     time=time+dt

# ani = animation.ArtistAnimation(fig, ims, interval=10)
# #plt.show(); #PC画面アニメ出力
# ani.save('forward-.gif',writer='imagemagick'); #gifファイル出力
# #ani.save('backward.mp4',writer='ffmpeg'); #mp4ファイル出力

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation, rc
from IPython.display import HTML

v = 2
dt = 0.01
dx = 0.01
N = 101
Nt = 100

CFL = v*dt/dx
if CFL > 1:
    print('CFL ERROR')
    print("CFL =", CFL)
else:
    print("CFL =", CFL)
x = np.arange(0, N*dx, dx)
y = np.zeros(len(x))

#矩形波を初期値にする
for i in range(10, 30):
    y[i] = 1


for n in range(1,Nt):
    for i in range(len(x)-1):
        y[i] = y[i] - CFL*(y[i]-y[i-1])
    y[-1] = y[-2] #iの最後はfor文で計算しないため、一つ前の値と等しくさせる