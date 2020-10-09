
matakuliah = input("Masukan Nama Matakuliah: ")
pertemuan = input("masukan max.pertemuan: ")
hadir = input("masukan jumlah hadir: ")
totalabsen = int(hadir) * 100 / int(pertemuan) 
print  ("Nilai absen yang didapat dari perhitungan diatas adalah: "'{:.1f}'.format(totalabsen))



