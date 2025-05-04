# Program Penghitung BMI (Body Mass Index)

# Input data berat dan tinggi
berat = float(input("Masukkan berat badan (kg): "))
tinggi = float(input("Masukkan tinggi badan (m): "))

# Menghitung BMI
bmi = berat / (tinggi * tinggi)

# Menentukan kategori BMI
if bmi < 18.5:
    kategori = "Berat badan kurang"
elif bmi < 25:
    kategori = "Berat badan normal"
elif bmi < 30:
    kategori = "Berat badan berlebih"
else:
    kategori = "Obesitas"

# Menampilkan hasil
print("\nHasil Perhitungan BMI:")
print(f"BMI Anda adalah: {bmi:.2f}")
print(f"Kategori BMI: {kategori}")