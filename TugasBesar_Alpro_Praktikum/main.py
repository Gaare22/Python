from connectdb import *
from prettytable import from_db_cursor
from random import randint
import os

#FUNGSI

def booking():
    sql = "SELECT kode_pemesanan FROM tb_pemesanan WHERE kode_pemesanan = %s"
    val = (booking,)
    mycursor.execute(sql,val)
    myresult = mycursor.fetchall()
    for x in myresult:
        print("Kode Booking          = ",x[0])

def nama_pemesan():
    sql = "SELECT id_user1 FROM tb_pemesanan WHERE kode_pemesanan = %s"
    val = (booking,)
    mycursor.execute(sql,val)
    myresult = mycursor.fetchall()
    for x in myresult:
        print("Nama                  = ",x[0])

def jenis_kelamin():
    sql = "SELECT jenis_kelamin1 FROM tb_pemesanan WHERE kode_pemesanan = %s"
    val = (booking,)
    mycursor.execute(sql,val)
    myresult = mycursor.fetchall()
    for x in myresult:
        print("Jenis Kelamin         = ",x[0])

def tanggal_berangkat():
    sql = "SELECT berangkat FROM tb_pemesanan WHERE kode_pemesanan = %s"
    val = (booking,)
    mycursor.execute(sql,val)
    myresult = mycursor.fetchall()
    for x in myresult:
        print("Tanggal Berangkat     = ",x[0])

def relasi_kota_tujuan():
    sql = "SELECT kota_tujuan FROM tb_pemesanan \
        INNER JOIN tb_tiket ON tb_pemesanan.kode_bandara = tb_tiket.kode_bandara WHERE kode_pemesanan = %s"
    val4 = (booking,)
    mycursor.execute(sql,val4)
    myresult = mycursor.fetchall()
    for x in myresult:
        print("Kota Tujuan           = ",x[0])

def relasi_kelas():
    sql5 = "SELECT kelas FROM tb_pemesanan \
        INNER JOIN tb_kelas ON tb_pemesanan.kode_kelas = tb_kelas.kode_kelas WHERE kode_pemesanan = %s"
    val5 = (booking,)
    mycursor.execute(sql5,val5)
    myresult = mycursor.fetchall()
    for x in myresult:
        print("Kelas                 = ",x[0])

def relasi_jadwal():
    sql6 = "SELECT jadwal FROM tb_pemesanan \
        INNER JOIN tb_jadwa ON tb_pemesanan.kode_jadwal = tb_jadwa.kode_jadwal WHERE kode_pemesanan = %s"
    val6 = (booking,)
    mycursor.execute(sql6,val6)
    myresult = mycursor.fetchall()
    for x in myresult:
        print("Jadwal                = ",x[0])

def relasi_pukul():
    sql = "SELECT pukul FROM tb_pemesanan \
        INNER JOIN tb_jadwa ON tb_pemesanan.kode_jadwal = tb_jadwa.kode_jadwal WHERE kode_pemesanan = %s"
    val6 = (booking,)
    mycursor.execute(sql,val6)
    myresult = mycursor.fetchall()
    for x in myresult:
        print("Pukul                 = ",x[0])

def kota_tujuan():
    sql4 = "SELECT kota_tujuan FROM tb_tiket WHERE kode_bandara = %s"
    val4 = (kode_bandara,)
    mycursor.execute(sql4,val4)
    myresult = mycursor.fetchall()
    for x in myresult:
        print("Kota Tujuan           = ",x[0])
        break   

def kelas():
    sql5 = "SELECT kelas FROM tb_kelas WHERE kode_kelas = %s"
    val5 = (kelas,)
    mycursor.execute(sql5,val5)
    myresult = mycursor.fetchall()
    for x in myresult:
        print("Kelas                 = ",x[0])

def jadwal(): #jadwal
    sql6 = "SELECT jadwal FROM tb_jadwa WHERE kode_jadwal = %s"
    val6 = (kode_jadwal,)
    mycursor.execute(sql6,val6)
    myresult = mycursor.fetchall()
    for x in myresult:
        print("Jadwal                = ",x[0])

def harga(): #harga
    sql = "SELECT harga FROM tb_kelas WHERE kode_kelas = %s"
    val = (kelas,)
    mycursor.execute(sql,val)
    myresult = mycursor.fetchall()
    for x in myresult:
        print("Harga                 =  Rp.",x[0])

def pukul(): #pukul
    sql = "SELECT pukul FROM tb_jadwa WHERE kode_jadwal = %s"
    val6 = (kode_jadwal,)
    mycursor.execute(sql,val6)
    myresult = mycursor.fetchall()
    for x in myresult:
        print("Pukul                 = ",x[0])

