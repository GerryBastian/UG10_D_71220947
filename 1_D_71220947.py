

print(" Ketik 1 Untuk menghitung penjumlahan.")
print(" Ketik 2 Untuk menghitung pengurangan.")
print("Ketik 3 Untuk menghitung perkalian.")
print("Ketik 4 Untuk menghitung pembagian.")
print("Ketik 5 Untuk menghitung Sisa hasil bagi (modulus).")
print("Ketik 6 Untuk menghitung pemangkatan.")

pemilihan= int(input("Masukkan Pilihan Anda :"))
bilpertama= int(input("Masukkan bilangan pertama:"))
bilkedua = int(input("Masukkan bilangan kedua:"))

if pemilihan == 1:
    jumlah = bilpertama + bilkedua
    print("hasil dari", bilpertama, "dijumlahkan dengan", bilkedua, "adalah", jumlah)
    
elif pemilihan == 2:
    kurang = bilpertama - bilkedua
    print("hasil dari", bilpertama, "dikurangi dengan", bilkedua, "adalah", kurang)
elif pemilihan == 3:
    kali = bilpertama * bilkedua
    print("hasil dari", bilpertama, "dikali dengan", bilkedua, "adalah", kali)
elif pemilihan == 4:
    bagi = bilpertama / bilkedua
    print("hasil dari", bilpertama, "dibagi dengan", bilkedua, "adalah", bagi)
elif pemilihan == 5:
    sisabagi = bilpertama % bilkedua
    print("hasil dari", bilpertama, "dibagi dengan", bilkedua, "adalah", sisabagi)
elif pemilihan == 6:
    pemangkatan = bilpertama ** bilkedua
    print("hasil dari", bilpertama, "dipangkatkan dengan", bilkedua, "adalah", pemangkatan)
  
  
  
