"""dlw2ty 2enta 3ndk 3245+645 tmm? t3ml regex (import re) ba3deeha 2eh ba2a.
2el 4akl 2el neha2y zay 2el README ba3deeha law fee argument True, ttl3 2el nateega ta7t 2el 5at.
law mfee4 2aw  digits 2ktr mn 2arba3a 2aw operators 8er + aw - 2aw 2ktar mn 4 prblms 2eddy error zay ma maktoob fel README.
problems arg is a list len 4 max.
result arg is False by default and gives answers if True
fst_oprnd
snd_oprnd
oprtr
"""

import re


def arithmetic_arranger(problems, result=False):

    # more than 4 problems
    if len(problems) > 4:
        print("Error: Too many problems.")
        arranged_problems = None
    # no problems provided
    if len(problems) < 1:
        print("Error: Enter a problem.")
        arranged_problems = None

    # transcribing the entered list
    for problem in problems:

        # no + or - operands
        if re.search("[+-]", problem) is None:
            print("Error: Operator must be '+' or '-'.")
            arranged_problems = None

        # extracting the operands and operator
        fst_oprnd = str(re.findall("()[+-]", problem)[0])
        snd_oprnd = str(re.findall("[+-]()", problem)[0])
        oprtr = str(re.findall("[+-]", problem)[0])

        # the formatting in the making, make another list called frmtd_b4_ans each element has prblm
        arngd_prblms_lst = list()
        spaces = 2 + len(str(snd_oprnd))
        arngd_prblm = f"{fst_oprnd.rjust(spaces)}\n{oprtr} {snd_oprnd}\n{'-'*spaces}"
        arngd_prblms_lst.append(arngd_prblm)
    return arngd_prblms_lst
