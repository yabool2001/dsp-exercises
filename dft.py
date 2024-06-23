import numpy as np
import matplotlib.pyplot as plt

def dft ( x_t , f_s , N , threshold = 1e-10 ) :
    # Historia utworzenia funkcji https://chatgpt.com/share/e7a46f16-564f-4490-b71f-466276daa8bb
    # x_t: próbki sygnału w dziedzinie czasu
    # N: liczba próbek w sygnale
    half_N = N // 2 + 1  # Liczba elementów do analizy dla obu przypadków
    # X_m_mag = np.zeros ( half_N )  # Amplitudy w dziedzinie częstotliwości
    # X_m_phi = np.zeros ( half_N )  # Fazy w dziedzinie częstotliwości
    result = np.zeros ( ( half_N , 3 ) )  # Kolumny: częstotliwość, amplituda, faza

    for m in range ( half_N ) :
        X_m_freq = m * f_s / N
        X_m = 0j  # Inicjalizacja składowej częstotliwości jako liczby zespolonej
        for n in range ( N ) :
            X_m += x_t[n] * np.exp ( -2j * np.pi * m * n / N )
        # Ustawienie zerowej amplitudy i fazy dla małych wartości
        X_m /= N  # Skalowanie przez liczbę próbek
        if np.abs ( X_m ) < threshold:
            X_m_mag = 0
            X_m_phi = 0  # Faza zerowa dla bardzo małych wartości amplitudy
        else:
            if m == 0 or m == N//2:  # Nie podwajamy dla składnika DC i Nyquista
                X_m_mag = np.abs(X_m)
            else:
                X_m_mag = 2 * np.abs(X_m)  # Podwajanie amplitudy dla odpowiedzi częstotliwości
            X_m_phi = np.angle ( X_m , deg = True )  # Obliczanie fazy
        result [m] = [ X_m_freq , X_m_mag , X_m_phi ]

    return result

# Parametry próbkowania
f_s = 8000  # Częstotliwość próbkowania
N = 8       # Liczba próbek
t_s = 1.0 / f_s  # Okres próbkowania

# Wyznaczenie punktów próbkowania t_n
t_n = np.arange ( 0 , N * t_s , t_s )

# Definicje częstotliwości sygnału
freq1 = 1000.0
freq2 = 2000.0

# Obliczenie sygnału x(t) w dyskretnych punktach t_n
x_t = np.sin(2 * np.pi * freq1 * t_n) + 0.5 * np.sin(2 * np.pi * freq2 * t_n + ((3/4) * np.pi) )

# Obliczenie DFT
X_m = dft ( x_t , 8000 , N )

# Wyświetlenie wyników
print ( f"{X_m=}")

plt.figure ( figsize = ( 10 , 5 ) )
plt.subplot ( 211 )
plt.stem ( X_m[:, 0] , X_m[:, 1] , 'b' ,  markerfmt = " " , basefmt = "-b" )
plt.ylabel ( 'Magnitude of X(m) |X(freq)|' )

plt.subplot ( 212 )
plt.stem ( X_m[:, 0] , X_m[:, 2] , 'b', markerfmt = " ", basefmt = "-b" )
plt.xlabel ( 'Freq (Hz)' )
plt.ylabel ( 'Phase Angle of X(m) Xphi(freq)' )
plt.show ()