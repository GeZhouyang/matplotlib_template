import numpy as np
from matplotlib import pyplot as plt

params = {'text.usetex' : True,
          'font.size' : 11,
          'font.family' : 'lmodern',
          'text.latex.unicode' : True}

plt.rcParams['text.latex.preamble']=[r'\usepackage{lmodern}']
plt.rcParams.update(params)


#---- Define a function to plot data

def plot_data(ax, x0,y0):
    
    c0 = ax.plot(x0, y0)
    
    ax.get_xaxis().set_tick_params(which='both', direction='in')
    ax.get_yaxis().set_tick_params(which='both', direction='in')
    
    return ax



#---- Script

if __name__ == '__main__':

    #---> Initialize data

    t = np.linspace(0,10,200)
    x = np.sin(pi*t) + np.abs(t-2)

    #---> Write into a new file
    
    fname = '../data/fourier3.txt'
    data_array = np.column_stack((t, x)) # convert multiple lists to one matrix
    
    np.savetxt(fname,data_array, fmt='%16.8e')
    
    #---> Create a figure (Optional)
    
    fig, ax = plt.subplots(1, 1, sharey=True)
    fig.set_size_inches(4.5, 4.5)
    
    ax = plot_data(ax, t,x)
        
    plt.show()
