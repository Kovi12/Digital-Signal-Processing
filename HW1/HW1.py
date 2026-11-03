###Examples
from timeit import default_timer as timer

import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import hamming, firwin, butter
print("##Examples")

##2.19

print("#2.19")
# create a 2x2 matrix
A = np.array([[2, 1], [4, 3]])

# compute the inverse of A using inv() function
AInv1 = np.linalg.inv(A)

# compute the inverse of A using the backslash operator and eye() function
AInv3 = np.eye(A.shape[0]) / A

print("Inverse of A using inv():\n", AInv1)
print("Inverse of A using backslash operator and eye():\n", AInv3)

##2.46
print("#2.46")
n = int(input("We will compute the sum of positive integer numbers up to n = "))
s = 0
for index in range(1, n + 1):
    s = s + index
print("The sum is", s)

##3.4
print("#3.4")
# define the initial sequence
a = np.array([1, 2, 4, 5, 6, 7, 8, 9, 5, 3])

# plot the initial sequence
plt.stem(a)
plt.axis([0, len(a) + 1, min(a) - 1, max(a) + 1])
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('Discrete aperiodic sequence')
plt.show()

# build the periodic sequence by repeating the initial sequence 20 times
a_periodic = np.tile(a, 20)

# plot the periodic sequence
plt.stem(a_periodic)
plt.axis([0, len(a_periodic) + 1, min(a_periodic) - 1, max(a_periodic) + 1])
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('Discrete periodic sequence')
plt.show()

##4.5
print("#4.5")
# Define the parameters
A = 1
fs = 100
t = np.arange(-100, 101) / fs
x = np.zeros_like(t)
x[t == 0] = A

# Plot the time domain signal
plt.subplot(2, 1, 1)
plt.plot(t, x), plt.axis([-5, 5, -.5, 1.5])
plt.title('Amplitude of the Impulse function')
plt.xlabel('Time (s)'), plt.ylabel('Amplitude')

# Compute the single-sided magnitude spectrum
X = np.fft.fft(x)
Z = np.abs(X)
N = int(np.ceil(len(Z) / 2))
Z = Z[0:N]
f = np.arange(N) * fs / (2 * N)
plt.subplot(2, 1, 2)
plt.plot(f, Z)
plt.title('Magnitude spectrum - single sided')
plt.xlabel('Frequency (Hz)'), plt.ylabel('Magnitude')

plt.show()

##6.7
print("#6.7")
wc = 0.3  # normalized cut-off frequency
n = 21  # filter order
h = wc * np.sinc(wc * (np.arange(-(n - 1) / 2, (n - 1) / 2 + 1)))  # impulse response is sinc
window = hamming(n)  # compute window coefficients with hamming
b1 = h * window  # computed multiplying sinc with Hamming window
b2 = firwin(n, wc)  # computed directly using firwin

plt.plot(b1, 'ob')
plt.plot(b2, 'r')
plt.gca().set_prop_cycle(None)  # equivalent to plt.hold(True) in older versions
plt.xlabel('Index')
plt.ylabel('Amplitude')
plt.show()

###Exercises
print("##Exercises")
##2.16
print("#2.16")
# Create an array of odd integers between 23 and 175
arr = np.arange(23, 176, 2)

# Find the indices of multiples of 5 in the array
idx = np.where(arr % 5 == 0)[0]

# Remove the multiples of 5 from the array
arr = np.delete(arr, idx)

# Print the resulting array
print(arr)

##2.44
print("#2.44")
n = 1000
A = np.random.rand(n, n)
b = np.random.rand(n)

start_time = timer()
x = np.linalg.solve(A, b)
end_time = timer()
print("Execution time using solve function:", end_time - start_time, "seconds")

start_time = timer()
x = np.dot(np.linalg.inv(A), b)
end_time = timer()
print("Execution time using inverse function:", end_time - start_time, "seconds")


