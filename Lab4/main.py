# imports
from scipy.io import wavfile
from scipy import signal
import numpy as np

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

spectrogram('guitar.wav')