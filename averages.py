def normal_average(a):
    return sum([b/len(a) for b in a])

def value_average(a):                       #tutaj w listę przedstawiamy w postaci krotek
    b=sum([i for _,i in a])
    return sum([(f*e)/b for f,e in a])

def w_average(a):
    return sum([f * e for f, e in a])

