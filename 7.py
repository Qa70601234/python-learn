#!/usr/bin/env python3
from time import time




def main():
    total = 0
    num = [x for x in range(1,100000001)]
    start = time()
    for  i in num:
        total += i 
    print(total)
    end = time()
    print('耗时：%.3fs' % (end - start))
if __name__ == '__main__':
    main()
