import math as ms
import shutil
import datetime
import os
import csv
import numpy as np
import random
import subprocess
#import pandas
import math
import sys

import glob
import os, errno
import matplotlib.pyplot as plt
import matplotlib.pylab as py
import matplotlib as mpl
from matplotlib import colors
# from matplotlib import colors
import matplotlib as mpl
from matplotlib.colors import LinearSegmentedColormap
from scipy.optimize import curve_fit
import sympy as sym
from decimal import Decimal
from matplotlib.ticker import FormatStrFormatter
import scipy.stats

path_out = r'D:/myfolder'
repitations=50

std_data_x = np.random.random(1)
mean_data_x = np.arange(5, 6,1)
# print(std_data_x)

std_data_y = np.random.random(1)
mean_data_y = np.arange(10, 11, 1)

# 95% confidence interval

CIx = (1.960 * std_data_x) / math.sqrt((repitations - 1))
CIy = (1.960 * std_data_y) / math.sqrt((repitations - 1))

fig = plt.figure(figsize=(6, 6))
ax1 = fig.add_subplot(111)

ind = (0.5, 1)
ax1.bar(ind[0], mean_data_x, yerr=CIx, align='center', width=0.2, color='r', label="data x")
ax1.bar(ind[1], mean_data_y, yerr=CIy, align='center', width=0.2, color='blue', label="data y")

ax1.legend(loc='upper right', fontsize=12)
ax1.set_ylim([0, 15])
ax1.set_xlim([0, 1.5])

ax1.set_ylabel("values", fontsize=12)
ax1.set_title("Barplot", size=15, y=1.01, x=0.50)

plt.tick_params(
    axis='x',  # changes apply to the x-axis
    which='both',  # both major and minor ticks are affected
    bottom='off',  # ticks along the bottom edge are off
    top='off',  # ticks along the top edge are off
    labelbottom='off')

plt.tight_layout(rect=[0, 0, 1, 0.95])
# plt.tight_layout()
plt.savefig(os.path.join(path_out, "mybarplot.png"))
plt.show()

