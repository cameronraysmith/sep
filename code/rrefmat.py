# with open(fname) as f:
#     content = f.readlines()
import sys
import numpy as np
#import matplotlib.pyplot as plt
#import subprocess
import sympy as sp
#from matplotlib import rc


def main(argv):
    dfname = "C4.eq"
    ffname = "ncycvolrat.pdf"
    delimiter = ' '

    f = open ( dfname , 'r')
    l = [ map(float,line.split(delimiter)) for line in f ]
    l = np.array(l)
    f.close()

    l2 = np.zeros(shape=(8,17))
    l2[:,0:16] = l[:,1:17]
    l2[:,16] = l[:,0]
    #l2[7,16] = -l[7,0]
    print l2
    #print l

    ref = sp.Matrix(l[:,1:17]).rref(simplified=True)
    print ref

    ref = sp.Matrix(l2).rref(simplified=True)
    print ref

    # rc('text', usetex=True)
    # rc('font', family='serif')

    # fig1=plt.figure(num=1,figsize=(12,9),facecolor='w')
    # ax1f1 = fig1.add_subplot(111)
    # ax1f1.set_ylabel('volume ratio (non-modular : modular)',
    #                  fontsize=30,labelpad=20,fontweight='normal')
    # ax1f1.set_xlabel('n',fontsize=30,labelpad=10)
    # ax1f1.set_xlim((2, 7))
    # ax1f1.set_ylim((0.6, 1.1))
    # ax1f1.set_xticklabels(('','3','4','5','6',''))
    # ax1f1.set_yticklabels(('','','.7','','','1',''))
    # ax1f1.tick_params(axis='both', which='major', labelsize=30)
    # plt.grid(True)
    # f1p1 = plt.plot(l[:,1],l[:,0],
    #                 linestyle='-', linewidth=5, color='k',
    #                 marker='o',markersize=12,
    #                 mec='k',mfc='r')
    # plt.savefig(ffname,bbox_inches='tight',
    #     facecolor=fig1.get_facecolor(), edgecolor='none')
    # plt.close()

    # vnc = subprocess.check_output(["evince",ffname])

if __name__ == "__main__":
    #import doctest
    #doctest.testmod()
    main(sys.argv[1:])
