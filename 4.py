import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import rfft, irfft, rfftfreq

time = 15
delta = 0.1
array = np.arange(-time, time, delta)
a = 28
b = 47
c = 14
input_signal = [a * math.sin(math.pi * i) + b * math.sin(math.pi * 2 * i) + c * math.sin(math.pi * 3 * i) for i in array]
plt.plot(array, input_signal, color='yellow')
plt.title('Input signal')
plt.xlabel('Frequency, Hz')
plt.ylabel('Amplitude, М')
plt.grid(True)
plt.show()
noise = np.random.uniform(-30, 30, np.size(array))
plt.plot(array, input_signal + noise, color='purple')
plt.title('Noisy signal')
plt.xlabel('Frequency, Hz')
plt.ylabel('Amplitude, М')
plt.grid(True)
plt.show()
spectrum = rfft(input_signal + noise)
plt.plot(rfftfreq(len(array)), abs(spectrum), )
plt.title('Noisy signal spectrum')
plt.xlabel('Frequency, Hz')
plt.ylabel('Amplitude, М')
plt.grid(True)
plt.show()
true_spectrum = []
for i in range(0, len(spectrum)):
    if abs(spectrum[i]) > np.max(abs(spectrum)) / 5:
        true_spectrum.append(spectrum[i])
    else:
        true_spectrum.append(0)
plt.plot(rfftfreq(len(array)), np.abs(true_spectrum))
plt.title('Non-noisy signal spectrum')
plt.xlabel('Frequency, Hz')
plt.ylabel('Amplitude, М')
plt.grid(True)
plt.show()
output = irfft(true_spectrum)
plt.plot(array, output, color='pink')
plt.title('Non-noisy output signal')
plt.xlabel('Frequency, Hz')
plt.ylabel('Amplitude, М')
plt.grid(True)
plt.show()
plt.plot(array, input_signal, color='yellow', label='Input signal')
plt.plot(array, input_signal + noise, color='purple', label='Noisy signal')
plt.plot(array, output, color='pink', label='Output signal')
plt.legend()
plt.grid(True)
plt.show()
