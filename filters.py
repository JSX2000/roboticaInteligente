from scipy.signal import kaiserord, lfilter, firwin, freqz, iirfilter, filtfilt
from scipy.fft import fft, fftfreq
from scipy.fftpack import fftshift

#Transformada de Fourier
def fourier_transform(signal, sample_rate=44100, duration=5):
    # Number of samples
    N = sample_rate * duration
    yf = fft(signal)
    xf = fftfreq(N, 1 / sample_rate)
    # Ordered FFT
    yf = fftshift(yf) # type: ignore
    xf = fftshift(xf)
    return xf, yf

def iir_filter(signal, f_cutoff, f_sampling, fbf=False):
    b, a = iirfilter(4, Wn=f_cutoff, fs=f_sampling, btype="low", ftype="butter")
    if not fbf:
        filtered = lfilter(b, a, signal)
    else:
        filtered = filtfilt(b, a, signal)
    return filtered


def fir_filter(signal, nyq_rate, f_cutoff):
    # Window width
    width = 5.0 / nyq_rate
    # The described attenuation in the stop band, in dB
    ripple_db = 60.0

    N, beta = kaiserord(ripple_db, width)
    taps = firwin(N, f_cutoff / nyq_rate, window=("kaiser", beta)) # type: ignore
    filtered_x = lfilter(taps, 1.0, signal)

    return filtered_x, taps, N
