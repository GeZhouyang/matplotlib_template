import numpy as np
from matplotlib import pyplot as plt

params = {'text.usetex' : True,
          'font.size' : 11,
          'font.family' : 'lmodern',
          'text.latex.unicode' : True}

plt.rcParams['text.latex.preamble']=[r'\usepackage{lmodern}']
plt.rcParams.update(params)

e  = np.exp(1)
pi = 3.1415926535897932



#---- Define a function to sample data

def sample_data(xOld, istart,istep):

    istop = len(xOld)
    xNew  = []  # assign an empty list (array)

    for i in range(istart,istop,istep):
        
        xNew.append(xOld[i])  # append it w/ sampled data        
    
    return xNew



#---- Define a function to plot data

def plot_data(ax, x0,y0, x1,y1):
    
    c0 = ax.plot(x0, y0, 'o', mec='r', mfc='none')
    c1 = ax.plot(x1, y1, '-k')

    ax.set_xlim(x1[0], x1[-1])
    ax.set_ylim(y1[0], y1[-1])

    ax.set_xlabel(r'$x$')
    ax.set_ylabel(r'$y$')

    ax.get_xaxis().set_tick_params(which='both', direction='in')
    ax.get_yaxis().set_tick_params(which='both', direction='in')

    ax.legend([r'Sampled data',r'Original data'],
              frameon=False, loc=2, numpoints=1, fontsize=9)
    
    return ax



#---- Script

if __name__ == '__main__':

    #---> Load original data

    x0 = np.loadtxt('../data/write.txt', usecols=(0,), skiprows=0)
    y0 = np.loadtxt('../data/write.txt', usecols=(1,), skiprows=0)

    #---> Write into a new file

    x0n = sample_data(x0, 0,10)
    y0n = sample_data(y0, 0,10)

    fname = '../output/write.txt'
    data_array = np.column_stack((x0n, y0n)) # convert multiple lists to one matrix
    
    np.savetxt(fname,data_array, fmt='%16.8e')

    #---> Create a figure (Optional)
    
    fig, ax = plt.subplots(1, 1, sharey=True)
    fig.set_size_inches(4.5, 4.5)
    
    ax = plot_data(ax, x0n,y0n, x0,y0)
        
    plt.savefig('../output/write.pdf', bbox_inches='tight', transparent=False)
    plt.show()
