# with open(fname) as f:
#     content = f.readlines()
import sys
import numpy as np
import matplotlib.pyplot as plt
import subprocess
from matplotlib import rc

def main(argv):
    dfname = "ncyclevolume.dat"
    ffname = "ncycvolrat.pdf"
    delimiter = '  '

    f = open ( dfname , 'r')
    l = [ map(float,line.split(delimiter)) for line in f ]
    l = np.array(l)
    #print l
    f.close()

    rc('text', usetex=True)
    rc('font', family='serif')

    fig1=plt.figure(1)
    ax1f1 = fig1.add_subplot(111)
    ax1f1.set_ylabel('non-modular:modular volume ratio',
                     fontsize=16,labelpad=20,fontweight='normal')
    ax1f1.set_xlabel('n',fontsize=16,labelpad=10)
    ax1f1.set_xlim((2, 7))
    ax1f1.set_ylim((0.6, 1.1))
    ax1f1.set_xticklabels(('','3','4','5','6',''))
    ax1f1.set_yticklabels(('','','.7','','','1',''))
    ax1f1.tick_params(axis='both', which='major', labelsize=16)
    plt.grid(True)
    f1p1 = plt.plot(l[:,1],l[:,0],
                    linestyle='-', linewidth=5, color='k',
                    marker='o',markersize=12,
                    mec='k',mfc='r')
    plt.savefig(ffname)
    plt.close()

    vnc = subprocess.check_output(["evince",ffname])

if __name__ == "__main__":
    #import doctest
    #doctest.testmod()
    main(sys.argv[1:])
