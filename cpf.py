#!/usr/bin/env python3
"""Verify if CPF is valid.

author: alvaro salgado
salgado.alvaro@me.com
"""

import numpy as np
import sys


def verify(cpf):
    """Verify cpf. cpf must be entered as a string."""
    body_1 = cpf[:-2]
    dv = cpf[-2:]

    b1 = np.array(list(body_1)).astype(int)
    multiplication = np.array([10, 9, 8, 7, 6, 5, 4, 3, 2])
    sum1 = (b1 * multiplication).sum()

    mod_1 = sum1 % 11
    if ((mod_1 == 0) or (mod_1 == 1)):
        dv_1 = 0
    else:
        dv_1 = 11 - mod_1

    body_2 = cpf[1:-2] + str(dv_1)
    b2 = np.array(list(body_2)).astype(int)
    sum2 = (b2 * multiplication).sum()

    mod_2 = sum2 % 11
    if ((mod_2 == 0) or (mod_2 == 1)):
        dv_2 = 0
    else:
        dv_2 = 11 - mod_2

    return ((str(dv_1) == dv[0]) and (str(dv_2) == dv[1]))

"""############################################
MAIN
############################################"""

cpf = sys.argv[1]
legible_cpf = cpf[0:3] + '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[-2:]

valid = verify(cpf)
valid

if valid is True:
    print(legible_cpf, 'is a VALID CPF')
else:
    print(legible_cpf, 'is NOT a valid CPF')
