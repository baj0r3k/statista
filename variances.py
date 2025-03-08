from SGH_Statystyka_wzory.averages import w_average,value_average,normal_average

def variance_o1(a):
    return sum([((b-normal_average(a))**2)/len(a) for b in a])

def variance_o2(a):
    b=sum([i for _,i in a])
    return sum([(r*((g-value_average(a))**2))/b for g,r in a])

def variance_o3(a):
    return sum([((b-w_average(a))**2)*c for b,c in a])

def expected(a):
    return sum(c*b for c,b in a)

def variance_p(a):
    return sum([((c-expected(a))**2)*b for c,b in a])
