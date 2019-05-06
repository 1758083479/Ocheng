'''
import sys

for line in sys.stdin:
    print(eval(line.strip()))
'''

import sys
for line in sys.stdin:
    a,b =line.strip().split('-')
    flag = 0
    a1 = len(a)
    b1= len(b)
    result = ''
    for i in range(a1):
        an = int(a[a1-1-i])
        if b1-i-1<0:
            bn=0
        else:
            bn= int(b[b1-1-i])
        cn = an-bn-flag
        flag = 0
        if cn<0:
            cn+=10
            flag=1
        result = str(cn) + result

    print(result)
