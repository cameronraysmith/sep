"""
hypergraphlattice.py

1. given a number of vertices generate a Hasse diagram
of the lattice of hypergraphs over the given number of vertices
2. use [Graham reduction](https://en.wikipedia.org/wiki/Hypergraph#Acyclicity)
to detect cycles in each hypergraph and generate a Hasse diagram of all
hypergraphs on a given number of vertices in which each hypergraph
contains at least one cycle

uses the python-lattice 0.0.2 package
https://pypi.python.org/pypi/python-lattice

uses the python dot2tex 2.8.7 package
https://pypi.python.org/pypi/dot2tex
"""

from lattice import Lattice
import itrecipes
import subprocess
import re
import dot2tex

from hypergraphcycle import testcycle

def subsetsize(ss):
    if not map(len,ss):
        return 0
    else:
        return max(map(len,ss))

def removesubsets(ss):
    fs = frozenset([m for i,m in enumerate(ss)
                    if not any(m < n for n in ss)])
    return fs

def Hasse2(L):
        graph=dict()
        for indexS,elementS in enumerate(L.Uelements):
            graph[indexS]=[]
            supersets = [(indexD,elementD)
                           for indexD,elementD in enumerate(L.Uelements)
                           if L.wrap(elementS) <= L.wrap(elementD)]
            supersets.remove((indexS,elementS))
            coverindexlist = [ind for ind,cover in supersets
                            if not any(L.wrap(cover) >= L.wrap(ostcover)
                      for i,ostcover in supersets if ostcover != cover)]
            graph[indexS]=coverindexlist
        dotcode='digraph G {\nsplines="line"\nrankdir=BT\n'
        dotcode+='\"'+str(L.TopElement.unwrap)+'\" [shape=box];\n'
        dotcode+='\"'+str(L.BottonElement.unwrap)+'\" [shape=box];\n'
        for s, ds in graph.iteritems():
            for d in ds:
                dotcode += "\""+str(L.WElementByIndex(s))+"\""
                dotcode += " -> "
                dotcode += "\""+str(L.WElementByIndex(d))+"\""
                dotcode += ";\n"
        dotcode += "}"
        try:
            from scapy.all import do_graph
            do_graph(dotcode)
        except:
            pass
        return dotcode

def Hasse3(L):
        graph=dict()
        for indexS,elementS in enumerate(L):
            graph[indexS]=[]
            supersets = [(indexD,elementD)
                           for indexD,elementD in enumerate(L)
                           if elementS <= elementD]
            supersets.remove((indexS,elementS))
            coverindexlist = [ind for ind,cover in supersets
                            if not any(cover >= ostcover
                      for i,ostcover in supersets if ostcover != cover)]
            graph[indexS]=coverindexlist

        vals = [val for k,v in graph.iteritems() for val in v]
        nakedkeys = [k for k,v in graph.iteritems() if not v]
        noionodes = [nk for nk in nakedkeys if nk not in vals]

        dotcode='digraph G {\nsplines="line"\nrankdir=BT\n'
        for g in noionodes:
            dotcode+='\"'+str(L[g])+'\" [shape=box];\n'
        #dotcode+='\"'+str(L.TopElement.unwrap)+'\" [shape=box];\n'
        #dotcode+='\"'+str(L.BottonElement.unwrap)+'\" [shape=box];\n'
        for s, ds in graph.iteritems():
            for d in ds:
                dotcode += "\""+str(L[s])+"\""
                dotcode += " -> "
                dotcode += "\""+str(L[d])+"\""
                dotcode += ";\n"
        dotcode += "}"
        # try:
        #     from scapy.all import do_graph
        #     do_graph(dotcode)
        # except:
        #     pass
        return dotcode

def genhypergraphs(vertices):
    #vertices=[1,2,3]
    #baseset = [frozenset([i]) for i in range(vertices)]
    baseset = vertices
    ps = itrecipes.powerset(baseset)
    ps.next() # burn the empty list
    psl = map(frozenset,ps)
    hg = itrecipes.powerset(psl)
    hgs = map(frozenset,hg)
    hgf = map(removesubsets,hgs)
    hgf = list(set(hgf))
    return hgf

def testfullset(hg,numverts):
    fullset = set(range(numverts))
    givenset = set()
    for i in hg:
        for j in i:
            givenset.add(j)
    return fullset.issubset(givenset)

def filternonfull(hgraphlist,numverts):
    return [hh for hh in hgraphlist if testfullset(hh,numverts)]

def filternonfulllist(hgraphlist,numverts):
    return [map(list,hh) for hh in hgraphlist if testfullset(hh,numverts)]

def filteracyclic(hgraphlist, numverts):
    return [hh for hh in hgraphlist if testcycle(hh,numverts)]

def genhypergraphlattice(vertices):
    def intersection(a,b): return removesubsets(a&b)
    def union(a,b): return removesubsets(a|b)
    hgs = genhypergraphs(vertices)
    hgs = sorted(hgs,key=subsetsize)
    L = Lattice(hgs,union,intersection)
    return L

def genhypergraphhasse(L):
    #dotstring = Hasse2(L) #L.Hasse()
    dotstring = Hasse3(L)
    dotstring = dotstring.replace("set","")
    dotstring = dotstring.replace("frozen","")
    dotstring = dotstring.replace("(","")
    dotstring = dotstring.replace(")","")
    dotstring = dotstring.replace("[","{")
    dotstring = dotstring.replace("]","}")
    dotstring = re.sub(r"\{\{(?=[0-9])","{",dotstring)
    dotstring = re.sub(r"(?<=[0-9])\}\}","}",dotstring)
    print dotstring
    return dotstring

def savedotfile(vertices):
    fh = open("output/hypergraphhasse.dot","w")
    #L = genhypergraphlattice(vertices)
    #dotstring = genhypergraphhasse(L)
    ghc=genhypergraphs([1,2,3,4])
    chg = filteracyclic(ghc,4)
    dotstring = genhypergraphhasse(chg)

    fh.write("%s" % dotstring)
    fh.close()

    texcode = dot2tex.dot2tex(dotstring, format='tikz', crop=True)
    texcode = re.sub(r"\{\}","empty",texcode) # using node name {}
                                              # produces a latex error
    fh = open("output/hypergraphhasse.tex","w")
    fh.write("%s" % texcode)
    fh.close()

    subprocess.call("cd output && latexmk -pdf hypergraphhasse.tex",shell=True)
    subprocess.call("cd output && rm hypergraphhasse.log \
                        hypergraphhasse.fdb_latexmk \
                        hypergraphhasse.fls \
                        hypergraphhasse.aux",shell=True)
    subprocess.call("evince output/hypergraphhasse.pdf &",shell=True)
    subprocess.call("pdf2svg output/hypergraphhasse.pdf \
                             output/hypergraphhasse.svg",shell=True)

    # subprocess.call("dot -Tps output/hypergraphhasse.dot -o output/hypergraphhasse.ps",shell=True)
    # subprocess.call("epstopdf output/hypergraphhasse.ps",shell=True)
    # subprocess.call("evince output/hypergraphhasse.pdf",shell=True)
    return dotstring

