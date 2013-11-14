from minineqrep import *
eqfname = "overfour"
minineqs,dim=minineqgen("overfour")
polyout = runpolymakescript(minineqs, "INEQUALITIES", "VERTICES", "overfour")
boolepolyverts = booleverts(polyout)
volboole = runpolymakescript(boolepolyverts,
                            "POINTS", "VOLUME", eqfname)
volkc = approxvol(minineqs,"overfour",0.01)

#9.17659647818378e-11/3.877906e-10
vol = convert(volboole)/volkc

