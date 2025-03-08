from SGH_Statystyka_wzory.averages import w_average,value_average,normal_average
from SGH_Statystyka_wzory.variances import variance_o1,variance_o2,variance_o3
import numpy as np
def normal_asymetry(a):
    return sum([(b-normal_average(a))**3/len(a) for b in a])/(np.sqrt(variance_o1(a)))**3

def coe_1(a):
    return np.sqrt(variance_o1(a))/normal_average(a)*100
def coe_2(a):
    return np.sqrt(variance_o2(a))/value_average(a)*100
def coe_3(a):
    return np.sqrt(variance_o3(a))/w_average(a)*100