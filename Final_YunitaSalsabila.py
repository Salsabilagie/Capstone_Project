#Stok Penjualan Minuman in Listed Dictionary :[{'Kode','Produk','Barista','Jenisminuman','Kategori','Stok','Harga'}]

Minuman = [
    {'Kode Produk':'P1',
     'Nama Produk':'Palma',
     'Barista':'Salsa',
     'Kategori':500,
     'Jenis Minuman':'Coffe',
     'Stok':22,
     'Harga':44000},

    {'Kode Produk':'C1',
     'Nama Produk':'Carlm',
     'Barista':'Wira',
     'Kategori':350,
     'Jenis Minuman':'Coffe',
     'Stok':47,
     'Harga':35000},
     
    {'Kode Produk':'L1',
     'Nama Produk':'Latte',
     'Barista':'Bobo',
     'Kategori':350,
     'Jenis Minuman':'Coffe',
     'Stok':35,
     'Harga':37000},
     
    {'Kode Produk':'M1',
     'Nama Produk':'Matcha',
     'Barista':'Bayu',
     'Kategori':500,
     'Jenis Minuman':'NonCof',
     'Stok':27,
     'Harga':46000},

    {'Kode Produk':'RV1',
     'Nama Produk':'RedVel',
     'Barista':'Ayu',
     'Kategori':350,
     'Jenis Minuman':'NonCof',
     'Stok':15,
     'Harga':36000},]

#Main Menu 
def MainMenu(): # Input menu (1-5)
    global menu
    menu = int(input('''
    ----------Coffe Shop Cosan---------
    ________________________________________
    Menu:
    1. Daftar Stok Minuman
    2. Tambah Daftar Minuman
    3. Hapus Daftar Minuman
    4. Update Stok dan Harga Minuman
    5. Keluar Program
    
    Pilihan Menu : '''))
    return menu


# Sub Menu
def SubMenu(): # Input sub menu (1-3)
    global subMbenu
    subMbenu = int(input('''
    1] Daftar Lengkap
    2] Daftar Stok
    3] Kembali ke Menu Utama
    Masukan Sub-Menu Daftar Stok : '''))
    return subMbenu

# Daftar Minuman Lengkap Print
printFormat = "{:<5}" + "{:<15}" * (len(Minuman[0]))

def PrintLengkap():
# Menampilkan judul
    print('Daftar Lengkap Stock Minuman')
# Loop item di dalam Minuman
    list_key = list(Minuman[0].keys())
    print(printFormat.format("", *list_key))
    for value in Minuman:
        list_value = list(value.values())
        # Menampilkan item berdasarkan format
        print(printFormat.format("", *list_value))

# Sort harga descending
def PrintSortHargaDesc():
    sortedHargaMinuman = sorted(Minuman, key=lambda k: k['Harga'], reverse=True)
    print('''
--------------------------Daftar Lengkap Harga Minuman-----------------------
_________________________________________________________________________________''')
    print('|Kode Minuman\t|Nama Produk\t|Barista\t|Kategori\t|Stok\t|Harga\t')
    for i in range(len(sortedHargaMinuman)):
        print(f"|{sortedHargaMinuman[i]['Kode Produk']}\t\t|{sortedHargaMinuman[i]['Nama Produk']}\t|{sortedHargaMinuman[i]['Barista']}\t|{sortedHargaMinuman[i]['Kategori']}\t|{sortedHargaMinuman[i]['Stock']}\t\t|{sortedHargaMinuman[i]['Harga']}\t\t|")
    print('\n')

# Sort harga ascending
def sortHargaAsc(h):
    return h['Harga']

# Daftar per produk
def PrintStok():
    Kode_produk = input('Masukan kode produk?')
    for item in Minuman : 
        if item ['Kode Produk'] == Kode_produk :
            list_key = list(item.keys())
            list_value = list(item.values())
            print(printFormat.format("", *list_key))
            print(printFormat.format("", *list_value))
            break

