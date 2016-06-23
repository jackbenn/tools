import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def histpair(x, y, bins=None, xmin=None, xmax=None, normed=1, alpha=0.2, figsize=(12,8), title=None, binsize=None):
    '''
    INPUT:
    x: numpy array; point of a distribution
    y: numpy array of the same length; will plot histogram for each unique value of y
    bins: int; number of bins in histogram
    xmin: lower limit; other 
    '''
    plt.figure(figsize=figsize)
    plt.title(title)
    if xmin is None and xmax is None:
        xc = x
    else:
        xc = np.clip(x,a_min=xmin,a_max=xmax)
        
    if binsize == None:
        if bins == None:
            bins = 20.
        # maybe there should be logic around trying to make these integers
        # I might need a +1 here
        binarray = np.arange(xc.min(), xc.max(), (xc.max() - xc.min())/bins)
    else:
        binarray = np.arange(xc.min(), xc.max(), binsize)


    
    for yval in np.unique(y):
            plt.hist(list(xc[y==yval]), alpha=alpha, bins=binarray, normed=normed, label=str(yval))
    plt.xlim(xmin=xmin, xmax=xmax)
    plt.legend()
    #plt.show()
