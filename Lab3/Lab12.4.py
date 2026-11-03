import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as dsp
N = 5
fs = 4000.
f = np.array([1500])/(fs/2)
b, a = dsp.butter(N, f, btype='low')
f, H = dsp.freqz(b,a,fs=fs)
plt.close('all')
plt.subplot(2,2,1)
plt.plot(f,abs(H))
plt.title('Butterworth with order ' +  str(N))
plt.grid('on')

N = 5
fs = 4000.
ripple = 0.3
f = np.array([1500])/(fs/2)
b, a = dsp.cheby1(N, ripple, f)
f, H = dsp.freqz(b,a,fs=fs)
plt.subplot(2,2,2)
plt.plot(f,abs(H))
plt.title('Cheby1 with order ' +  str(N))
plt.grid('on')
plt.show()