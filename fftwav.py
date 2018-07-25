import sys
import wave
import numpy as np
import matplotlib.pyplot as plt

# Check number of arguments
if len(sys.argv) < 2:
    print('Auto x-axis limits:')
    print('   Usage: python fftwav.py audio_file.wav')
    print('Fixed upper limit for x-axis (lower = 0):')
    print('   Usage: python fftwav.py audio_file upper_lim')
    print('Fixed limits for x-axis:')
    print('   Usage: python fftwav.py audio_file lower_lim upper_lim')

    sys.exit()

# Load .wav file
input_file = sys.argv[1]
wav_obj = wave.open(input_file, 'r')
Fs = wav_obj.getframerate()
wav_data = np.fromstring(wav_obj.readframes(Fs), dtype=np.int16)
nChannels = wav_obj.getnchannels()
wav_obj.close()
if nChannels == 2:
    left, right = wav_data[0::2], wav_data[1::2]  # Stereo file
else:
    left = wav_data;                              # Mono file

# MATLAB's nextpow2
L = len(left)
i = 0
while True:
    i += 1
    len_FFT = 2**i
    if len_FFT > L:
        break

# Pad the array so that its length is a power of 2 (for increased FFT speed)
left = np.lib.pad(left, (0,len_FFT-L), 'constant', constant_values=0)

# Fourier transform
Fk = np.fft.fft(left)/len_FFT
f = np.fft.fftfreq(len_FFT,1.0/Fs)  # 1.0 is necessary to force 'float'
Y = 2*abs(Fk[1:round(-len_FFT/2+1)]) # Round is necessary to force 'int'
f = f[1:round(-len_FFT/2+1)]

# Plot
fig, ax = plt.subplots()
ax.plot(f,Y)
if len(sys.argv) == 3:
    ax.set_xlim((0, int(sys.argv[2])))
if len(sys.argv) == 4:
    if int(sys.argv[3]) < int(sys.argv[2]):
        print('Error: the chosen xmin > xmax.')
        sys.exit()
    ax.set_xlim((int(sys.argv[2]), int(sys.argv[3])))
ax.set_xlabel(r'$f (\mathrm{Hz})$',size='x-large')
ax.set_ylabel(r'$\vert Y(f)\vert$',size='x-large')
fig.suptitle('Single-sided amplitude spectrum of file:\n$' + input_file + '$',size='x-large')
plt.show()
