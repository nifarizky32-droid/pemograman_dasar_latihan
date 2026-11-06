 IF Tunggal (IF)
Pengertian: IF tunggal digunakan untuk menjalankan perintah jika suatu kondisi bernilai benar (True).

Contoh soal:

Buatlah program untuk mengecek apakah seseorang sudah cukup umur untuk membuat KTP. Jika umur 17 tahun atau lebih, tampilkan "Anda sudah boleh membuat KTP".

umur = int(input("Masukkan umur: "))

if umur >= 17:
    print("Anda sudah boleh membuat KTP")
    
    
IF-ELIF-ELSE
Pengertian: Digunakan untuk memilih satu dari beberapa kondisi.

Contoh soal:

Buatlah program untuk menentukan nilai huruf berdasarkan nilai angka:

Nilai 90–100 = A

Nilai 80–89 = B

Nilai 70–79 = C

Nilai di bawah 70 = D
nilai = int(input("Masukkan nilai: "))

if nilai >= 90:
    print("Nilai A")
elif nilai >= 80:
    print("Nilai B")
elif nilai >= 70:
    print("Nilai C")
else:
    print("Nilai D")
    
IF Bercabang (Nested IF)
Pengertian: IF bercabang adalah IF yang berada di dalam IF lainnya.

Contoh soal:

Buatlah program untuk menentukan apakah seseorang boleh mengikuti ujian.

Jika nilai tugas minimal 75, lanjutkan pemeriksaan.

Jika kehadiran minimal 80%, maka boleh mengikuti ujian.

Jika kehadiran kurang dari 80%, tidak boleh mengikuti ujian.

Jika nilai tugas kurang dari 75, tidak boleh mengikuti ujian.

nilai = int(input("Masukkan nilai tugas: "))

if nilai >= 75:
    kehadiran = int(input("Masukkan kehadiran (%): "))

    if kehadiran >= 80:
        print("Boleh mengikuti ujian")
    else:
        print("Tidak boleh mengikuti ujian")
else:
    print("Tidak boleh mengikuti ujian")