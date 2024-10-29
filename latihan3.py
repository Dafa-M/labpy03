saldo = 1_000_000

while True:
    print(f"\nSaldo saat ini: Rp {saldo}")
    print("1. Tarik Tunai")
    print("2. Keluar")

    pilihan = input("Pilih menu (1/2): ")
    
    if pilihan == "1":
        jumlah = int(input("Masukkan jumlah penarikan: "))
        
        if jumlah <= saldo:
            saldo -= jumlah
            print("Penarikan berhasil!")
        else:
            print("Saldo tidak mencukupi!")
            
    elif pilihan == "2":
        print("Terima kasih telah menggunakan ATM UPB MEGAH!")
        break
    else:
        print("Pilihan tidak valid! Silakan pilih 1 atau 2.")
