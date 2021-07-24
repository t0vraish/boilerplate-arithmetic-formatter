"""dlw2ty 2enta 3ndk 3245+645 tmm? t3ml regex (import re) ba3deeha 2eh ba2a.
2el 4akl 2el neha2y zay 2el README ba3deeha law fee argument True, ttl3 2el nateega ta7t 2el 5at.
law mfee4 2aw  digits 2ktr mn 2arba3a 2aw operators 8er + aw - 2aw 2ktar mn 4 prblms 2eddy error zay ma maktoob fel README.
problems arg is a list len 4 max.
result arg is False by default and gives answers if True
fst_oprnd
snd_oprnd
oprtr
"""


def arithmetic_arranger(prblms_input, result=False):

    # more than 4 problems
    if len(prblms_input) > 4:
        print("Error: Too many problems.")
        arngd_prblms_lst = None
    # no problems provided
    if len(prblms_input) < 1:
        print("Error: Enter a problem.")
        arngd_prblms_lst = None

    # transcribing the entered list
    for prblm in prblms_input:

        # extracting the operands and operator
        prblm_spltd = prblm.split()
        fst_oprnd = prblm_spltd[0]
        snd_oprnd = prblm_spltd[2]
        oprtr = prblm_spltd[1]

        # no + or - operands
        if oprtr not in ["+", "-"]:
            print("Error: Operator must be '+' or '-'.")
            arngd_prblms_lst = None

        # the formatting in the making, make another list called frmtd_b4_ans each element has prblm
        arngd_prblms_lst = list()
        spaces = 2 + len(str(snd_oprnd))
        if result == True:
            prblm_res = str(eval(prblm))
            arngd_prblm = f"{fst_oprnd.rjust(spaces)}\n{oprtr} {snd_oprnd}\n{'-'*spaces}\n{prblm_res.rjust(spaces)}"
        elif result == False:
            arngd_prblm = (
                f"{fst_oprnd.rjust(spaces)}\n{oprtr} {snd_oprnd}\n{'-'*spaces}"
            )
        arngd_prblms_lst.append(arngd_prblm)

    arngd_prblms = "\t".join(arngd_prblms_lst)

    return arngd_prblms


# DEBUG
ofa7 = arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "-1.723 + 49"], True)
print(ofa7)
