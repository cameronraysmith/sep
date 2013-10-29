from lattice import Lattice
import itrecipes
import subprocess

def removesubsets(ss):
    fs = frozenset([m for i,m in enumerate(ss) if not any(m < n for n in ss)])
    return fs

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

def genhypergraphlattice(vertices):
    def intersection(a,b): return removesubsets(a&b)
    def union(a,b): return removesubsets(a|b)
    hgs = genhypergraphs(vertices)
    L = Lattice(hgs,union,intersection)
    return L

def genhypergraphhasse(vertices):
    L = genhypergraphlattice(vertices)
    dotstring = L.Hasse()
    dotstring = dotstring.replace("set","")
    dotstring = dotstring.replace("frozen","")
    print dotstring
    return dotstring

def savedotfile(vertices):
    fh = open("hypergraphhasse.dot","w")
    dotstring = genhypergraphhasse(vertices)
    fh.write("%s" % dotstring)
    fh.close()
    subprocess.call("dot -Tps hypergraphhasse.dot -o hypergraphhasse.ps",shell=True)
    subprocess.call("epstopdf hypergraphhasse.ps",shell=True)
    subprocess.call("evince hypergraphhasse.pdf",shell=True)

