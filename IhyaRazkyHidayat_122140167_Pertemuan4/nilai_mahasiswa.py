# Program Pengelolaan Data Nilai Mahasiswa

# Membuat list berisi dictionary data mahasiswa
data_mahasiswa = [
    {
        "nama": "Ahmad Fajar",
        "nim": "12345",
        "nilai_uts": 85,
        "nilai_uas": 90,
        "nilai_tugas": 88
    },
    {
        "nama": "Budi Santoso",
        "nim": "12346",
        "nilai_uts": 70,
        "nilai_uas": 65,
        "nilai_tugas": 80
    },
    {
        "nama": "Citra Dewi",
        "nim": "12347",
        "nilai_uts": 60,
        "nilai_uas": 55,
        "nilai_tugas": 70
    },
    {
        "nama": "Dian Permata",
        "nim": "12348",
        "nilai_uts": 90,
        "nilai_uas": 95,
        "nilai_tugas": 92
    },
    {
        "nama": "Eko Prasetyo",
        "nim": "12349",
        "nilai_uts": 45,
        "nilai_uas": 50,
        "nilai_tugas": 60
    }
]

# Menghitung nilai akhir dan menentukan grade untuk setiap mahasiswa
for mahasiswa in data_mahasiswa:
    # Menghitung nilai akhir (30% UTS + 40% UAS + 30% Tugas)
    nilai_akhir = (0.3 * mahasiswa["nilai_uts"]) + (0.4 * mahasiswa["nilai_uas"]) + (0.3 * mahasiswa["nilai_tugas"])
    mahasiswa["nilai_akhir"] = nilai_akhir
    
    # Menentukan grade berdasarkan nilai akhir
    if nilai_akhir >= 80:
        mahasiswa["grade"] = "A"
    elif nilai_akhir >= 70:
        mahasiswa["grade"] = "B"
    elif nilai_akhir >= 60:
        mahasiswa["grade"] = "C"
    elif nilai_akhir >= 50:
        mahasiswa["grade"] = "D"
    else:
        mahasiswa["grade"] = "E"

# Mencari mahasiswa dengan nilai tertinggi dan terendah
nilai_tertinggi = max(data_mahasiswa, key=lambda x: x["nilai_akhir"])
nilai_terendah = min(data_mahasiswa, key=lambda x: x["nilai_akhir"])

# Menampilkan data mahasiswa dalam format tabel
print("=" * 80)
print("{:<20} {:<10} {:<10} {:<10} {:<10} {:<15} {:<5}".format(
    "Nama", "NIM", "UTS", "UAS", "Tugas", "Nilai Akhir", "Grade"))
print("-" * 80)

for mahasiswa in data_mahasiswa:
    print("{:<20} {:<10} {:<10} {:<10} {:<10} {:<15.2f} {:<5}".format(
        mahasiswa["nama"],
        mahasiswa["nim"],
        mahasiswa["nilai_uts"],
        mahasiswa["nilai_uas"],
        mahasiswa["nilai_tugas"],
        mahasiswa["nilai_akhir"],
        mahasiswa["grade"]
    ))

print("=" * 80)

# Menampilkan mahasiswa dengan nilai tertinggi dan terendah
print("\nMahasiswa dengan nilai tertinggi:")
print(f"Nama: {nilai_tertinggi['nama']}")
print(f"NIM: {nilai_tertinggi['nim']}")
print(f"Nilai Akhir: {nilai_tertinggi['nilai_akhir']:.2f}")
print(f"Grade: {nilai_tertinggi['grade']}")

print("\nMahasiswa dengan nilai terendah:")
print(f"Nama: {nilai_terendah['nama']}")
print(f"NIM: {nilai_terendah['nim']}")
print(f"Nilai Akhir: {nilai_terendah['nilai_akhir']:.2f}")
print(f"Grade: {nilai_terendah['grade']}")