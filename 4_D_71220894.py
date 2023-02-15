from gettext import npgettext


print("!! Selamat Datang Di H+ GYM !!")
print("Silahkan Pilih menu Dibawah ini:")
print("1. Menambahkan Data\n2. Menampilkan Data\n3. Keluar ")
inpt = int(input("Silahkan masukan pilian yang Anda inginkan: "))
if inpt == 1:
    listnp = []
    i = 0
    while True: 
        np  = raw_input("Masukan Nama Pelanggan :".format())
        listnp.append(raw_input)
        i += 1

        jm = input("Masukan jenis Member: ").title().lower()
        print("Data sudah berhasil ditambahkan!")
    
elif inpt == 2:
    
else:
    print('Sistem Berhenti....')
