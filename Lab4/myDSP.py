import numpy as np
import sounddevice as sd
import soundfile as sf
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy import signal


def mySine(A, f, ph, t):
    return A * np.sin(2 * np.pi * f * t + ph)


def myStep(A, t0, t):
    return A * (t >= t0)


def readWav(fileName):
    data, fs = sf.read(fileName)
    return data, fs


def playWav(y, fs):
    sd.play(y, fs)


def plotInTime(y, fs):
    plt.close()
    plt.figure()
    N = np.size(y, 0)
    t = np.arange(N) / fs
    plt.plot(t, y)
    plt.xlabel('Times (s)')
    plt.ylabel('Amplitude')
    plt.grid('on')
    plt.show()


def plotInFrequency(y, fs):
    plt.close()
    plt.figure()
    N = int(np.ceil(np.size(y, 0) / 2))
    f = (fs / 2) * np.arange(N) / (N - 1)
    Yleft = abs(np.fft.fft(y[:, 0]))
    Yright = abs(np.fft.fft(y[:, 1]))
    plt.plot(f, Yleft[:N], f, Yright[:N])
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    plt.grid('on')
    plt.show()



def myDFT(x):
    N = np.size(x)
    X = np.zeros(N, dtype=complex)
    for k in range(N):
        for n in range(N):
            X[k] = X[k] + x[n] * np.exp(-2j * np.pi * k * n / N)
    return (X)



def spectrogram(file):
    # Load audio file
    sample_rate, samples = wavfile.read(file)

    # Set up the spectrogram parameters
    nperseg = 512
    noverlap = int(nperseg * 0.5)

    # Compute spectrogram
    frequencies, times, spectrogram = signal.spectrogram(samples, sample_rate, nperseg=nperseg, noverlap=noverlap)

    # Plot spectrogram
    plt.pcolormesh(times, frequencies, np.log(spectrogram))
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [sec]')
    plt.show()
