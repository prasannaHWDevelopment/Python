import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn-poster')
%matplotlib inline
# Sampling Rate
s_r = 2000
# Sampling Interval
t_s = 1.0/s_r
t = np.arange(0,1,t_s)
% FRequencies of the signal 
freq = 1000.234
x = 3*np.sin(2*np.pi*freq*t)

freq = 4000
x += np.sin(2*np.pi*freq*t)

freq = 7000   
x += 0.5* np.sin(2*np.pi*freq*t)

plt.figure(figsize = (10, 8))
plt.plot(t, x, 'r')
plt.ylabel('Amplitude')

plt.show()

from numpy.fft import fft, ifft

X = fft(x)
N = len(X)
n = np.arange(N)
T = N/s_r
freq = n/T 

plt.figure(figsize = (14, 8))
plt.subplot(121)

plt.stem(freq, np.abs(X), 'b', \
         markerfmt=" ", basefmt="-b")
plt.xlabel('Freq (Hz)')
plt.ylabel('FFT Amplitude |X(freq)|')
plt.xlim(0, 10)

plt.subplot(122)
plt.plot(t, ifft(X), 'r')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.tight_layout()
plt.show()
