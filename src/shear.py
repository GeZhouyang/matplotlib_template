import numpy as np
from matplotlib import pyplot as plt

params = {'text.usetex' : True,
          'font.size' : 20,
          'font.family' : 'sans-serif',
          'text.latex.unicode' : True}

plt.rcParams['text.latex.preamble']=[r'\usepackage{lmodern}']
plt.rcParams.update(params)

    

#---- define a function to plot data

def plot_data(ax, x0,y0,u0,v0, tname):#, x1,y1):
    
    c0 = ax.quiver(x0,y0,u0,v0, alpha=0.6)

    ax.set_xlim(-1.4, 1.4)
    ax.set_ylim(-1.4, 1.4)

    plt.axis('off')
    plt.title(tname)

    #-- draw coords arrows

    xpc,ypc,lpc = 0,0,0.15
    ax.arrow(xpc,ypc,lpc,0,head_width=0.05, fc='k',ec='k')
    ax.arrow(xpc,ypc,0,lpc,head_width=0.05, fc='k',ec='k')

    #-- Add texts with white background

    #props = dict(boxstyle="square",fc='w',ec='w')

    ax.text(xpc+lpc*1.8,ypc, r'$y$', fontsize=14)#, bbox=props)
    ax.text(xpc,ypc+lpc*1.8, r'$z$', fontsize=14)#, bbox=props)
    
    
    return ax




#---- Script

if __name__ == '__main__':

    #---> Coordinates

    x = np.linspace(-1,1,8)
    y = x
    x0,y0 = np.meshgrid(x,y)

    #---> Strain

    lam = 1./2. # strain rate
    theta = np.pi/2. # rotation matrix
    cos,sin = np.cos(theta), np.sin(theta)

    u0 = lam*(x0*cos + y0*sin)
    v0 = lam*(x0*sin - y0*cos)
    
    fig, ax0 = plt.subplots(1, 1, sharey=True)
    fig.set_size_inches(6, 6)
    
    ax0 = plot_data(ax0, x0,y0,u0,v0, 'Strain')
    plt.savefig('../output/strain.png', bbox_inches='tight', transparent=True)


    #---> Rotation

    omg = 1. # vorticity
    theta = 0. # rotation matrix
    cos,sin = np.cos(theta), np.sin(theta)

    u1 = lam*(y0*cos + x0*sin)
    v1 = lam*(y0*sin - x0*cos)
    
    fig, ax1 = plt.subplots(1, 1, sharey=True)
    fig.set_size_inches(6, 6)
    
    ax1 = plot_data(ax1, x0,y0,u1,v1, 'Rotation')
    plt.savefig('../output/rotation.png', bbox_inches='tight', transparent=True)

    #---> Shear

    u2,v2 = u0+u1,v0+v1
    
    fig, ax2 = plt.subplots(1, 1, sharey=True)
    fig.set_size_inches(6, 6)
    
    ax2 = plot_data(ax2, x0,y0,u2,v2, 'Shear')
    plt.savefig('../output/shear.png', bbox_inches='tight', transparent=True)

    
    plt.show()
