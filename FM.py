import numpy as np
import matplotlib.pyplot as plt

fc = 100
kf = 50

fm = 10
Amplitude = 1
t = np.linspace(0, 1, 1000)

mesaj_sinyali = Amplitude * np.sin(2 * np.pi * fm * t)
module_edilmis_sinyal = np.cos(2 * np.pi * (fc + kf * mesaj_sinyali) * t)

plt.figure(figsize=(10, 6))

plt.subplot(3, 1, 1)
plt.plot(t, mesaj_sinyali, 'b')
plt.title('Mesaj Sinyali')
plt.xlabel('Zaman')
plt.ylabel('Genlik')

plt.subplot(3, 1, 2)
plt.plot(t, fc + kf * mesaj_sinyali, 'r')
plt.title('Modulasyon Sinyali')
plt.xlabel('Zaman')
plt.ylabel('Frekans')

plt.subplot(3, 1, 3)
plt.plot(t, module_edilmis_sinyal, 'g')
plt.title('FM Sinyali')
plt.xlabel('Zaman')
plt.ylabel('Genlik')

plt.tight_layout()
plt.show()
