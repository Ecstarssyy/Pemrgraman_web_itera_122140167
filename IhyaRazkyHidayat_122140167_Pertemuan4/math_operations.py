# Modul Math Operations

# Konstanta
PI = 3.14159
KELVIN_CONSTANT = 273.15

# Fungsi untuk menghitung luas dan keliling bentuk geometri
def luas_persegi(sisi):
    """Menghitung luas persegi"""
    return sisi * sisi

def keliling_persegi(sisi):
    """Menghitung keliling persegi"""
    return 4 * sisi

def luas_persegi_panjang(panjang, lebar):
    """Menghitung luas persegi panjang"""
    return panjang * lebar

def keliling_persegi_panjang(panjang, lebar):
    """Menghitung keliling persegi panjang"""
    return 2 * (panjang + lebar)

def luas_lingkaran(jari_jari):
    """Menghitung luas lingkaran"""
    return PI * jari_jari * jari_jari

def keliling_lingkaran(jari_jari):
    """Menghitung keliling lingkaran"""
    return 2 * PI * jari_jari

# Fungsi untuk konversi suhu
def celsius_ke_fahrenheit(celsius):
    """Konversi suhu dari Celsius ke Fahrenheit"""
    return (celsius * 9/5) + 32

def celsius_ke_kelvin(celsius):
    """Konversi suhu dari Celsius ke Kelvin"""
    return celsius + KELVIN_CONSTANT

def fahrenheit_ke_celsius(fahrenheit):
    """Konversi suhu dari Fahrenheit ke Celsius"""
    return (fahrenheit - 32) * 5/9