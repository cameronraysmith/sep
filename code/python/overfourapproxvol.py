"""
overfourapproxvol.py

use

B. Cousins and S. Vempala, A Cubic Algorithm for Computing Gaussian Volume.
2013. [arXiv:1306.5829](http://arxiv.org/abs/1306.5829v2).

to approximate the volume of the globally consistent polytope
for the case of the overfour graph

overfour = [(0,1,2),(0,1,3),(0,2,3),(1,2,3)]
"""

from minineqrep import *

def approxvol(minineqs,eqfname,error_threshold=0.2):
    minineqstr = re.sub(r'], ',r'],\n',str(minineqs))
    #polyout = runpolymakescript(minineqs,
    #                        "INEQUALITIES", "CENTROID", eqfname)
    #centroid = [float(Fraction(s)) for s in polyout.split()][1:]
    centroid = list(0.125*np.ones(np.shape(minineqs)[1]-1))
    filestring = str("addpath('volconvbod');\n"
                     "aa=%s;\n"
                     "bb = [aa(:,2:end) aa(:,1)];\n"
                     "bb(:,1:end-1)=-1*bb(:,1:end-1);\n"
                     "intpoint = %s';\n"
                     "Volume(bb,[],%s,intpoint)" %
                     (minineqstr, centroid, error_threshold))
    scriptname = eqfname + "Vol"
    fname = open(scriptname + ".m",'w')
    fname.write(filestring)
    fname.close()
    #matlab -nodesktop -nojvm -nosplash -r "run polymakeVol; exit;"
    matprocout = subprocess.check_output(["matlab", "-nodesktop",
                                      "-nojvm", "-nosplash",
                                      "-logfile", scriptname + ".out",
                                      "-r", scriptname + "; exit;"])
    fname = open(scriptname + ".out")
    matout = fname.read()
    fname.close()
    vollist = re.findall(r'(?<=Final Volume: ).*(?=,)',matout)
    vol = float(vollist[0])
    return vol

eqfname = "overfour"
minineqs,dim=minineqgen("overfour")
polyout = runpolymakescript(minineqs, "INEQUALITIES", "VERTICES", "overfour")
boolepolyverts = booleverts(polyout)
volboole = runpolymakescript(boolepolyverts,
                            "POINTS", "VOLUME", eqfname)
volkc = approxvol(minineqs,"overfour",0.01)

#9.17659647818378e-11/3.877906e-10
vol = convert(volboole)/volkc

