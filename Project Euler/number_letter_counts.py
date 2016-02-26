import inflect
import re

count = 0
num = inflect.engine()

for i in range(1,1001):
    count+=len(re.sub('[ -]','',num.number_to_words(i)))
print(count)
