import numpy as np
def median(a):
    a.sort()
    print(a)
    if len(a)%2==0:
        b=int(len(a)/2)
        result=(a[b]+a[b-1])/2
        return f'Median equals to {result}'
    elif len(a)%2!=0:
        result=np.percentile(a, 50)
        return f'Median equals to {result}'
