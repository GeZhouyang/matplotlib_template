import sys
import numpy as np
from matplotlib import pyplot as plt

params = {'text.usetex' : True,
          'font.size' : 12.5,
          'font.family' : 'lmodern',
          'text.latex.unicode' : True}

plt.rcParams['text.latex.preamble']=[r'\usepackage{lmodern}']
plt.rcParams.update(params)
    

#---- define a function to plot data

def plot_data(ax, x0,y0, x1,y1):
    
    c0 = ax.plot(x0, y0, 'o', mec='r', mfc='none')
    c1 = ax.plot(x1, y1, '-k')

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    ax.set_xlabel(r'$x$')
    ax.set_ylabel(r'$y$')

    ax.get_xaxis().set_tick_params(which='both', direction='in')
    ax.get_yaxis().set_tick_params(which='both', direction='in')

    ax.legend([r'Data',r'Theory'],
              frameon=False, loc=2, numpoints=1, fontsize=10)
    ax.text(0.6, 0.3, r'A trivial plot.')
    
    return ax




#---- Script

if __name__ == '__main__':

    #---> Load data

    x0 = np.loadtxt('../data/basic.txt', usecols=(0,), skiprows=0)
    y0 = np.loadtxt('../data/basic.txt', usecols=(1,), skiprows=0)
    x1 = np.loadtxt('../data/basic.txt', usecols=(2,), skiprows=0)
    y1 = np.loadtxt('../data/basic.txt', usecols=(3,), skiprows=0)

    #---> Create the figure
    
    fig, ax = plt.subplots(1, 1, sharey=True)
    fig.set_size_inches(4.5, 4.5)
    
    ax = plot_data(ax, x0,y0, x1,y1)
        
    plt.savefig('../output/basic.pdf', bbox_inches='tight', transparent=False)
    plt.show()
