import numpy as np
import matplotlib.pyplot as plt

fc = 1000
Amplitude = 1
fm = 100
Amplitude_mod = 0.5

t = np.linspace(0, 1, 1000)
carrier_signal = Amplitude * np.sin(2 * np.pi * fc * t)
message_signal = Amplitude_mod * np.sin(2 * np.pi * fm * t)
modulated_signal = (1 + Amplitude_mod * message_signal) * carrier_signal

plt.figure(figsize=(10, 6))

plt.subplot(3, 1, 1)
plt.plot(t, carrier_signal, 'b')
plt.title('Carrier Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.subplot(3, 1, 2)
plt.plot(t, message_signal, 'r')
plt.title('Message Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.subplot(3, 1, 3)
plt.plot(t, modulated_signal, 'g')
plt.title('AM Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()
