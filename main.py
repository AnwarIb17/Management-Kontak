print("="*50)
print("Management Kontak".center(50))
print("Menu Utama".center(50))
print("="*50)

kontak1 = {"nama":"anwar","HP":"0829130814","email":"anwarIB@gmail.com"}
kontak2 = {"nama":"Kevin","HP":"912390410","email":"Kevin@gmail.com"}
kontak = [kontak1, kontak2]

while True:
  print("="*50)
  print("1. Melihat Semua Kontak")
  print("2. Menambahkan Kontak Baru")
  print("3. Menghapus Kontak")
  print("4. Keluar Dari Kontak")
  print("="*50)

  pilihan = input("\nMasukkan pilihan anda (1,2,3,4) :")

  if pilihan == '1':
    #melihat semua kontak
    if kontak:
      print("\n")
      for num,i in enumerate(kontak,start=1):
        print(f'{num}. {i["nama"]}, ({i["HP"]}, {i["email"]})')
      print("\n")
    else:
      print("kontak masih kosong !")
    
  elif pilihan == '2':
    # menambah kontak
    nama = input("Masukkan nama kontak baru       :")
    HP = input("Masukkan NO HP kontak baru      :")
    email = input("Masukkan email dari kontak baru :")
    kontak_baru = {"nama":nama, "HP":HP, "email":email}
    kontak.append(kontak_baru)
    
    print(f"\nkontak baru berhasil di tambahkan !")
    print("\n")
    
  elif pilihan == '3':
    # menghapus kontak
    print("\n")
    
    if kontak :
      print("Kontak yang tersedia")
      for num,i in enumerate(kontak,start=1):
        print(f'{num}. {i["nama"]}, ({i["HP"]}, {i["email"]})')
    else:
      print("kontak masih kosong !\n")
      continue
    
    i_hapus = int(input("Masukkan pilihan kontak yang ingin di hapus :"))
    del kontak[i_hapus-1]
    print("\nKontak yang dipilih telah berhasil di hapus !\n")

      
  elif pilihan == '4':
    # keluar dari kontak
    break
  
  else:
    print("Anda memasukkan pilihan yang salah")