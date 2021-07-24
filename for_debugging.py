import re

prblm = "  -3.6223 +   -2.345  "
# print(re.findall("[+-]", hoe))

# fst_oprnd = "-5.754"
# oprtr = "+"
# snd_oprnd = "-5377"
# spaces = 2 + len(str(snd_oprnd))
# arranged_problem = f"{fst_oprnd.rjust(spaces)}\n{oprtr} {snd_oprnd}\n{'-'*spaces}"
# print(arranged_problem)

splted = prblm.split()

fst_oprnd = splted[0]
snd_oprnd = splted[2]
oprtr = splted[1]
# print(fst_oprnd, snd_oprnd, oprtr)
prblm_res = str(eval(prblm))
spaces = 2 + len(str(snd_oprnd))
arngd_prblm = f"{fst_oprnd.rjust(spaces)}\n{oprtr} {snd_oprnd}\n{'-'*spaces}\n{prblm_res.rjust(spaces)}"
print(arngd_prblm)
