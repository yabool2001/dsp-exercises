# Zaczerpnięte z podręcznika z rozdz. "15 Pulse Shaping" podręcznika:
# "PySDR: A Guide to SDR and DSP using Python"

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

num_symbols = 10
sps = 8
bits = np.random.randint ( 0 , 2 , num_symbols ) # Our data to be transmitted, 1

x = np.array ( [] )
for bit in bits :
    pulse = np.zeros ( sps )
    pulse[0] = bit * 2 - 1 # set the first value to either a 1 or -1
    x = np.concatenate ( ( x , pulse ) ) # add the 8 samples to the signal
plt.figure ( 0 )
plt.plot ( x , '.-' )
plt.grid ( True )
plt.show ()

# bits:[0,1,1,1,1,0,0,0,1,1]
# BPSK symbols:[-1,1,1,1,1,-1,-1,-1,1,1]
# Nie jestem pewny czy to dobrze jest, bo sam robiłem z przyciętego PDF domyślając się : Applying 8 samples per symbol : [-1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,-1,0,0,0,0,0,0,0,-1,0,0,0,0,0,0,0,-1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0]

# Create our raised-cosine filter
num_taps = 101
beta = 0.35
Ts = sps # Assume sample rate is 1 Hz, so sample period is 1, so *symbol* period is 8
t = np.arange ( num_taps ) - ( num_taps - 1 ) // 2
h = np.sinc ( t / Ts ) * np.cos ( np.pi * beta * t / Ts ) / ( 1 - ( 2 * beta * t / Ts ) ** 2 )
plt.figure ( 1 )
plt.plot ( t , h , '.' )
plt.grid ( True )
plt.show ()

# Filter our signal, in order to apply the pulse shaping
x_shaped = np.convolve ( x , h )
plt.figure ( 2 )
plt.plot ( x_shaped , '.-' )
for i in range ( num_symbols ) :
    plt.plot ( [ i * sps + num_taps // 2 , i * sps + num_taps // 2 ] , [ 0 , x_shaped[ i * sps + num_taps // 2 ] ] )
plt.grid ( True )
plt.show ()