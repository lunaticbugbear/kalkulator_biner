
while True:
    print('----------------------')
    print('1. Binary to Decimal |')
    print('2. Decimal to Binary |')
    print('----------------------')
    # Memberikan user pilihan mode
    mode = int(input('Pilih mode: '))

        # Konversi biner ke desimal
    if mode == 1:
        bin_num = int(input('Masukkan bilangan binary: '))
        result = 0
        bin_num_reverse = str(bin_num)[::-1]
        
        # Melakukan perhitungan konversi biner ke desimal
        for x in range(len(bin_num_reverse)):
            if bin_num_reverse[x] == '1':
                result += 2**x
        
        print(f'Hasil: {result}')
        
    # Konversi desimal ke biner
    elif mode == 2:
        dec_num = int(input('Masukkan bilangan desimal: '))
        result = bin(dec_num)[2:]
        print(f'Hasil: {result}')
        
    # Jika pengguna memasukkan pilihan selain 1 atau 2
    elif mode != 1 and mode != 2:
        print('Pilihan tidak tersedia. Mohon masukkan pilihan yang tersedia.')
        continue
    
    
    # Meminta pengguna untuk mengulang program atau mengakhirinya
    repeat = input('Apakah kamu ingin mengulang program (y/n): ')
    
    if repeat == 'y':
        continue
    
    else:
        print('Terima kasih telah menggunakan kalkulator ini :)')
        break
