# Digital Signal Processing in python
This repository contains scripts that can do digital signal processing.

## Fast Fourier Transform
Numpy's FFT has been wrapped in a simple script so that the technique can be used easily. The scripts require input data and show a figure with the amplitude spectrum.

#### dspfft
The `dspfft` file is a **module** that performs FFT on an array data (named *y*) with a corresponding sampling rate *Fs*.

*Using the module:*

```python
import dspfft
y = ...  # your data
Fs = ... # sampling rate
dspfft.fft(y,Fs,filename='somename.png',xmin=10,xmax=400)
```

**Note:** the arguments `y` and `Fs` are required, the rest is optional (default values: `filename='fftout.png'`, `xmin=0` and `xmax=10000`)


#### fftwav
The `fftwav` script reads `.wav` files and generates an amplitude spectrum for the entire audio file.

*Running the script:*

The script can run in different modes:
* Automatic xlim: `python fftwav.py audio_file.wav`
* Fixed lower limit (xmin = 0), choose upper limit: `python fftwav.py audio_file.wav xmax`
* Choose both limits: `python fftwav.py audio_file.wav xmin xmax`
