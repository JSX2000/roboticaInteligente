import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
from playsound import playsound


def audio_filter():
    playsound("audios/Keepers.mp3")

    sampFreq, sound = wavfile.read("audios/Keepers.mp3")
    print(sound.dtype, sampFreq)

    sound = sound / 2.0**15
    sound = sound[:, 0]

    length_in_s = sound.shape[0] / sampFreq
    print("Audio length", length_in_s)

    plt.plot(sound[:], "r")
    plt.xlabel("Sound signal")
    plt.tight_layout()
    plt.show()

    time = np.arange(sound.shape[0]) / sound.shape[0] * length_in_s
    plt.plot(time, sound[:], "r")
    plt.xlabel("time, signal")
    plt.tight_layout()
    plt.show()

    yerr = (
        0.005 * np.sin(2 * np.pi * 6000.0 * time)
        + 0.008 * np.sin(2 * np.pi * 8000.0 * time)
        + 0.006 * np.sin(2 * np.pi * 2500.0 * time)
    )
    signal = sound + yerr
    plt.plot(time[6000:7000], signal[6000:7000])
    plt.xlabel("time, s")
    plt.show()

    fft_spectrum = np.fft.rfft(signal)
