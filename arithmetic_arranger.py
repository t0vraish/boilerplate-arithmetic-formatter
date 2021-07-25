"""
How the code works:
- You get the list of input function strings
- For each string you split it and assign each operand to a variable, then turn it into a string
- The program then checks which number is longer and adjust the spacing using the "spaces" variable and adjusts the number  of dashes
- Then checks for "result" argument in the function and adds the result of the inserted problem string
- After that, the resultant formatted string is appended to a list which is returned through the function
- Theres error checking if there are more than 4 problems entered, no problems, if there weren't digits entered, if the operand isn't "+" or "-"
"""


def arithmetic_arranger(prblms_input, result=False):

    # more than 4 problems
    if len(prblms_input) > 4:
        print("Error: Too many problems.")
        arngd_prblms_lst = None
        exit()
    # no problems provided
    if len(prblms_input) < 1:
        print("Error: Enter a problem.")
        arngd_prblms_lst = None
        exit()

    arngd_prblms_lst = list()
    # transcribing the entered list
    for prblm in prblms_input:

        # extracting the operands and operator
        prblm_spltd = prblm.split()
        fst_oprnd = prblm_spltd[0]
        snd_oprnd = prblm_spltd[2]
        oprtr = prblm_spltd[1]

        # no digits entered
        try:
            fst_flt_tst = float(fst_oprnd)
            snd_flt_tst = float(snd_oprnd)
        except:
            print("Error: Numbers must only contain digits.")
            exit()

        # no + or - operands
        if oprtr not in ["+", "-"]:
            print("Error: Operator must be '+' or '-'.")
            arngd_prblms_lst = None
            exit()

        # the formatting in the making, make another list called frmtd_b4_ans each element has prblm

        # making sure spacing is alright
        if len(str(snd_oprnd)) > len(str(fst_oprnd)):
            spaces = 2 + len(str(snd_oprnd))
            fst_oprnd_frmt = fst_oprnd.rjust(spaces)
            snd_oprnd_frmt = snd_oprnd
        else:
            spaces = 2 + len(str(fst_oprnd))
            fst_oprnd_frmt = fst_oprnd.rjust(spaces)
            snd_oprnd_frmt = snd_oprnd.rjust(spaces - 2)

        # real deal formatting
        if result == True:
            prblm_rslt = str(eval(prblm))
            arngd_prblm = f"{fst_oprnd_frmt}\n{oprtr} {snd_oprnd_frmt}\n{'-'*spaces}\n{prblm_rslt.rjust(spaces)}"
        elif result == False:
            arngd_prblm = f"{fst_oprnd_frmt}\n{oprtr} {snd_oprnd_frmt}\n{'-'*spaces}"

        # joining multiple formatted problems into a list
        arngd_prblms_lst.append(arngd_prblm)

    # turning the list into a single string
    # arngd_prblms = "\t".join(arngd_prblms_lst)

    # how to handle if there's an error and getting the final result
    return arngd_prblms_lst


# DEBUG
# testing = arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "9999 + 9999"], True)
# for prblm in testing:
#     print(f"{prblm}\n")
