import re

hoe = "36223 +2345"
print(re.findall("[+-]", hoe))

fst_oprnd = "-5.754"
oprtr = "+"
snd_oprnd = "-5377"
spaces = 2 + len(str(snd_oprnd))
arranged_problem = f"{fst_oprnd.rjust(spaces)}\n{oprtr} {snd_oprnd}\n{'-'*spaces}"
print(arranged_problem)
