import random

lst = random.sample(range(0, 10), 10)  
code1 = str([n for n in lst])

code2 = ''
for b in lst:
    code2+=str(b)

print('1 -', code1)
print('2 -', code2)

code3 = ''.join(lst)
print('3 -', code3)