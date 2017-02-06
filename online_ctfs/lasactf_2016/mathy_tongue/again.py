#!/usr/bin/env python
# -*- coding, utf-8 -*-
# @Author, john
# @Date,   2016-03-20 00,39,55
# @Last Modified by,   john
# @Last Modified time, 2016-03-20 01,11,49


import sympy

nadokalol, mekalal, nadokalkalol, pekalol, sakalal, namekalal, fanamekalol, dokalkalol, fanavodokalkalal, dokalol, lokalal, rekalol, sakalkalal, gokalkalkalol, nalokalal, nafanavolokalkalkalol, zokalal, nagokalol, fanagokalal, gokalol, nazokalal, fanazokalol, lokalkalal= sympy.symbols('nadokalol, mekalal, nadokalkalol, pekalol, sakalal, namekalal, fanamekalol, dokalkalol, fanavodokalkalal, dokalol, lokalal, rekalol, sakalkalal, gokalkalkalol, nalokalal, nafanavolokalkalkalol, zokalal, nagokalol, fanagokalal, gokalol, nazokalal, fanazokalol, lokalkalal')

counting_equations = [
sympy.Eq(lokalal,nagokalol-1),
sympy.Eq(lokalal,fanagokalal-2),
sympy.Eq(lokalal,gokalol-3),
sympy.Eq(lokalal,nazokalal-4),
sympy.Eq(lokalal,fanazokalol-5),
sympy.Eq(lokalal,zokalal-6),
sympy.Eq(nagokalol,lokalal+1),
sympy.Eq(nagokalol,fanagokalal-1),
sympy.Eq(nagokalol,gokalol-2),
sympy.Eq(nagokalol,nazokalal-3),
sympy.Eq(nagokalol,fanazokalol-4),
sympy.Eq(nagokalol,zokalal-5),
sympy.Eq(fanagokalal,lokalal+2),
sympy.Eq(fanagokalal,nagokalol+1),
sympy.Eq(fanagokalal,gokalol-1),
sympy.Eq(fanagokalal,nazokalal-2),
sympy.Eq(fanagokalal,fanazokalol-3),
sympy.Eq(fanagokalal,zokalal-4),
sympy.Eq(gokalol,lokalal+3),
sympy.Eq(gokalol,nagokalol+2),
sympy.Eq(gokalol,fanagokalal+1),
sympy.Eq(gokalol,nazokalal-1),
sympy.Eq(gokalol,fanazokalol-2),
sympy.Eq(gokalol,zokalal-3),
sympy.Eq(nazokalal,lokalal+4),
sympy.Eq(nazokalal,nagokalol+3),
sympy.Eq(nazokalal,fanagokalal+2),
sympy.Eq(nazokalal,gokalol+1),
sympy.Eq(nazokalal,fanazokalol-1),
sympy.Eq(nazokalal,zokalal-2),
sympy.Eq(fanazokalol,lokalal+5),
sympy.Eq(fanazokalol,nagokalol+4),
sympy.Eq(fanazokalol,fanagokalal+3),
sympy.Eq(fanazokalol,gokalol+2),
sympy.Eq(fanazokalol,nazokalal+1),
sympy.Eq(fanazokalol,zokalal-1),
sympy.Eq(zokalal,lokalal+6),
sympy.Eq(zokalal,nagokalol+5),
sympy.Eq(zokalal,fanagokalal+4),
sympy.Eq(zokalal,gokalol+3),
sympy.Eq(zokalal,nazokalal+2),
sympy.Eq(zokalal,fanazokalol+1),
]

adding_equations =  [
sympy.Eq(nadokalol * mekalal , nadokalkalol),
sympy.Eq(pekalol + mekalal , sakalal),
sympy.Eq(namekalal + fanamekalol , mekalal),
sympy.Eq(dokalkalol - namekalal , fanavodokalkalal),
sympy.Eq(namekalal * dokalol , fanamekalol * pekalol),
sympy.Eq(lokalal * mekalal , lokalkalal),
sympy.Eq(pekalol + pekalol + mekalal - lokalal , rekalol),
sympy.Eq(sakalkalal * pekalol , gokalkalkalol),
sympy.Eq(dokalol , sakalal + mekalal),
sympy.Eq(pekalol + pekalol - sakalal - mekalal , rekalol),
sympy.Eq(lokalal - pekalol , sakalal),
#sympy.Eq(nadokalol * nalokalal , nafanavolokalkalkalol),
sympy.Eq(namekalal + namekalal , fanamekalol),
sympy.Eq(fanamekalol * mekalal , pekalol),
sympy.Eq(zokalal + pekalol , sakalkalal) ]

variables = [nadokalol, mekalal, nadokalkalol, pekalol, sakalal, namekalal, fanamekalol, dokalkalol, fanavodokalkalal, dokalol, lokalal, rekalol, sakalkalal, gokalkalkalol, 
#nalokalal, 
#nafanavolokalkalkalol,
     zokalal, nagokalol, fanagokalal, gokalol, nazokalal, fanazokalol, lokalkalal]


other_eqs = [
sympy.Eq(fanagokalal, fanazokalol - 3),
sympy.Eq(nagokalol, fanazokalol - 4),
sympy.Eq(lokalal, fanazokalol - 5),
sympy.Eq(zokalal, fanazokalol + 1),
sympy.Eq(gokalol, fanazokalol - 2),
sympy.Eq(nazokalal, fanazokalol - 1),
]

together = other_eqs + adding_equations
print "total number equations", len(together)
print "total number variables", len(variables)

equations = \
'''fanagokalal == fanazokalol - 3
nagokalol == fanazokalol - 4
lokalal == fanazokalol - 5
zokalal == fanazokalol + 1
gokalol == fanazokalol - 2
nazokalal == fanazokalol - 1
mekalal*nadokalol == nadokalkalol
mekalal + pekalol == sakalal
fanamekalol + namekalal == mekalal
dokalkalol - namekalal == fanavodokalkalal
dokalol*namekalal == fanamekalol*pekalol
lokalal*mekalal == lokalkalal
-lokalal + mekalal + 2*pekalol == rekalol
pekalol*sakalkalal == gokalkalkalol
dokalol == mekalal + sakalal
-mekalal + 2*pekalol - sakalal == rekalol
lokalal - pekalol == sakalal
2*namekalal == fanamekalol
fanamekalol*mekalal == pekalol
pekalol + zokalal == sakalkalal'''

print "==removing unecessary variables=="
for variable in variables:
    # variable = str(variable)
    # count = equations.count(variable)
    if (equations.count(str(variable))) == 0:
        print "* should remove", str(variable)
        # variables.remove(variable)
    # if count == 0:
    #     print "* should remove", variable
    #     variables.remove(eval(variable))

print "total number equations", len(together)
print "total number variables", len(variables)

count = 1
for line in equations.split('\n'):
    print count, line
    count += 1

# print sympy.solve(together , variables)
print ""
print "==========================="
count = 0
for variable in variables:
    var = str(variable)
    # print var
    print var, "maps to", chr(97+count)
    equations = equations.replace(var, chr(97+count))
    count += 1
    # print equations
    print ""

count = 1
for line in equations.split('\n'):
    print count, line
    count += 1

sympy.solve(together, variables)