# with open(fname) as f:
#     content = f.readlines()
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import subprocess
import fileinput
from matplotlib import rc
import pandas as pd


def plotvoldimdf(dfname,ffnames=["fourgraphsvol.pdf",
                                 "fourgraphsdim.pdf",
                                 "fourhypergraphsvol.pdf",
                                 "fourhypergraphsdim.pdf"]):
    fhandle = open(dfname,'r')
    df = pd.read_csv(fhandle)

    rc('text', usetex=False)
    rc('font', family='sans-serif')

    dfgvr=df[df['graph type']=='graph']['volume ratio']
    dfgd=df[df['graph type']=='graph']['dimension']
    dfhvr=df[df['graph type']=='hypergraph']['volume ratio']
    dfhd=df[df['graph type']=='hypergraph']['dimension']

    dflist = [dfgvr,dfgd,dfhvr,dfhd]

    for i,l in enumerate(dflist):

        fig1=plt.figure(num=1,figsize=(12,9),facecolor='w')
        ax1f1 = fig1.add_subplot(111)

        if max(l)<=1:
            ax1f1.set_ylabel('volume ratio (non-modular : modular)',
                             fontsize=30,labelpad=20,fontweight='normal')
            ax1f1.set_xlabel('graph',fontsize=30,labelpad=10)
            ax1f1.set_xlim((0, len(l)+1))
            ax1f1.set_ylim((0.0, 1.1))
            #ax1f1.set_xticklabels(('','1','2','3','4','5',
            #                          '6','7','8','9','10',
            #                          '11',''))
            #ax1f1.set_xticklabels(('','','','','','','','',''))
            ax1f1.set_yticklabels(('','.2','','.6','','1'))
        else:
            ax1f1.set_ylabel('dimension',
                             fontsize=30,labelpad=20,fontweight='normal')
            ax1f1.set_xlabel('graph',fontsize=30,labelpad=10)
            ax1f1.set_xlim((0, len(l)+1))
            #ax1f1.set_ylim((0.0, max(l)+1))
            ax1f1.set_ylim((5.0, 15.0))

        ax1f1.tick_params(axis='both', which='major', labelsize=30)
        plt.grid(True)
        f1p1 = plt.plot(range(len(l)+1)[1:],l,
                        linestyle='-', linewidth=5, color='k',
                        marker='o',markersize=12,
                        mec='k',mfc='r')
        plt.savefig(ffnames[i],bbox_inches='tight',
            facecolor=fig1.get_facecolor(), edgecolor='none')
        plt.close()
        svgfile = os.path.splitext(ffnames[i])[0] + ".svg"
        subprocess.call("inkscape -l "+
                        svgfile +
                        " " + ffnames[i],shell=True)
        for line in fileinput.FileInput(svgfile,inplace=1):
            line = line.replace("Bitstream Vera Sans","HelveticaNeue")
            line = line.replace("BitstreamVeraSans-Roman","HelveticaNeue")
            print line,

   vnc = subprocess.call("evince " + " ".join(ffnames),shell=True)

def plotvoldim(l,ffname="fourgraphsvolrat.pdf"):
    #dfname = "fourgraphs.dat"
    #ffname = "fourgraphsvolrat.pdf"
    #delimiter = '  '

    #f = open ( dfname , 'r')
    #l = [ map(float,line.split(delimiter)) for line in f ]
    #l = np.array(l)
    #print l
    #f.close()

    rc('text', usetex=True)
    rc('font', family='serif')

    fig1=plt.figure(num=1,figsize=(12,9),facecolor='w')
    ax1f1 = fig1.add_subplot(111)

    if max(l)<=1:
        ax1f1.set_ylabel('volume ratio (non-modular : modular)',
                         fontsize=30,labelpad=20,fontweight='normal')
        ax1f1.set_xlabel('graph',fontsize=30,labelpad=10)
        ax1f1.set_xlim((0, len(l)+1))
        ax1f1.set_ylim((0.0, 1.1))
        #ax1f1.set_xticklabels(('','1','2','3','4','5',
        #                          '6','7','8','9','10',
        #                          '11',''))
        #ax1f1.set_xticklabels(('','','','','','','','',''))
        ax1f1.set_yticklabels(('','.2','','.6','','1'))
    else:
        ax1f1.set_ylabel('dimension',
                         fontsize=30,labelpad=20,fontweight='normal')
        ax1f1.set_xlabel('graph',fontsize=30,labelpad=10)
        ax1f1.set_xlim((0, len(l)+1))
        ax1f1.set_ylim((0.0, max(l)+1))

    ax1f1.tick_params(axis='both', which='major', labelsize=30)
    plt.grid(True)
    f1p1 = plt.plot(range(len(l)+1)[1:],l,
                    linestyle='-', linewidth=5, color='k',
                    marker='o',markersize=12,
                    mec='k',mfc='r')
    plt.savefig(ffname,bbox_inches='tight',
        facecolor=fig1.get_facecolor(), edgecolor='none')
    plt.close()

    #vnc = subprocess.check_output(["evince",ffname])

def plotfourgraphs(argv):
    dfname = "fourgraphs.dat"
    ffname = "fourgraphsvolrat.pdf"
    delimiter = '  '

    f = open ( dfname , 'r')
    l = [ map(float,line.split(delimiter)) for line in f ]
    l = np.array(l)
    #print l
    f.close()

    rc('text', usetex=True)
    rc('font', family='serif')

    fig1=plt.figure(num=1,figsize=(12,9),facecolor='w')
    ax1f1 = fig1.add_subplot(111)

    if max(l[:,0])<=1.:
        ax1f1.set_ylabel('volume ratio (non-modular : modular)',
                         fontsize=30,labelpad=20,fontweight='normal')
        ax1f1.set_xlabel('graph',fontsize=30,labelpad=10)
        ax1f1.set_xlim((0, len(l)+1))
        ax1f1.set_ylim((0.0, 1.1))
        #ax1f1.set_xticklabels(('','1','2','3','4','5',
        #                          '6','7','8','9','10',
        #                          '11',''))
        #ax1f1.set_xticklabels(('','','','','','','','',''))
        ax1f1.set_yticklabels(('','.2','','.6','','1'))
    else:
        ax1f1.set_ylabel('dimension',
                         fontsize=30,labelpad=20,fontweight='normal')
        ax1f1.set_xlabel('graph',fontsize=30,labelpad=10)
        ax1f1.set_xlim((0, len(l)+1))
        ax1f1.set_ylim((0.0, max(l[:,0])+1))
        #ax1f1.set_xticklabels(('','1','2','3','4','5',
        #                          '6','7','8','9','10',
        #                          '11',''))
        #ax1f1.set_xticklabels(('','','','','','','','',''))
        #ax1f1.set_yticklabels(('','.2','','.6','','1'))

    ax1f1.tick_params(axis='both', which='major', labelsize=30)
    plt.grid(True)
    f1p1 = plt.plot(l[:,1],l[:,0],
                    linestyle='-', linewidth=5, color='k',
                    marker='o',markersize=12,
                    mec='k',mfc='r')
    plt.savefig(ffname,bbox_inches='tight',
        facecolor=fig1.get_facecolor(), edgecolor='none')
    plt.close()

    vnc = subprocess.check_output(["evince",ffname])

if __name__ == "__main__":
    #import doctest
    #doctest.testmod()
    plotfourgraphs(sys.argv[1:])

