print('Program Menghitung berbelanja')
print('-----------------')
print('Pilih Opsi')
print('==========> 1.Filosofi Teras')
print('            2.Psychology of Money')
print('            3.No More Burnout')
print("\n")

Pilihan =  int(input("Masukkan Pilihan : "))
print("\n")
#uang_Rp_80_000
#uang_Rp_100_000
#uang_Rp_500_000

match Pilihan:
    case Pilihan if Pilihan == 1: opsi1 = 'Filosofi Teras'
    case Pilihan if Pilihan == 2: opsi1 = 'Psikologi uang'
    case Pilihan if Pilihan == 3: opsi1 = 'No More Burnout'

    case _: print('Tidak ada menu')

if opsi1 == 'Filosofi Teras':
    print('Harga buku', opsi1,'Rp.80.000')
elif opsi1 == 'Psikologi uang':
    print('Harga buku', opsi1,'Rp.100.000')
elif opsi1 == 'No More Burnout':
    print('Harga buku', opsi1,'Rp.150.000')
else:
    print('Mohon Maaf uang anda tidak cukup.',end='pulang ke rumah')
