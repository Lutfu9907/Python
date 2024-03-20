import numpy as np
from matplotlib import pyplot as plt, mlab

prng = np.random.RandomState(42)
fs = 1000
t = np.linspace(0, 0.3, 301)
A = np.array([2, 15]).reshape(-1, 1)
f = np.array([150, 100]).reshape(-1, 1)
xn = (A * np.exp(2j * np.pi * f * t)).sum(axis=0) + 10 * prng.randn(*t.shape)

fig, (ax0, ax1) = plt.subplots(ncols=2, layout='constrained')

yticks = np.arange(-50, 30, 10)
yrange = (yticks[0], yticks[-1])
xticks = np.arange(0, 550, 50)
xrange = (xticks[0], xticks[-1])

ax0.psd(xn, NFFT=301, Fs=fs, window=mlab.window_none, pad_to=1024,
        scale_by_freq=True)
ax0.set_title('Periodogram')
ax0.set_yticks(yticks)
ax0.set_xticks(xticks)
ax0.grid(True)
ax0.set_ylim(yrange)
ax0.set_xlim(xrange)

ax1.psd(xn, NFFT=150, Fs=fs, window=mlab.window_none, pad_to=512, noverlap=75,
        scale_by_freq=True)
ax1.set_title('Welch')
ax1.set_xticks(xticks)
ax1.set_yticks(yticks)
ax1.set_ylabel('')
ax1.grid(True)
ax1.set_ylim(yrange)
ax1.set_xlim(xrange)

plt.show()