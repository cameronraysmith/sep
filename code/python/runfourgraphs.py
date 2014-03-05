"""
runfourgraphs.py
"""

import numpy as np
import pandas as pd
import subprocess
import sys
from minineqrep import minineqrep
from plotfourgraphs import plotvoldimdf


def definenames():
    graphlist = ["twok2",
                 "claw",
                 "P4",
                 "C4",
                 "paw",
                 "diamond",
                 "K4"]

    hgraphlist = ["flagpole",
                  "overtwo",
                  "basket",
                  "tripod",
                  "overtwoconnect",
                  "overthree"]#,
                  #"overfour"]

    ffnames = ["fourgraphsvol.pdf",
               "fourgraphsdim.pdf",
               "fourhgraphsvol.pdf",
               "fourhgraphsdim.pdf"]

    return graphlist, hgraphlist, ffnames


def rungraphlist(graphlist,graphtype):
    vrats=np.zeros(len(graphlist))
    dims=np.zeros(len(graphlist))
    dfrowlist=[]

    for i,g in enumerate(graphlist):
        print g
        vrats[i], dims[i]=minineqrep([g,"VERTICES"])
        dfdictrow={}
        dfdictrow.update({'volume ratio': vrats[i], 'dimension': dims[i],
                      'graph name':g, 'graph type':graphtype})
        dfrowlist.append(dfdictrow)

    return dfrowlist


def runvolcomp(args):
    graphlist, hgraphlist, ffnames = definenames()
    graphrowlist=rungraphlist(graphlist,'graph')
    hgraphrowlist=rungraphlist(hgraphlist,'hypergraph')

    #dfrowlist=itertools.chain(graphrowlist,hgraphrowlist)
    dfrowlist = graphrowlist + hgraphrowlist

    df=pd.DataFrame(dfrowlist)
    df.to_csv('graphdata.csv')
    plotvoldimdf('graphdata.csv')
    return df

if __name__ == "__main__":
    #import doctest
    #doctest.testmod()
    runvolcomp(sys.argv[1:])
