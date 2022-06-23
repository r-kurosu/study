import math
from unicodedata import name

a = [1, 1/11]

def zenkasiki(n):
    a.append((34/11) * a[n+1] - (3/11)*a[n])
    
    return


def main():
    for i in range(0,51):
        zenkasiki(i)
        # print(f"a_{i} = {a[i]}")
        if i == 0:
            continue
        
        print(f"n={i} : a[n]/a[n-1] = {a[i]/a[i-1]}")
        
    return



main()