##3.28
print("#3.28")
def myTriangularPulse(A, t1, t2, t3, t):
    x = np.zeros_like(t)
    x[(t >= t1) & (t < t2)] = A / (t2 - t1) * (t[(t >= t1) & (t < t2)] - t1)
    x[(t >= t2) & (t < t3)] = A / (t2 - t3) * (t[(t >= t2) & (t < t3)] - t3)
    return x


A = 1
fs = 10
t = np.arange(-2, 5, 1 / fs)

x = myTriangularPulse(A, 1, 3, 4, t)

# plot signal
plt.subplot(2, 1, 1)
plt.plot(t, x)
plt.title('Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

# plot envelope
env = np.zeros_like(t)
env[(t >= 1) & (t < 4)] = 1
plt.subplot(2, 1, 2)
plt.plot(t, env)
plt.title('Envelope')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()


# 3.55
print("#3.55")
def sampleAndHoldA(f, t0, t1, fs):
    t = np.arange(t0, t1, 1 / fs)
    x = f(t)
    x_samp = np.zeros(len(t))
    for i in range(len(t)):
        if i == 0:
            x_samp[i] = x[i]
        else:
            x_samp[i] = x_samp[i - 1]
            if t[i] >= i / fs:
                x_samp[i] = x[i]
    return t, x_samp


# Define the function to be sampled
def myFunc(t):
    return np.sin(2 * np.pi * t) + 0.5 * np.cos(4 * np.pi * t)


# Sample the function with a sampling frequency of 10 Hz
t0 = 0
t1 = 2
fs = 10
t, x = sampleAndHoldA(myFunc, t0, t1, fs)

# Plot the original function and the sampled points
t_cont = np.linspace(t0, t1, 1000)
x_cont = myFunc(t_cont)

plt.plot(t_cont, x_cont, label='Original function')
plt.stem(t, x, label='Sampled points')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.show()

##4.25
print("#4.25")
t = np.linspace(-5, 5, 1000)
f = np.heaviside(t, 1)
df = np.diff(f)

N = len(df)
freq = np.fft.fftfreq(N)
df_fft = np.fft.fft(df)

mag = np.abs(df_fft)
phase = np.angle(df_fft)

plt.figure(figsize=(10, 5))
plt.subplot(2, 1, 1)
plt.plot(freq, mag)
plt.title('Magnitude spectrum of Step function')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(freq, phase)
plt.title('Phase spectrum of Step function')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Phase (rad)')
plt.grid(True)

plt.tight_layout()
plt.show()


##5.19
print("#5.19")
def OverlapSave(h, x):
    L = len(x)
    M = len(h)
    P = 2 ** (int(np.ceil(np.log2(L + M - 1))))

    # zero-pad h and x
    np.pad(h, (0, P - M), mode='constant')
    x_pad = np.pad(x, (0, M - 1), mode='constant')

    # create window function
    window = np.zeros(P)
    window[:M] = h
    window = np.roll(window, -M // 2)

    # perform convolution using overlap-add method
    y = np.zeros(L + M - 1)
    for i in range(0, L, P - M):
        x_block = x_pad[i:i + P - M]
        X_block = np.fft.fft(x_block, P)
        Y_block = np.fft.ifft(X_block * np.fft.fft(window, P))
        y[i:i + P - M] += np.real(Y_block)[:P - M]

    return y


h = np.array([1, 2, 3, 4, 5])
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
y = OverlapSave(h, x)
print(y)

##6.23
print("#6.23")
# Butterworth filter order
n = 3

# Cutoff frequency in radians per second
wc = 1.0

# Analog transfer function
b, a = butter(n, wc, analog=True)
print('Analog transfer function: H(s) =', b, '/', a)

##Nfact recursive
print("##Nfact recursive")
def fact(n):
    if n == 0 or n == 1:
        return n
    return n * fact(n-1)

print(fact(5))