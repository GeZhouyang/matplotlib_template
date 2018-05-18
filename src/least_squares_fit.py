import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import leastsq

params = {'text.usetex' : True,
          'font.size' : 11,
          'font.family' : 'lmodern',
          'text.latex.unicode' : True}

plt.rcParams['text.latex.preamble']=[r'\usepackage{lmodern}']
plt.rcParams.update(params)


#---- least squares fit

def fitting(x,y,degree):

    # create lambda fitting functions
    if degree == 1:
        func = lambda tpl,x : tpl[0]*x+tpl[1] # tpl contains the parameters of the fit
        tpl_init = (1.0,2.0) # initial guess of the tuple
    elif degree == 2:
        func = lambda tpl,x : tpl[0]*x**2+tpl[1]*x+tpl[2]
        tpl_init=(1.0,2.0,3.0)

    # define the error function (to minimize)
    error_func = lambda tpl,x,y: (func(tpl,x)-y)**2

    # minimize
    tpl_final, success = leastsq(error_func, tpl_init[:], args=(x,y))

    # fitted data
    x_f = np.linspace(x.min(),x.max(),50)
    y_f = func(tpl_final, x_f)

    # gather outputs
    fitted = []
    fitted.append(tpl_final)
    fitted.append(x_f)
    fitted.append(y_f)
    
    return fitted

#---- define a function to plot data

def plot_data(ax, t,z):
    
    c0 = ax.plot(t, z)

    # least squares fit

    degree = 2
    fitted = fitting(t,z, degree)
    
    coef = fitted[0]
    t_f = fitted[1]
    z_f = fitted[2]

    print "Fitting coefficients ", coef
    c0_f = ax.plot(t_f, z_f, '--')

    plt.xlim(xmin=0)
    plt.ylim(ymin=0)
    
    ax.set_xlabel(r'$t/T$')
    ax.set_ylabel(r'$\Delta/D$')
    
    ax.get_xaxis().set_tick_params(which='both', direction='in')
    ax.get_yaxis().set_tick_params(which='both', direction='in')
    
    ax.legend([r'Original',r'Fitted'],
              frameon=False, loc=2, numpoints=1, fontsize=9)
    
    return ax




#---- Script

if __name__ == '__main__':

    #---> Load data

    filename = '../data/least_squares_data.txt'

    t = np.loadtxt(filename, usecols=(0,), skiprows=0)
    z = np.loadtxt(filename, usecols=(1,), skiprows=0)

    z = z - z[0]

    #---> Create the figure
    
    fig, ax = plt.subplots(1, 1, sharey=True)
    fig.set_size_inches(4.5, 4.5)
    
    ax = plot_data(ax, t,z)
        
    plt.savefig('../output/least_squares.png', bbox_inches='tight', transparent=False)
    plt.show()
