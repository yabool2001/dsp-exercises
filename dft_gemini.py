import numpy as np
import matplotlib.pyplot as plt

# 1. Parametry naszego pomiaru
f_s = 1000       # Częstotliwość próbkowania (1000 Hz)
N = 1000         # Liczba próbek (okno trwa 1 sekundę)
t = np.arange(N) / f_s  # Wektor czasu
f0 = 150         # Częstotliwość naszej fali (150 Hz)

# 2. Generujemy SYGNAŁ RZECZYWISTY (zwykły cosinus oscylujący w 1D)
# x(t) = cos(2*pi*f0*t)
x_real = np.cos(2 * np.pi * f0 * t)

# 3. Generujemy SYGNAŁ ZESPOLONY (fala wykładnicza zespolona I/Q oscylująca w 2D)
# Zgodnie z tożsamością Eulera: e^(j*2*pi*f0*t) = cos(...) + j*sin(...)
x_complex = np.exp(1j * 2 * np.pi * f0 * t)


# ---------------------------------------------------------
# OBLICZANIE WIDMA DFT
# ---------------------------------------------------------
# Obliczamy surowe DFT dla obu sygnałów
X_real = np.fft.fft(x_real)
X_complex = np.fft.fft(x_complex)

# Tworzymy oś częstotliwości (np.fft.fftfreq) i sortujemy ją (np.fft.fftshift),
# aby ujemne i dodatnie częstotliwości ustawiły się po lewej/prawej stronie zera.
freqs = np.fft.fftshift(np.fft.fftfreq(N, d=1/f_s))
X_real_shifted = np.fft.fftshift(X_real)
X_complex_shifted = np.fft.fftshift(X_complex)


# ---------------------------------------------------------
# RYSOWANIE WYNIKÓW
# ---------------------------------------------------------
plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.title("Widmo DFT dla SYGNAŁU RZECZYWISTEGO (cosinus)")
# Wydobywamy amplitudę z zespolonego wyniku (abs) i normujemy /N
plt.plot(freqs, np.abs(X_real_shifted) / N, color='blue')
plt.ylabel("Amplituda")
plt.grid(True)

plt.subplot(2, 1, 2)
plt.title("Widmo DFT dla SYGNAŁU ZESPOLONEGO (e^jωt)")
plt.plot(freqs, np.abs(X_complex_shifted) / N, color='red')
plt.xlabel("Częstotliwość [Hz]")
plt.ylabel("Amplituda")
plt.grid(True)

plt.tight_layout()
plt.show()