# # Sort stok descending
# def PrintSortStokDesc():
#     sortedStokMinuman = sorted(Minuman, key=lambda k: k['Stok'], reverse=True)
#     print('''
# ---------Daftar Stok Minuman--------
# _________________________________________''')
#     print('|Kode Minuman\t|Nama Produk\t|Barista\t|Stok\t|')
#     for i in range(len(sortedStokMinuman)):
#         print(f"|{sortedStokMinuman[i]['Kode Produk']}\t\t|{sortedStokMinuman[i]['Nama Produk']}\t|{sortedStokMinuman[i]['Barista']}\t|{sortedStokMinuman[i]['Stok']}\t|")
#     print('\n')

# # Sort stok ascending
# def sortStokAsc(s):
#     return s['Stok']

# Validasi Menu 2 alphanumeric
def validasiKodeNew(in1):
    if in1.isalnum():
        return True
    else:
        print('Masukan hanya alphanumerik')

# Validasi Menu 2 duplikasi kode
def validasiKodeMinumanBaru(in1):
    for i in range(len(Minuman)):
        checker = Minuman[i]['Kode Produk']
        if checker == in1:
            print('Kode minuman sudah dipakai, masukan kode yang berbeda!')
            return False
    return True


# Tambah stok minuman
def TambahDaftar():
    print('-------------------------------------Before--------------------------------------')
    PrintLengkap()

    while True:    
        kodeNew = input('Masukan kode minuman baru : ').upper()
        if validasiKodeMinumanBaru(kodeNew):
            if validasiKodeNew(kodeNew):
                break
    ProdukNew = input('Masukan produk minuman baru : ')
    BaristaNew = input('Masukan nama barista baru : ')
    KategoriNew = input('Masukan kategori minuman baru : ')
    while True:
        try:
            JenisNew = int(input('''Jenis Minuman:
    1] Coffe
    2] Noncoffe 
    Masukan Jenis minuman baru : '''))
            if JenisNew == 1:
                KategoriNew = 'Coffe'
                break
            elif JenisNew == 2:
                KategoriNew = 'Noncoffe'
                break
            else:
                print('Masukan angka sesuai pilihan kategori')
        except ValueError:
            print('Masukan hanya angka!')
    StokNew = int(input('Masukan stok minuman baru : '))
    HargaNew = int(input('Masukan harga minuman baru : '))
    print('\nPenambahan daftar minuman berhasil!')

    #Append into main list
    Minuman.append({'Kode Produk':kodeNew,'Nama Produk':ProdukNew,'Barista':BaristaNew,'Kategori Minuman':KategoriNew,'Jenis':JenisNew,'Stok':StokNew,'Harga':HargaNew})
    
    #Daftar setelah penambahan
    print('--------------------------------------After--------------------------------------')
    PrintLengkap()

# Validasi duplikasi hapus menu 3
def ValidasiDupDel(in1):
    for i in Minuman:
        if i['Kode Produk'] == in1:
            break
    else:
        print('Kode minuman tidak ada dalam daftar')
        return True
            

# Hapus daftar minuman
def HapusDaftar(in1):
    for i in range(len(Minuman)):
        checker = Minuman[i]['Kode Produk']
        if checker == in1:
            finalDel = i
            while True:
                delConfirmation = input('Apakah anda yakin ingin menghapus minuman? (Y/N): ').upper()
                if delConfirmation == 'N':
                    print('Penghapusan data dibatalkan')
                    break
                elif delConfirmation == 'Y':
                    del Minuman[finalDel]
                    print(f'Penghapusan kode minuman {in1} berhasil\n')
                    #Daftar setelah penghapusan daftar
                    print('--------------------------------------After--------------------------------------')
                    PrintLengkap()
                    break
                else:
                    print('Hanya masukan jawaban Y/N')
            break


# Validasi duplikasi hapus menu 4.1 dan 4.2
def ValidasiDupUpd(in1):
    for i in Minuman:
        if i['Kode Produk'] == in1:
            break
    else:
        print('Kode minuman tidak ada dalam daftar')
        return True

# Update stok minuman menu 4.1
def UpdateStok(in1,in2):
    ValidasiDupUpd(in1)
    for i in range(len(Minuman)):
        checker = Minuman[i]['Kode Produk']
        if checker == in1:
            finalUpdS = i
            while True:
                delConfirmation = input('Apakah anda yakin ingin update stok minuman? (Y/N): ').upper()
                if delConfirmation == 'N':
                    print('Update stok dibatalkan')
                    break
                elif delConfirmation == 'Y':
                    Minuman[finalUpdS]['Stok'] = in2
                    print(f'Update stok kode minuman {in1} berhasil\n')
                    #Daftar setelah update stok
                    print('--------------------------------------After--------------------------------------')
                    PrintLengkap()
                    break
                else:
                    print('Hanya masukan jawaban Y/N')
            break


