def fungsi(**data):
    nama = data["nama"]
    tinggi = data["tinggi"]
    berat = data["berat"]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi(nama = "danis", tinggi = 180, berat = 80)

def math(*args, **kwargs):
    
    if kwargs["option"] == "tambah":
        output = 0
        for angka in args:
            output += angka
    
    elif kwargs["option"] == "kali":
        output = 1
        for angka in args:
            output *= angka

    else:
        print("tidak diketahui")
    
    return output



hasil = math(1,2,3,4, option = "tambah")
hasilSatu = math(1,2,3,4, option = "kali")
print(hasil)
print(hasilSatu)