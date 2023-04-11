# from filters import fir_filter, iir_filter, fourier_trnasform
from filters import fir_filter, fourier_transform
from scipy.signal import freqz
from numpy import cos, sin, pi, absolute, arange
import numpy as np
from matplotlib import pyplot as plt

if __name__ == "__main__":
    # create signal
    np.random.seed(42)
    fs = 80
    ts = np.arange(0, 5, 1.0 / fs)
    x_t = np.sin(2*np.pi * 1 * ts)
    noise = 0.2 * sin(2 * pi * 15.3 * ts) + 0.1 * sin(2 * pi *
                                                      16.7 * ts + 0.1) + 0.1 * sin(2 * pi * 23.45 * ts + 0.8)
    x_noise = x_t + noise
    plt.figure(figsize=[6.4, 2.4])
    plt.plot(ts, x_t, alpha=0.8, lw=3, color="C1", label="Clean signal (ys)")
    plt.plot(ts, x_noise, color="C0", label="Noisy signal (x_noise)")
    plt.xlabel("Time / s")
    plt.ylabel("Amplitude")
    plt.legend(loc="lower center", bbox_to_anchor=[
               0.5, 1], ncol=2, fontsize="smaller")
    plt.tight_layout()
    plt.show()

    xf, yf = fourier_transform(x_noise, sample_rate=fs, duration=5)
    plt.plot(xf, np.abs(yf))
    plt.show()
    fc = 10
    x_filtered = iir_filter(x_noise, fc, fs)
    xf, yf = fourier_transform(x_filtered, sample_rate=fs, duration=5)
    plt.plot(xf, np.abs(yf))
    plt.show()
    plt.figure(figsize=[6.4, 2.4])
    plt.plot(ts, x_noise, label="Raw signal")
    plt.plot(ts, x_filtered, alpha=0.8, lw=3, label="SciPy lfilter")
    plt.xlabel("Time  / s")
    plt.ylabel("Amplitude")
    plt.legend(loc="lower center", bbox_to_anchor=[
        0.5, 1], ncol=2, fontsize="smaller")
    plt.tight_layout()
    plt.show()