# Update harga minuman menu 4.2
def UpdateHarga(in1,in2):
    ValidasiDupUpd(in1)
    for i in range(len(Minuman)):
        checker = Minuman[i]['Kode Produk']
        if checker == in1:
            finalUpdH = i
            while True:
                delConfirmation = input('Apakah anda yakin ingin update harga minuman? (Y/N): ').upper()
                if delConfirmation == 'N':
                    print('Update harga minuman dibatalkan')
                    break
                elif delConfirmation == 'Y':
                    Minuman[finalUpdH]['Harga'] = in2
                    print(f'Update harga kode minuman {in1} berhasil\n')
                    #Daftar setelah update harga minuman
                    print('--------------------------------------After--------------------------------------')
                    PrintLengkap()
                    break
                else:
                    print('Hanya masukan jawaban Y/N')
            break

# Program 
while True:
    try:
        MainMenu()
        if menu == 1:
            while True:    
                try:
                    SubMenu()
                    if subMbenu == 3: # Kembali ke Main menu
                        break
                    elif subMbenu == 2: # Daftar stok saja
                        PrintStok()
                    elif subMbenu == 1: # Daftar minuman lengkap
                        PrintLengkap()
                        sortMenu2 = int(input('Sorting Harga:\n1. Tertinggi\n2. Terendah\n3. Kembali\nMasukan menu sorting : \n'))
                        if sortMenu2 == 2:
                            Minuman.sort(key=sortHargaAsc)
                            PrintLengkap()
                        elif sortMenu2 == 1:
                            Minuman.sort(key=sortHargaAsc, reverse=True)
                            PrintLengkap()
                            #PrintSortStokDesc()
                        elif sortMenu2 == 3:
                            break
                        else:
                            print('Masukan Hanya Angka Menu!') 
                    else:
                        print('Masukan Hanya Angka Menu!')
                except ValueError:
                    print('Masukan Hanya Angka Menu!')
        elif menu == 2:
            TambahDaftar()
        elif menu == 3:
            #Daftar sebelum penghapusan daftar
            print('-------------------------------------Before--------------------------------------')
            PrintLengkap()
            while True:
                kodeDel = input('Masukan kode minuman yang ingin dihapus : ').upper()
                if ValidasiDupDel(kodeDel):
                    continue
                HapusDaftar(kodeDel)
                break
        elif menu == 4:
            while True:
                try:
                    subMenu4 = int(input('''Submenu Update:
    1] Update Stok Minuman
    2] Update Harga Minuman
    3] Kembali ke Menu Utama
    Masukan pilihan update : '''))
                    if subMenu4 == 1:
                        #Daftar sebelum update stok minuman
                        print('-------------------------------------Before--------------------------------------')
                        PrintLengkap()
                        while True:
                            kodeUpdateStok = input('Masukan kode minuman : ').upper()
                            stokUpdate = int(input('Masukan update stok : '))
                            if ValidasiDupUpd(kodeUpdateStok):
                                continue
                            UpdateStok(kodeUpdateStok,stokUpdate)
                            break
                    elif subMenu4 == 2:
                        #Daftar sebelum update harga minuman
                        print('-------------------------------------Before--------------------------------------')
                        PrintLengkap()
                        while True:
                            kodeUpdateHarga = input('Masukan kode minuman : ').upper()
                            hargaUpdate = int(input('Masukan update harga : '))
                            if ValidasiDupUpd(kodeUpdateHarga):
                                continue
                            UpdateHarga(kodeUpdateHarga,hargaUpdate)
                            break
                    elif subMenu4 == 3:
                        break
                    else:
                        print('Masukan Hanya Angka Menu!') 
                except ValueError:
                    print ('Masukan Hanya Angka Menu!')
        elif menu == 5:
            break
        elif menu != 1 or menu != 2 or menu != 3 or menu != 4 or menu != 5:
            print('Masukan angka menu yang sesuai!')
    except ValueError:
        print('Masukan Hanya Angka Menu!')

