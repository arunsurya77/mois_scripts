import numpy as np
import matplotlib.pyplot as plt

T=77

#F_SILICA CORNING arXiv:0805.0091
S1 = np.poly1d([1.75949E-12, -1.59700E-09, 5.27414E-07, -4.94251E-05, 1.10127E+00])
S2 = np.poly1d([-1.57223E-12,1.44546E-09, -4.49019E-07, 4.76391E-05, 1.78752E-05])
S3 = np.poly1d([1.48829E-10, -9.20275E-08, 1.84595E-05, -1.27815E-03, 7.93552E-01])
L1 = np.poly1d([6.84605E-14, 7.77072E-11, -6.53638E-08, 9.08730E-06 , -8.90600E-02])**2
L2 = np.poly1d([7.85145E-13, -1.09482E-08, 6.59069E-06, -8.59578E-04, 2.97562E-01])**2
L3 = np.poly1d([8.21348E-10, -5.07660E-07, 1.01968E-04, -7.09788E-03, 9.34454E+00])**2

FSIL_S1=S1(T)
FSIL_S2=S2(T)
FSIL_S3=S3(T)
FSIL_L1=L1(T)
FSIL_L2=L2(T)
FSIL_L3=L3(T)

#ZNS Leviton 2013 
S1 = np.poly1d([6.91051E-11, -4.14798E-08, 1.01086E-05, -5.12262E-04, 3.35933])
S2 = np.poly1d([-6.54805E-11,3.81621E-08, -8.91159E-06, 4.89603E-04, 0.706131])
S3 = np.poly1d([8.31188E-10, -7.57289E-07, 2.31080E-04, -2.93193E-02, 4.02154])
L1 = np.poly1d([2.29917E-12, -1.23408E-09, 2.73286E-07, -8.93057E-06 , 0.161151])**2
L2 = np.poly1d([4.35237E-12, -2.77513E-09, 7.55906E-07, -4.66636E-05, 0.282427])**2
L3 = np.poly1d([4.16370E-09, -3.95895E-06, 1.23906E-03, -0.161010, 41.1590])**2

ZNS_S1=S1(T)
ZNS_S2=S2(T)
ZNS_S3=S3(T)
ZNS_L1=L1(T)
ZNS_L2=L2(T)
ZNS_L3=L3(T)


#BAF2 Leviton JWST
S1 = np.poly1d([3.650068E-12, -1.332822E-10, -1.884197E-06, -8.986505E-04, 8.285359E-01])
S2 = np.poly1d([-3.904140E-12, 5.257707E-10, 1.656780E-06, 9.091254E-04, 3.315039E-01])
S3 = np.poly1d([-1.764139E-10, -4.302326E-08, 7.204123E-05, -1.161161E-02, 4.367314E+00])
L1 = np.poly1d([-7.312824E-11, 5.231437E-08, -1.277585E-05, 8.880306E-04 , 8.362026E-02])**2
L2 = np.poly1d([-4.348650E-11, 4.686248E-08, -1.897870E-05, 3.381142E-03, -1.148764E-01])**2
L3 = np.poly1d([-8.848551E-10, -3.280396E-07, 4.283633E-04, -6.672202E-02, 4.921549E+01])**2

BAF2_S1=S1(T)
BAF2_S2=S2(T)
BAF2_S3=S3(T)
BAF2_L1=L1(T)
BAF2_L2=L2(T)
BAF2_L3=L3(T)

#ZNSE Leviton JWST
S1 = np.poly1d([1.26557E-10, -8.77087E-08, 2.00829E-05, -1.13389E-03, 4.41367E+00])
S2 = np.poly1d([-1.18476E-10, 8.10837E-08, -1.80101E-05, 1.11709E-03, 4.47774E-01])
S3 = np.poly1d([2.15956E-09, -1.89210E-06, 5.77330E-04, -8.18190E-02, 6.70952E+00])
L1 = np.poly1d([4.51629E-12, -3.12380E-09, -7.20678E-07, -3.62359E-05 , 1.98555E-01])**2
L2 = np.poly1d([1.53230E-11, -1.07544E-08, 2.56481E-06, -1.56654E-04, 3.82382E-01])**2
L3 = np.poly1d([6.53366E-09, -8.48293E-06, 3.06061E-03, -5.06215E-01, 7.33880E+01])**2

