import numpy as np
from scipy.stats import truncnorm,halfnorm
from scipy.optimize import fmin_slsqp

import matplotlib.pyplot as plt


def func(p, r, xa, xb):
    return truncnorm.nnlf(p, r)


def constraint(p, r, xa, xb):
    a, b, loc, scale = p
    return np.array([a*scale + loc - xa, b*scale + loc - xb])


xa, xb = 0.007, 0.90
loc = 0.007
scale = .01

a = (xa - loc)/scale
b = (xb - loc)/scale

# Generate some data to work with.
r = truncnorm.rvs(a, b, loc=loc, scale=scale, size=10000)
data=np.loadtxt('tol1.txt')
data=np.loadtxt('tol_76_24_slit.txt')
data=np.loadtxt('tol_all2.txt')
data=np.loadtxt('tol_tilt_offaxis.txt')
data=np.loadtxt('tol.txt')
data=np.loadtxt('tol_field_2.txt')
data=np.loadtxt('tol_all_newaug.txt')
r=data[:,1]*1000
r=data[:,1]
# loc_guess = 0.007
# scale_guess = 0.01
# a_guess = (xa - loc_guess)/scale_guess
# b_guess = (xb - loc_guess)/scale_guess
# p0 = [a_guess, b_guess, loc_guess, scale_guess]

# par = fmin_slsqp(func, p0, f_eqcons=constraint, args=(r, xa, xb),
                 # iprint=False, iter=1000)

# xmin = 0.005
# xmax = 0.1
# x = np.linspace(xmin, xmax, 1000)

fig, ax = plt.subplots(1, 1)
# ax.plot(x, truncnorm.pdf(x, a, b, loc=loc, scale=scale),
        # 'r-', lw=3, alpha=0.4, label='truncnorm pdf')
# ax.plot(x, truncnorm.pdf(x, *par),
        # 'k--', lw=1, alpha=1.0, label='truncnorm fit')
	
p=ax.hist(r, bins=20,histtype='stepfilled', alpha=0.3)
plt.cla()
n=p[0]/200
xn=p[1]
xx=(xn[1:]+xn[:-1])/2
ax.legend(shadow=True)
#plt.xlim(xmin, xmax)
plt.grid(True)
conf=(len(np.where(r<27)[0])/200)*100 
conf2=(len(np.where(r<45)[0])/200)*100 
plt.title('Histogram RMS spot size Tolerence Field [0.0,0.0] ' )
plt.text(28,0.20, "{:.2f}".format(conf) + " %")
plt.text(45,0.20, "{:.2f}".format(conf2) + " %")
#plt.title('Histogram Slit size 80% EE Tolerence Field [0 0] Decenter TilT Distance')
plt.xlabel('RMS spot radius')
plt.xlabel('Slit size 80% EE microns')
plt.ylabel('Fraction')
plt.xlim([18,60])
plt.bar(xx,n,xn[1]-xn[0],alpha=0.4)
plt.plot([27,27],[0, 0.3], 'k-', lw=4, color='green',label='3 pixel boundary')
plt.plot([45,45],[0, 0.3], 'k-', lw=4, color='green',label='5 pixel boundary')
plt.legend()
plt.show()
