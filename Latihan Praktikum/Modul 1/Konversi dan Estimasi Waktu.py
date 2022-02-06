jam = int(input("Masukkan jam kepergian: "))
menit = int(input("Masukkan menit kepergian: "))
lama = int(input("Masukkan lama penerbangan (menit): "))
perbedaan = int(input("Masukkan perbedaan waktu (menit): "))

menit_sampai = jam * 60 + menit + lama + perbedaan
jam_sampai = menit_sampai // 60
menit_sampai = menit_sampai % 60

if menit_sampai < 10:
    menit_sampai = "0" + str(menit_sampai)
if jam_sampai < 10:
    jam_sampai = "0" + str(jam_sampai)

print('Waktu kedatangan Tuan Kil di Negara Peng adalah', jam_sampai, menit_sampai)
