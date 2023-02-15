Telur_bakar = 7000
Lele_terbang = 10000
Es_coklat = 5000
EDoger = 13000

print('============= MAKANAN =============')
print("1. Telur Bakar : Rp 7.000\n2. Lele Terbang Mas Bhe : Rp. 10.000\n3.Es Coklat Lempu : Rp. 5.000\n4. Es Doger : Rp 13.000")
print('============= PESANAN =============')
Tb = int(input('Telur Bakar    : '))
Lt = int(input('Lele Terbang   : '))
Ec = int(input('Es Cokelat     : '))
Ed = int(input('Es Doger       : '))
V = Telur_bakar*Tb
X = Lele_terbang*Lt
Y = Es_coklat*Ec
Z = EDoger*Ed
print('============= TOTAL =============')
print('TOTAL TELUR BAKAR  ',Tb,'      : Rp. ',V)
print('TOTAL LELE TERBANG ',Lt,'     : Rp. ',X)
print('TOTAL ES COKELAT   ',Ec,'       : Rp. ',Y)
print('TOTAL ES DOGER     ',Ed,'       : Rp. ',Z)
K = V + X+ Y+ Z
print('Jumlah total biaya yang harus dibayar adalah Rp. ',K)