def rupiah():
    sql = "SELECT harga FROM tb_kelas WHERE kode_kelas = %s"
    val = (kelas,)
    mycursor.execute(sql,val)
    myresult = mycursor.fetchall()
    for x in myresult:
        print("Rp. ",x[0])
    return x

def ubah_nama():
    sql = "SELECT nama FROM tb_user WHERE nama = %s"
    val = (nama,)
    mycursor.execute(sql,val)
    myresult = mycursor.fetchall()
    for x in myresult:
        print("Nama Sebelumnya      = ", x[0])

def ubah_jk():
    sql = "SELECT jenis_kelamin FROM tb_user WHERE jenis_kelamin = %s"
    val = (jk,)
    mycursor.execute(sql,val)
    myresult = mycursor.fetchall()
    for x in myresult:
        print("Jenis Kelamin Sebelumnya      = ", x[0])

def ubah_tanggal():
    sql = "SELECT tanggal_keberangkatan FROM tb_user WHERE nama = %s"
    val = (nama,)
    mycursor.execute(sql,val)
    myresult = mycursor.fetchall()
    for x in myresult:
        print("Tanggal Keberangkatan Sebelumnya         = ", x[0])
        return x

def ubah_kota():
    sql = "SELECT kota_tujuan FROM tb_tiket WHERE kode_bandara = %s"
    val = (kode_bandara,)
    mycursor.execute(sql,val)
    myresult = mycursor.fetchall()
    for x in myresult:
        print("Kota Tujuan Sebelumnya         = ", x[0])

def ubah_kelas():
    sql = "SELECT kelas FROM tb_kelas WHERE kode_kelas = %s"
    val = (kelas,)
    mycursor.execute(sql,val)
    myresult = mycursor.fetchall()
    for x in myresult:
        print("Kelas Tujuan Sebelumnya         = ", x[0])

def ubah_jadwal():
    sql = "SELECT pukul FROM tb_jadwa WHERE kode_jadwal = %s"
    val = (kode_jadwal,)
    mycursor.execute(sql,val)
    myresult = mycursor.fetchall()
    for x in myresult:
        print("Pukul Keberangkatan Sebelumnya         = ", x[0])

#BATAS FUNGSI

