in1=input("Masukan nama pemain pertama:")
in2=input("Masukan nama pemain Kedua:")
in3=input("Masukan nama pemain Ketiga:")
j1=int(input("masukan jumlah kartu pertama:"))
j2=int(input("masukan jumlah kartu kedua:"))
j3=int(input("masukan jumlah kartu ketiga:"))

if (j1> j2 and j3):
    print(in1, "menang dengan jumlah kartu", j1)
elif (j1>21):
    print("kartu melebihi batas")
elif (j2>21):
    print("kartu melebihi batas")
elif (j3>21):
    print("kartu melebihi batas")
elif (j2> j3 and j1):
    print(in2, "menang dengan jumlah kartu", j2)
elif (j3> j1 and j2):
    print(in3, "menang dengan jumlah kartu", j3)
