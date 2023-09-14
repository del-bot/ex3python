## n = int(input('input number of coins'))
## count_0 = 0
## count_1 = 0
## for i in range(n):
##    m = int(input())
##    if m == 0:
##        count_0 +=1
##    else:
##        count_1 +=1
## print(count_1 if count_0 > count_1 else count_0)

##import math

#s = int(input('input sum of numbers'))
#p = int(input('input mult numbers'))
#d = s*s - 4*p

#if d > 0:
#    x1 = (s + math.sqrt(d)) / 2
#    print(f'first number {x1}, second number {p/x1}')
#    x2 = (s - math.sqrt(d)) / 2
#    print(f'first number{x2}, second number{p/x2}')
#elif d == 0:
#    x1 = s/2
#    print(f'first number{x1}, second number{p/x1}')
#elif d < 0:
#    print('no radix')
#else:
#    print('impossible')

n = int(input('input N number'))
i = 0
while 2**i  < n:
    print(2**i)
    i +=1
 