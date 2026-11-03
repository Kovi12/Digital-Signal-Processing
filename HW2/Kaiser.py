#fc1 = 1600 	fc2 = 3600  	ft = 200	rp = 0.2	rs = 45 	filter type = HP	FIR window = Kaiser 	IIR Type = Chebyshev type II
import numpy as np
import scipy.signal as sp
import matplotlib.pyplot as plt

fs = 8000
fc = 1600
ft = 200
w = np.array([fc/(fs/2)])
r = 45
wt = ft/(fs/2)

wp = np.array([fc - ft / 2]) / (fs / 2)
ws = np.array([fc + ft / 2]) / (fs / 2)

N, beta = sp.kaiserord(r, wt)
b = sp.firwin(N, w, window=('kaiser', beta), pass_zero='highpass', fs=fs)
w, h = sp.freqz(b,a=1, worN=512, plot=None)
f = (fs / 2) * w / (np.pi)

print(N)

plt.close('all')
plt.plot(f, abs(h), linewidth=3)
plt.show()
