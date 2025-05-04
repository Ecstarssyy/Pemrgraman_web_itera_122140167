# Program Utama yang Menggunakan Modul math_operations

# Cara 1: Mengimpor seluruh modul
import math_operations

# Cara 2: Mengimpor fungsi-fungsi tertentu dari modul
from math_operations import celsius_ke_fahrenheit, celsius_ke_kelvin

print("=" * 50)
print("PROGRAM DEMONSTRASI MODUL MATH_OPERATIONS")
print("=" * 50)

# Menggunakan konstanta PI
print(f"\nNilai PI dalam modul: {math_operations.PI}")

# Demo fungsi perhitungan luas dan keliling bentuk geometri
print("\n1. PERHITUNGAN BENTUK GEOMETRI")
print("-" * 40)

# Persegi
sisi_persegi = 5
print(f"Persegi dengan sisi {sisi_persegi} cm:")
print(f"   Luas: {math_operations.luas_persegi(sisi_persegi):.2f} cm²")
print(f"   Keliling: {math_operations.keliling_persegi(sisi_persegi):.2f} cm")

# Persegi Panjang
panjang = 10
lebar = 5
print(f"\nPersegi Panjang dengan panjang {panjang} cm dan lebar {lebar} cm:")
print(f"   Luas: {math_operations.luas_persegi_panjang(panjang, lebar):.2f} cm²")
print(f"   Keliling: {math_operations.keliling_persegi_panjang(panjang, lebar):.2f} cm")

# Lingkaran
jari_jari = 7
print(f"\nLingkaran dengan jari-jari {jari_jari} cm:")
print(f"   Luas: {math_operations.luas_lingkaran(jari_jari):.2f} cm²")
print(f"   Keliling: {math_operations.keliling_lingkaran(jari_jari):.2f} cm")

# Demo fungsi konversi suhu (menggunakan import langsung)
print("\n2. KONVERSI SUHU")
print("-" * 40)

# Contoh suhu dalam Celsius
suhu_celsius = 25
print(f"Suhu {suhu_celsius}°C sama dengan:")
# Menggunakan fungsi yang diimpor langsung
print(f"   {celsius_ke_fahrenheit(suhu_celsius):.2f}°F (menggunakan import fungsi)")
print(f"   {celsius_ke_kelvin(suhu_celsius):.2f}K (menggunakan import fungsi)")

# Menggunakan fungsi melalui modul
print(f"   {math_operations.fahrenheit_ke_celsius(98.6):.2f}°C (dari 98.6°F menggunakan modul)")

print("\n" + "=" * 50)