lanjut=True
while lanjut:
    os.system('cls')
    print("======================================")
    print("|           SELAMAT DATANG           |")
    print("|    LOKET PENJUALAN TIKET PESAWAT   |")
    print("|       PT. PESAWAT KITA SEMUA       |")
    print("|  BANDARA INTERNASIONAL YOGYAKARTA  |")
    print("======================================")
    print("\nMenu :")
    print("--------------------")
    print("1. Beli Tiket")
    print("2. Cetak Tiket")
    print("3. Cancel Tiket")
    print("0. Keluar")
    print("--------------------")
    pilih=int(input("--> Masukkan Pilihan Anda = "))
    if pilih == 1:
        os.system('cls')
        print("Anda Memilih Menu Beli Tiket Pesawat")
        print("--------------------------------------")
        nama = input("Masukkan Nama Anda                            = ")
        untuk_jk = True
        while untuk_jk:
            jk = input("Masukkan Jenis Kelamin [L/P]                  = ")
            if jk == 'L' or jk == 'l':
                jk = "Laki-laki"
                break
            elif jk == 'P' or jk == 'p':
                jk = "Perempuan"
                break
            else:
                print("Kode yang Anda Masukkan Salah")
        brngkt = input("Masukkan Tanggal Keberangkatan [yyyy/mm/dd]   = ")
        
        sql = "INSERT INTO tb_user (id_user, nama, jenis_kelamin, tanggal_keberangkatan) VALUES (%s,%s,%s,%s)"
        val = ("",nama,jk,brngkt)
        mycursor.execute(sql,val)
        mydb.commit()

        os.system("pause")
        os.system("cls")

        print("\nDaftar Tujuan Pesawat")
        mycursor.execute("SELECT kode_bandara, kota_tujuan FROM tb_tiket")
        x = from_db_cursor(mycursor)
        print(x)        
        kode_bandara=input("\nMasukkan Kode Bandara Tujuan Anda           = ")

        os.system("pause")
        os.system("cls")

        print("\nDaftar Kelas Pesawat")
        sql = "SELECT kode_kelas, kelas, harga FROM tb_kelas WHERE kode_bandara = %s"
        val = (kode_bandara,)
        mycursor.execute(sql,val)
        y = from_db_cursor(mycursor)
        print(y)        
        kelas=input("\nMasukkan Kode Kelas Pilihan Anda                 = ")
        
        os.system('pause')
        os.system("cls")

        print("\nJadwal Keberangkatan Pesawat")
        sql = "SELECT * FROM tb_jadwa WHERE kode_bandara = %s ORDER BY pukul"
        val = (kode_bandara,)
        mycursor.execute(sql,val)
        z = from_db_cursor(mycursor)
        print(z)        
        kode_jadwal = input("\nMasukkan Kode Jadwal Pilihan Anda           = ")

        os.system('pause')
        os.system("cls")

        oke=True
        while oke :
            os.system('cls')
            print("----------------------------------------")
            print("             DATA PEMESANAN             ")
            print("----------------------------------------")
            print("Nama                  = ",nama)
            print("Jenis Kelamin         = ",jk)
            print("Tanggal Keberangkatan = ",brngkt)
            kota_tujuan()
            kelas()
            jadwal()
            pukul()
            harga()

            print("---------------------------")
            pilih2=input("\nApakah Data Sudah Benar? [Y/T]     = ")
            if pilih2 == 'Y' or pilih2 == 'y':
                os.system("pause")
                oke=False
            elif pilih2 == 'T' or pilih2 == 't':
                os.system('pause')
                os.system("cls")
                print("Ubah Data :")
                print("--------------")
                print("1. Nama")
                print("2. Jenis Kelamin")
                print("3. Tanggal Keberangkatan")
                print("4. Kota Tujuan")
                print("5. Kelas")
                print("6. Jadwal Keberangkatan")
                print("0. Kembali")
                print("--------------")
                pilih3=int(input("Masukkan Data yang ingin di ubah = "))
                if pilih3 == 1:
                    os.system('pause')
                    os.system("cls")
                    print("Ubah Nama ")
                    print("-------------")
                    ubah_nama()
                    print("-------------")
                    namabaru=input("Nama Baru            = ")
                    nama = namabaru
                elif pilih3 == 2:
                    os.system('pause')
                    os.system("cls")
                    print("Ubah Jenis Kelamin ")
                    print("-------------")
                    ubah_jk()
                    print("-------------")
                    jkbaru=input("Jenis Kelamin Baru            = ")
                    jk = jkbaru
                elif pilih3 == 3:
                    os.system('pause')
                    os.system("cls")
                    print("Ubah Tanggal Keberangkatan ")
                    print("-------------")
                    ubah_tanggal()
                    print("-------------")
                    brngktbaru=input("Tanggal Keberangkatan Baru               = ")
                    brngkt = brngktbaru
                elif pilih3 == 4:
                    os.system('pause')
                    os.system("cls")
                    print("Ubah Kota Tujuan ")
                    print("-------------")
                    ubah_kota()
                    print("-------------")
                    mycursor.execute("SELECT kode_bandara, kota_tujuan FROM tb_tiket")
                    x = from_db_cursor(mycursor)
                    print(x)        
                    kode_bandara_baru=input("\nMasukkan Kode Bandara Tujuan Anda           = ")
                    kode_bandara = kode_bandara_baru

                    os.system('pause')
                    os.system("cls")

                    print("\nDaftar Kelas Pesawat")
                    sql = "SELECT kode_kelas, kelas, harga FROM tb_kelas WHERE kode_bandara = %s"
                    val = (kode_bandara,)
                    mycursor.execute(sql,val)
                    y = from_db_cursor(mycursor)
                    print(y)        
                    kelas_baru=input("Masukkan Kode Kelas Pilihan Anda                 = ")
                    kelas = kelas_baru
                    
                    os.system('pause')
                    os.system("cls")

                    print("\nJadwal Keberangkatan Pesawat")
                    sql = "SELECT * FROM tb_jadwa WHERE kode_bandara = %s ORDER BY pukul"
                    val = (kode_bandara,)
                    mycursor.execute(sql,val)
                    z = from_db_cursor(mycursor)
                    print(z)        
                    kode_jadwal_baru = input("\nMasukkan Kode Jadwal Pilihan Anda           = ")
                    kode_jadwal = kode_jadwal_baru

                elif pilih3 == 5:
                    os.system('pause')
                    os.system("cls")
                    print("Ubah Kelas ")
                    print("-------------")
                    ubah_kelas()
                    print("-------------")
                    sql = "SELECT kode_kelas, kelas, harga FROM tb_kelas WHERE kode_bandara = %s"
                    val = (kode_bandara,)
                    mycursor.execute(sql,val)
                    y = from_db_cursor(mycursor)
                    print(y)        
                    kelasbaru = input("Masukkan Kode Kelas Pilihan Anda                 = ")
                    kelas = kelasbaru
                elif pilih3 == 6:
                    os.system('pause')
                    os.system("cls")
                    print("Ubah Jadwal ")
                    print("-------------")
                    ubah_jadwal()
                    print("-------------")
                    sql = "SELECT * FROM tb_jadwa WHERE kode_bandara = %s ORDER BY pukul"
                    val = (kode_bandara,)
                    mycursor.execute(sql,val)
                    z = from_db_cursor(mycursor)
                    print(z)        
                    kode_jadwal_baru = input("\nMasukkan Kode Jadwal Pilihan Anda           = ")
                    kode_jadwal = kode_jadwal_baru
                elif pilih3 == 0:
                    oke
                else:
                    print("OK")
                    break
            else:
                print("KODE SALAH")

        os.system('cls')
        beli=input("Lanjutkan Pembelian [Y/T]    = ")
        print("----------------------------------------")
        
        if beli == 'Y' or beli == 'y':
            os.system("cls")
            print("Menu Pembayaran")
            print("-----------------")
            print("\nTagihan Anda     ")
            print("-----------------")
            harga = rupiah()
            print("-----------------")
            # print(type(harga)) #tuple
            values = ','.join(str(v) for v in harga)
            # print(type(values)) #str
            h = int(values)
            # print(type(h)) #int

            kurang = True
            while kurang:
                uang=int(input("\nMasukkan Nominal Uang            = Rp. "))
                if uang < h:
                    print("Maaf Uang Anda Kurang") 
                elif uang == h:
                    print("-------------------------------------------------")
                    print("Uang Anda                        = Rp. ", uang)
                    print("Jumlah yang harus di bayar       = Rp. ", h)
                    print("-------------------------------------------------")
                    print("Uang Pas, Tidak ada Kembalian")
                    os.system('pause')
                    break
                else:
                    kembali = uang - h
                    print("-------------------------------------------------")
                    print("Uang Anda                        = Rp. ", uang)
                    print("Jumlah yang harus di bayar       = Rp. ", h)
                    print("-------------------------------------------------")
                    print("Kembalian                        = ",kembali)
                    os.system('pause')
                    break
        elif beli == 'T' or beli =='t':
            break
        else:
            print("Kode Salah, Silahkan pilih Y/T")

        os.system('cls')
        bil = randint(0,20)
        print("-------------------------------")
        print("Pembelian Anda Telah Berhasil")
        print("-------------------------------")
        os.system('pause')
        os.system('cls')
        print("-------------------------------------")
        print("--------------- TIKET ---------------")
        print("-------------------------------------")
        print("Nama                  = ",nama)
        print("Jenis Kelamin         = ",jk)
        print("Tanggal Keberangkatan = ",brngkt)
        kota_tujuan()
        kelas()
        jadwal()
        pukul()
        harga()
        print("KODE BOOKING          = ",bil)
        print("-------------------------------------")
        print("-------------------------------------")
        os.system('pause')
        
        msql = "INSERT INTO tb_pemesanan(id_pemesanan, kode_pemesanan, id_user1, kode_bandara, kode_jadwal, kode_kelas, jenis_kelamin1, berangkat) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        myval = ('',bil,nama,kode_bandara,kode_jadwal,kelas,jk,brngkt)
        mycursor.execute(msql,myval)
        mydb.commit()
        

    elif pilih == 2:
        os.system('cls')
        print("Anda Memilihi Menu Cetak Tiket Pesawat")
        print("-------------------------------------------------")
        booking = input("Masukkan Kode Booking Anda   = ")
        os.system('pause')

        os.system('cls')
        print("-------------------------------------")
        print("--------------- TIKET ---------------")
        print("-------------------------------------")            
        nama_pemesan()
        jenis_kelamin()
        tanggal_berangkat()
        relasi_kota_tujuan()
        relasi_kelas()
        relasi_jadwal()
        relasi_pukul()
        print("-------------------------------------")
        print("-------------------------------------")
        os.system('pause')
        

    elif pilih == 3:
        os.system('cls')
        print("Anda memilih menu Batalkan Tiket")
        print("-------------------------------------------------")
        batal_tiket = input("Masukkan kode booking Anda = ")
        os.system('pause')
        os.system('cls')
        batal=input("Lanjutkan Pembatalan [Y/T]    = ")
        if batal == 'Y' or batal == 'y':
            msql = "DELETE FROM tb_pemesanan WHERE kode_pemesanan = %s"
            myval = (batal_tiket,)
            mycursor.execute(msql,myval)
            mydb.commit()

            print("TIKET SUDAH DIBATALKAN")
            os.system('pause')
            


        elif batal == 'T' or batal == 't':
            print("CANCEL TIKET DI BATALKAN")
            os.system('pause')
            break

    elif pilih == 0:
        lanjut=False
        break

    else:
        print("MAAF, KODE SALAH")
        os.system('pause')

os.system('cls')
print("-----------------------------------------------")
print("   Terimakasih Telah Menggunakan Program Ini")
print("-----------------------------------------------")