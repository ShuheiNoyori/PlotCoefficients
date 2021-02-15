#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import pandas as pd
from matplotlib import pyplot as plt
plt.rcParams['font.family'] = 'Times New Roman' # 'Hiragino Sans'
plt.rcParams['axes.axisbelow'] = True

##############################################
# Functions
##############################################
def barplot(x0, x1, y, height):
    if x0 > x1:
        raise Exception('X1 must be equal to or more than X0')
    if x0*x1 > 0:
        if x0 > 0:
            plt.barh(y, x1-x0, left=x0, height=height, color = 'tab:orange')
        elif x0 < 0:
            plt.barh(y, x0-x1, left=x1, height=height, color = 'tab:blue')
    else:
        plt.barh(y, x1-x0, left=x0, height=height, color = 'tab:gray')

def coefbarplot(df):
    plt.figure(figsize = (6, 4))
    
    for i, cil, ciu in zip(range(len(df.index)), df['CIlower'], df['CIUpper']):
        barplot(cil, ciu, i, 0.4)
    
    plt.vlines(0, -1, len(df.index), color='black', linestyles='dotted', linewidth=1)
    plt.ylim(len(df.index), -1)
    plt.grid()
    plt.yticks(range(len(df.index)), df.index)
    plt.xlabel('Coefficient (95% confidence interval)')
    plt.ylabel('Parameter')
    
##############################################
# Main
##############################################
# Read data
path_to_file = 'path_to_file'
filename = 'filename.csv'

df = pd.read_csv(os.path.join(path_to_file, filename),
                 index_col = 0,
                 encoding = 'SHIFT-JIS')

# 95% confidence interval (Estimate: Estimated coefficient, Std. Error: Standard error)
df['CIlower'] = df['Estimate'] - 1.96*df['Std. Error']
df['CIUpper'] = df['Estimate'] + 1.96*df['Std. Error']

coefbarplot(df)
plt.savefig(os.path.join(path_to_file, 'plot_{}.png'.format(filename[:-4])),
            dpi=600,
            bbox_inches='tight')
