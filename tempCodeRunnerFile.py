import re

hoe = "36223 +2345"
print(re.findall("([0-9.]+)[+-]", hoe))