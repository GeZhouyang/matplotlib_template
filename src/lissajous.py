import sys
import numpy as np
from matplotlib import pyplot as plt

params = {'text.usetex' : True,
          'font.size' : 12.5,
          'font.family' : 'lmodern',
          'text.latex.unicode' : True}

plt.rcParams['text.latex.preamble']=[r'\usepackage{lmodern}']
plt.rcParams.update(params)

pi = np.pi
cos = np.cos
sin = np.sin

#---- define a function to plot data

def plot_data(ax, x,y):
    
    ax.plot(x,y)

    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)

    ax.set_aspect('equal')
    ax.grid(True)
    
    ax.set_xlabel(r'$x=$ cos($t$)')
    ax.set_ylabel(r'$y=A$cos($\omega t+\delta \pi$)')
    ax.set_title(r'$A=$ '+('%.1f'%A)+
                 r', $\omega=$ '+('%.1f'%omega)+
                 r', $\delta=$ '+('%.1f'%delta))
    
    return ax


#---- Script

if __name__ == '__main__':

    #---> Create the figure
    
    fig, ax = plt.subplots(1, 1, sharey=True)
    fig.set_size_inches(5,5)

    #---> Plot

    t = np.linspace(0.,4.*pi,500)

    X = cos(t)

    A = 1.
    
    cnt = 0
    for omega in np.linspace(2.,2.,1):
        for delta in np.linspace(0.,2.,21):
            Y = A*cos(omega*t + delta*pi)
    
            ax = plot_data(ax, X,Y)
            cnt += 1
            print 'number ',cnt
            
            plt.savefig('../output/Lissajous/curve'+('%03d'%cnt)+'.png',
                        bbox_inches='tight', transparent=False)
            
            plt.cla()  # clear axis
            
    #plt.show()
