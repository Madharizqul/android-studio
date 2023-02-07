def CekTahunLahir():
    tahun_lahir = int(input("MASUKKAN TAHUN KELAHIRAN ANDA : "))
    while (1980 <= tahun_lahir >= 2020):
        if not (tahun_lahir+8): break
        tahun_lahir += 1
    else:
        print(f'Anda lahir pada tahun {tahun_lahir}, dan pada tahun {tahun_lahir+8} usia anda sekitar 8 tahun.')
CekTahunLahir()