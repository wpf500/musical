#!/usr/bin/env python
import numpy as np
from scikits import audiolab

f = audiolab.Sndfile('test.wav', 'r')
frames = f.read_frames(f.nframes)

N = 64
spectrum = np.fft.fft(frames, N)
freqs = [(np.abs(x), np.angle(x)) for x in spectrum]

print 'unset key'
print 'set xrange [0:2*pi]'

print 'plot',
for (amp, phase) in freqs:
    print '%f * sin(x + %f), ' % (amp, phase),

print '"-" with lines'
print

for theta in np.linspace(0, 2 * np.pi, f.nframes / 50):
    signal = 0
    for (amp, phase) in freqs:
        signal += amp * np.sin(theta + phase)

    print theta, signal
