# NIM/Nama : 16521516/Ahmad Nadil
# Tanggal : 3 November 2021
# Deskripsi : Bertempur

# KAMUS
# hp_Ric_Awal = Integer
# N_Ric = Integer
# act_Ric = Array [0..N_Ric-1] of char
# hp_Kil_Awal = Integer
# N_Kil = Integer
# act_Kil = Array [0..N_Ric-1] of char

# ALGORITMA
champ = ''      # Isi Pemenang sebagai string kosong

#Input Data Tuan Ric
hp_Ric_Awal = int(input('Masukkan nyawa awal Ric : '))          #Input Nyawa Tuan Ric
hp_Ric = hp_Ric_Awal                                            #Set hp_Ric == hp_Ric_Awal ; hp_Ric untuk dilakukan pengurangan setiap aksi
N_Ric = int(input('Banyak aksi Ric : '))                        #Input banyak aksi tuan Ric
act_Ric =[0 for i in range (N_Ric)]                             #Isi act_Ric dengan array berisi angka 0 sebanyak N_Ric
for i in range (N_Ric):                                         #Looping untuk mengisi act_Ric sesuai inputan
    act_Ric[i] = input('Masukkan aksi Ric ke ' + str(i+1) + ' : ')

#Input Data Tuan Kil
hp_Kil_Awal = int(input('Masukkan nyawa awal Kil : '))          #Input Nyawa Tuan Kil
hp_Kil = hp_Kil_Awal                                            #Set hp_Kil == hp_Kil_Awal ; hp_Kil untuk dilakukan pengurangan setiap aksi
N_Kil = int(input('Banyak aksi Kil : '))                        #Input banyak aksi tuan Kil
act_Kil =[0 for i in range (N_Kil)]                             #Isi act_Kil dengan array berisi angka 0 sebanyak N_Kil
for i in range (N_Kil):                                         #Looping untuk mengisi act_Ric sesuai inputan
    act_Kil[i] = input('Masukkan aksi Kil ke ' + str(i+1) + ' : ')

curse = 10      #Set curse sebesar 0
act = 0

while champ == '':
    if act_Ric[act % N_Ric] == 'H':             #Kondisi jika H (Healing)
        hp_Ric += (hp_Ric_Awal - hp_Ric) // 10
    else :                                      #Kondisi menyerang
        hp_Kil -= int(act_Ric[act%N_Ric])
        if hp_Kil <= 0 and champ == '':
            champ = 'Ric'
    
    if act_Kil[act % N_Kil] == 'H':             #Kondisi jika H (Healing)
        hp_Kil += (hp_Kil_Awal - hp_Kil) // 10  
    else :                                      #Kondisi menyerang
        hp_Ric -= int(act_Kil[act % N_Kil])
        if hp_Ric <= 0 and champ == '':
            champ = 'Kil'

    act += 1
    if act >= 4 :   #Kondisi untuk mengurangi darah karena kutukan, akan di apply pada ronde ke 5 dan seterusnya
        hp_Kil -= curse
        hp_Ric -= curse
        curse += 5
        if hp_Ric <= 0 and champ == '':
            champ = 'Kil'
        if hp_Kil <= 0 and champ == '':
            champ = 'Ric'
    print('Ric : ' , hp_Ric , 'Kil : ' , hp_Kil)
#Output Akhir
print('Pemenang Game adalah',champ)