ZNSE_S1=S1(T)
ZNSE_S2=S2(T)
ZNSE_S3=S3(T)
ZNSE_L1=L1(T)
ZNSE_L2=L2(T)
ZNSE_L3=L3(T)

#CAF2 Leviton
S1 = np.poly1d([1.09741437E-09, 7.17518006E-07, -7.38704087E-04, 9.64897439E-01])
S2 = np.poly1d([-9.71236119E-10, -8.40049522E-07, 7.44817508E-04, 8.04911323E-02])
S3 = np.poly1d([2.58329027E-07, -1.67438455E-04, 3.13937373E-02, 2.24550341E+00])
L1 = np.poly1d([-5.27928096E-10, 2.21072817E-07, -1.21180637E-05,-6.61856475E-02])**2
L2 = np.poly1d([-1.29845516E-09, 9.31841153E-07, -2.42570135E-04, 1.40131234E-01])**2
L3 = np.poly1d([1.14612930E-06, -7.43081369E-04, 1.40040106E-01, 2.72931138E+01])**2

CAF2_S1=S1(T)
CAF2_S2=S2(T)
CAF2_S3=S3(T)
CAF2_L1=L1(T)
CAF2_L2=L2(T)
CAF2_L3=L3(T)

print("FSILICA Sellmeier1 Coefficients for ", T, " K")
print("K1 : ","{:e}".format(FSIL_S1))
print("L1 : ","{:e}".format(FSIL_L1))
print("K2 : ","{:e}".format(FSIL_S2))
print("L2 : ","{:e}".format(FSIL_L2))
print("K3 : ","{:e}".format(FSIL_S3))
print("L3 : ","{:e}".format(FSIL_L3))
print(" ")
print("ZNS Sellmeier1 Coefficients for", T, " K")
print("K1 : ","{:e}".format(ZNS_S1))
print("L1 : ","{:e}".format(ZNS_L1))
print("K2 : ","{:e}".format(ZNS_S2))
print("L2 : ","{:e}".format(ZNS_L2))
print("K3 : ","{:e}".format(ZNS_S3))
print("L3 : ","{:e}".format(ZNS_L3))
print(" ")
print("ZNSE Sellmeier1 Coefficients for ", T, " K")
print("K1 : ","{:e}".format(ZNSE_S1))
print("L1 : ","{:e}".format(ZNSE_L1))
print("K2 : ","{:e}".format(ZNSE_S2))
print("L2 : ","{:e}".format(ZNSE_L2))
print("K3 : ","{:e}".format(ZNSE_S3))
print("L3 : ","{:e}".format(ZNSE_L3))
print(" ")
print("BAF2 Sellmeier1 Coefficients for ", T, " K")
print("K1 : ","{:e}".format(BAF2_S1))
print("L1 : ","{:e}".format(BAF2_L1))
print("K2 : ","{:e}".format(BAF2_S2))
print("L2 : ","{:e}".format(BAF2_L2))
print("K3 : ","{:e}".format(BAF2_S3))
print("L3 : ","{:e}".format(BAF2_L3))
print(" ")
print("CAF2 Sellmeier1 Coefficients for ", T, " K")
print("K1 : ","{:e}".format(CAF2_S1))
print("L1 : ","{:e}".format(CAF2_L1))
print("K2 : ","{:e}".format(CAF2_S2))
print("L2 : ","{:e}".format(CAF2_L2))
print("K3 : ","{:e}".format(CAF2_S3))
print("L3 : ","{:e}".format(CAF2_L3))

