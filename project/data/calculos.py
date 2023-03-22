import numpy as np

def Flujo_calnet(o_f, l_s, a_f, h_f, l_f):
    F_f = 0.0;
    F_f = o_f * (l_s * (1 - a_f)) + h_f + l_f

    return F_f

def Rad_ondac(Za, Zd, Zo):
    Kv = 0.4
    Is = Kv ** 2 * ((np.log((Za - Zd) / Zo)) ** -2)

    return Is

waf = 1.1
cf = 0.0127
paf = 1.124

def Flujo_calsens(LAI):
    cpa = 2932    
    Taf = 317.95
    tf = 313.8
    Hf = (1.1 * LAI * paf * cpa * cf * waf) * (Taf - tf)
    return Hf

def Cal_lat(Tf):
    const = 1.91846e6
    lf = const * (Tf / Tf - 33.91) ** 2
    return lf

def Coef_cn():
    Cf = 0.01 * (1 + 0.3 / waf)
    return Cf

def Cal_latv(lf, LAI, r, qaf):
    Lf = lf * LAI * paf * cf * waf * r * qaf
    return Lf