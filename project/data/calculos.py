import numpy as np

def Flujo_calnet(o_f, l_s, a_f, h_f, l_f):
    F_f = 0.0;
    F_f = o_f * (l_s * (1 - a_f)) + h_f + l_f

    return F_f

def Rad_ondac(Za, Zd, Zo):
    Kv = 0.4
    Is = Kv ** 2 * ((np.log((Za - Zd) / Zo)) ** -2)

    return Is

def Flujo_calsens(LAI, paf, cpa, cf, waf, Taf, tf):
    
    Hf = (1.1 * LAI * paf * cpa * cf * waf) * (Taf - tf)
    return Hf

def Cal_lat():
    return

def Coef_cn():
    return

def Cal_latv():
    return

def rel_macv():
    return

def rel_mstc():
    return