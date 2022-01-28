"""
   Explore exponential vs power-law scaling
   by looking at y(t)=exp(-t/t0)*(1+t/t1)**(-b).
"""

import sys
import numpy as np
from matplotlib import pyplot as plt


## parameters
t0 = 10.
t1 = 1.
b  = .5


#---- Script

if __name__ == '__main__':

    #---> Generate data

    xmax = 10*t0
    
    x0 = np.logspace(-3,0,100)
    x1 = np.linspace(1.1,xmax,100)

    t = np.concatenate((x0,x1))  # time

    y0 = np.exp(-t/t0)
    y1 = (1. + t/t1)**(-b)

    y = y0*y1  # signal
    
    #---> Create the figure
    
    fig, ax = plt.subplots(1, 1, sharey=True)
    fig.set_size_inches(6, 6)

    ax.plot(t,y, 'k')
    ax.plot(t,y0, ls='--', alpha=0.75)
    ax.plot(t,y1, ls=':',  alpha=0.75)
    
    ax.set_xlim(t[0], t[-1])
    ax.set_ylim(y[-1], 1)

    ax.set_xlabel(r'$t$')
    ax.set_ylabel(r'$y$')

    #ax.set_xscale('log')
    #ax.set_yscale('log')

    ax.get_xaxis().set_tick_params(which='both', direction='in')
    ax.get_yaxis().set_tick_params(which='both', direction='in')
    
    ax.legend([r'$y(t)=\exp(-t/t_0)(1+t/t_1)^{-b}$',
               r'$y(t)=\exp(-t/t_0)$',
               r'$y(t)=(1+t/t_1)^{-b}$'],
              frameon=False, numpoints=1, fontsize=12)

    ax.set_title('$t_0=%.3f$, $t_1=%.3f$, $b=%.3f$,'
                 %(t0,t1,b))
    
    #plt.savefig('../output/scaling.pdf', bbox_inches='tight', transparent=False)
    plt.show()
