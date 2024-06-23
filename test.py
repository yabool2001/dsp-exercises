import numpy as np

def calculate_dft( x_t , N , threshold = 1e-10 ):
    # x_t: próbki sygnału w dziedzinie czasu
    # N: liczba próbek w sygnale
    X_m_mag = np.zeros ( N )  # Amplitudy w dziedzinie częstotliwości
    X_m_phi = np.zeros ( N )  # Fazy w dziedzinie częstotliwości

    for m in range ( N ) :
        X_m = 0j  # Inicjalizacja składowej częstotliwości jako liczby zespolonej
        for n in range ( N ) :
            X_m += x_t[n] * np.exp ( -2j * np.pi * m * n / N )
        # Ustawienie zerowej amplitudy i fazy dla małych wartości
        if np.abs ( X_m ) < threshold:
            X_m_mag[m] = 0
            X_m_phi[m] = 0  # Faza zerowa dla bardzo małych wartości amplitudy
        else:
            X_m_mag[m] = np.abs ( X_m )  # Obliczanie amplitudy
            X_m_phi[m] = np.angle ( X_m , deg = True )  # Obliczanie fazy

    return X_m_mag , X_m_phi

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
X_m_mag, X_m_phi = calculate_dft(x_t, N)

# Wyświetlenie wyników
print("Magnitudes:", X_m_mag)
print("Phases:", X_m_phi)
