""" Plot the flow field due to a source dipole
"""
import sys
import numpy as np
import matplotlib.patches as patches
from matplotlib import pyplot as plt
from matplotlib import rc
rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
rc('text', usetex=True)


#---- Generate the flow field

def flow_field(xmin,xmax,itot):
    
    x = np.linspace(xmin,xmax,itot)
    y = np.linspace(xmin,xmax,itot)

    x1d, y1d, u1d, v1d = [],[],[],[] 
    
    for i,xx in enumerate(x):
        for j,yy in enumerate(x):

            x1d.append(xx)
            y1d.append(yy)

            r  = max(.5, np.sqrt(xx**2 + yy**2)) # saturate small r
            r3 = r**3
            r5 = r**5
            buf= xx**2 - yy**2

            # source dipole flow
            u1d.append(3.*xx**2/r5 - 1./r3)
            v1d.append(3.*xx*yy/r5)
            
    # generate the grid ...
    x2d = np.reshape(x1d,(itot,itot))
    y2d = np.reshape(y1d,(itot,itot))
    
    # ... and the velocity fields
    u2d = np.reshape(u1d,(itot,itot))
    v2d = np.reshape(v1d,(itot,itot))
    
    return x2d,y2d,u2d,v2d


#---- Script

if __name__ == '__main__':

    ## create a figure
    fig, ax = plt.subplots(1, 1)
    fig.set_size_inches(6,4)
    
    ax.set_aspect(1)
    ax.set_title(r'Source dipole ($-\to+$)')

    
    ## velocity contours
    xmin,xmax = -5.0,5.0
    itot = 101

    x2d,y2d,u2d,v2d = flow_field(xmin,xmax,itot)

    vel = np.sqrt(np.add(np.square(u2d),np.square(v2d)))  # velocity magnitude

    lvl = np.arange(-6,4,1) # contour levels
    for i in range(3): # plot repeatedly to remove edges (workaround)
        ctf = ax.contourf(x2d,y2d,np.log(vel), levels=lvl, cmap='gray')

    cbar = fig.colorbar(ctf)
    cbar.ax.set_ylabel(r'$\log(v/v_0)$')

    ax.set_xlim(xmin, xmax)
    ax.set_ylim(xmin, xmax)

    
    ## velocity quivers (on a sparse mesh)
    xmin,xmax = -4.5,4.5
    itot = 11

    x2d,y2d,u2d,v2d = flow_field(xmin,xmax,itot)

    vel = np.sqrt(np.add(np.square(u2d),np.square(v2d)))  # velocity magnitude
    # direction
    u0 = np.divide(u2d,vel, out=np.zeros_like(u2d), where=abs(vel)>1e-9)
    v0 = np.divide(v2d,vel, out=np.zeros_like(v2d), where=abs(vel)>1e-9)

    q0 = ax.quiver(x2d,y2d, u0,v0,
                   scale=15., width=0.0075, pivot='mid',
                   color=['#A9A9A9'], edgecolors=['#A9A9A9'])  # darkgray

    
    ## save the figure
    plt.savefig('../output/source_dipole.pdf', bbox_inches='tight')
