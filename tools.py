import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''
TODO
  xlim instead of xmin/xmax?
  kde
  set colors
'''


def histpair(x, y, bins=None, binsize=None, xmin=None, xmax=None, ymax=None,
             normed=1, alpha=0.2, figsize=(12, 8), title=None, ax=None):
    '''
    INPUT:
    x:      numpy array; point of a distribution
    y:      numpy array of the same length; will plot histogram
            for each unique value of y
    bins:   int; number of bins in histogram
    xmin:   lower limit; other
    normed: normalize number of elements in each class
    '''
    if ax is None:
        fig, ax = plt.subplots(figsize=figsize)
    if title is not None:
        ax.set_title(title)
    if xmin is None and xmax is None:
        xc = x
    else:
        xc = np.clip(x, a_min=xmin, a_max=xmax)

    if binsize is None:
        if bins is None:
            bins = 20.
        # maybe there should be logic around trying to make these integers
        binarray = np.arange(xc.min(),
                             xc.max(),
                             (xc.max() - xc.min())/(bins+1))
    else:
        binarray = np.arange(xc.min(),
                             xc.max(),
                             binsize)

    for yval in np.unique(y):
            ax.hist(list(xc[y == yval]),
                    alpha=alpha,
                    bins=binarray,
                    normed=normed,
                    label=str(yval))
    ax.set_xlim(xmin=xmin, xmax=xmax)
    if ymax is not None:
        ax.set_ylim(0, ymax)
    ax.legend()
