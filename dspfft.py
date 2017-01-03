import sys
import wave
import numpy as np
import matplotlib.pyplot as plt

def fft(y,Fs,filename='fftout.png',xmin=0,xmax=10000):
    plt.switch_backend('agg')
    # MATLAB's nextpow2
    L = len(y)
    i = 0
    while True:
        i += 1
        len_FFT = 2**i
        if len_FFT > L:
            break

    # Pad the array so that its length is a power of 2 (for increased FFT speed)
    y = np.lib.pad(y, (0,len_FFT-L), 'constant', constant_values=0)

    # Fourier transform
    Fk = np.fft.fft(y)/len_FFT
    f = np.fft.fftfreq(len_FFT,1.0/Fs)  # 1.0 is necessary to force 'float'
    Y = 2*abs(Fk[1:-len_FFT/2+1])
    f = f[1:-len_FFT/2+1]

    # Plot
    fig, ax = plt.subplots()
    ax.plot(f,Y)
    if xmax < xmin:
        print('Error: xmin > xmax.')
        sys.exit()
    ax.set_xlim((xmin, xmax))
    ax.set_xlabel(r'$f (\mathrm{Hz})$',size='x-large')
    ax.set_ylabel(r'$\vert Y(f)\vert$',size='x-large')
    fig.suptitle('Single-sided amplitude spectrum of the input data',size='x-large')
    plt.savefig(filename)
