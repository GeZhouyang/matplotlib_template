'''
A simple script to calculate and plot the radial distribution function 
of a suspension of equal hard spheres. The raw data is stored in plain
vtk files with time indices. The output is the averaged distribution
over all pairs. The algorithm follows roughly the two links below:

http://www.physics.emory.edu/faculty/weeks//idl/gofr2.html
https://homepage.univie.ac.at/franz.vesely/simsp/dx/node22.html#EQPCF2

'''


import sys
import numpy as np
from matplotlib import pyplot as plt

params = {'text.usetex' : True,
          'font.size' : 12.5,
          'font.family' : 'lmodern',
          'text.latex.unicode' : True}

plt.rcParams['text.latex.preamble']=[r'\usepackage{lmodern}']
plt.rcParams.update(params)

# box size
lx = 9.4270
ly = 9.4270
lz = 9.4270

NP = 100 # num of particles
num_density = NP/(lx*ly*lz)

# bin setting
num_bins = 61
r_min = 1.95
r_max = 5.
dr = (r_max-r_min)/(num_bins+1)

ddir = '../data/' # data directory
    
dt = 2.089E-05
shear_rate = 0.01


#---- Use numpy's histogram function to do the counting

def counting(dist):
    
    n,bins = np.histogram(dist,bins=num_bins,range=(r_min,r_max))

    nl = list(n)
    bl = list(bins)
    count_bin = [nl,bl]

    return count_bin

#---- Compute the distance from the reference particle between all pairs
   
def comp_dist(istep):

    # Load data from file

    print 'istep = ',istep,' time = ', istep*1000*dt*shear_rate

    fname = ddir+'para'+str(istep).zfill(7)+'k.vtk'
    pos = []

    # read particle positions
    
    f = open(fname,'r')
    lines = f.readlines()[5:NP+5]  # skip headers
    for line in lines:
        buf = np.fromstring(line, dtype=float, sep='    ')
        buf1 = []
        for i in range(3):
            buf1.append(buf[i])
        pos.append(buf1)
    f.close()

    # generate periodic boxes
    
    pos_big = []
    y_shift = np.mod(shear_rate*lz*istep*1000*dt, ly)
    
    for jz in [-1.,0.,1.]:
        jz *= lz
        for jy in [-2.,-1.,0.,1.,2.]:
            jy = jy*ly + jz/lz*y_shift  # shift y depending on z (Lees-Edwards)
            for jx in [-1.,0.,1.]:
                jx *= lx                
        
                for i in range(NP):
                    buf = [ pos[i][0]+jx,pos[i][1]+jy,pos[i][2]+jz ]
                    pos_big.append(buf)
        
    # calculate distances
    
    dist = []
    for i in range(NP):
        xi = pos[i][0]
        yi = pos[i][1]
        zi = pos[i][2]
        buf = []
        for j in range(5*9*NP):
            xj = pos_big[j][0]
            yj = pos_big[j][1]
            zj = pos_big[j][2]
            
            d_ij = np.sqrt( (xi-xj)**2+(yi-yj)**2+(zi-zj)**2 )
            if d_ij < r_max and d_ij > 1e-7: # exclude self
                dist.append(d_ij)

    return dist

#---- Plot the radial distribution function

def plot_data(ax, count,bins):

    dist = np.zeros(num_bins)
    for i in range(num_bins):
        dist[i] = bins[i] + dr/2.
        
    c0 = ax.semilogy(dist, count, 'ok-', mfc='none')

    xx = [r_min,r_max]
    yy = [1.,1.]
    c1 = ax.semilogy(xx,yy,'--k')
    
    ax.set_xlim(xmin=r_min, xmax=r_max)
    ax.set_ylim(ymin=0.7, ymax=12.)
    
    ax.set_xlabel(r'$r$')
    ax.set_ylabel(r'$g(r)$')
    
    ax.get_xaxis().set_tick_params(which='both', direction='in')
    ax.get_yaxis().set_tick_params(which='both', direction='in')
    
    return ax
    

#---- Main script

if __name__ == '__main__':

    ibegin = 10000
    iend   = 200000
    ijump  = 10000
    
    Nstep = (iend-ibegin)/ijump
    dist = []
    
    for i in np.arange(ibegin,iend,ijump):
        dist.append(comp_dist(i))  # this will be a list of lists

    flat_list = [item for sublist in dist for item in sublist]

    # group into bins
    
    buf = counting(flat_list)
    count, bins = buf[0], buf[1]
    
    for i in range(num_bins):
        r = bins[i]
        count[i] *= 1./(Nstep*NP*4.*np.pi*r*r*dr*num_density) # normalization
    
    # plot the data
    
    fig, ax = plt.subplots(1, 1, sharey=True)
    fig.set_size_inches(6,6)
    
    ax = plot_data(ax, count,bins)
        
    plt.savefig('../output/radial_distr_func.png', bbox_inches='tight', transparent=False)
    plt.show()
