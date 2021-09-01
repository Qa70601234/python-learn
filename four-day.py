#!/usr/bin/env python3
print(1)
for i in range(5):
    print('*'*i)
print(2)
print('')
for i in range(6):    
    print(' '*(5-i),end='')
    print('*'*i)
print(3)
for i in range(6):
    print(' '*(5-i),end='')
    print('*'*(i*2-1))
    