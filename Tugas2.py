from os import system
from datetime import datetime
 
def view_menu():
    system("cls")
    menu = """
    Pendaftaran Siswa Baru
    [A] - Daftar Siswa
    [B] - Tampilkan semua siswa yang mendaftar
    [C] - Cari nama siswa
    [D] - Perbarui biodata siswa
    [E] - Hapus Nama Siswa
    [I] - Pengumuman
    [Q] - KELUAR
    """
    print(menu)
 
def verify_ans(char):
    char = char.upper()
    if char == "Y":
        return True
    else:
        return False
 
def print_header(msg):
    system("cls")
    print(msg)
 
def create_id_students():
    today = datetime.now()
    year = today.year
    month = today.month
    hari = today.day
    counter = len(students_list)+1
    id_contact = str("%4d%02d%02d-C%03d" % (year, month, hari, counter))
    return id_contact
 
def create_students_list(id_students = None, all_fields = False, TTL = True):
    if id_students != None and all_fields == False:
        print(f"""
        -DATA DITEMUKAN-
    ID \t:{id_students}
    Nama \t:{students_list[id_students]["nama"]}
    Gender \t:{students_list[id_students]["gender"]}
    Kelas \t:{students_list[id_students]["kelas"]}
    Asal \t:{students_list[id_students]["asal"]}
    TTL \t:{students_list[id_students]["ttl"]}
            """)
    elif id_students != None and TTL == False:
        print(f"""
        -DATA DITEMUKAN-
    ID \t:{id_students}
    Nama \t:{students_list[id_students]["nama"]}
    Gender \t:{students_list[id_students]["gender"]}
    Kelas \t:{students_list[id_students]["kelas"]}
    Asal \t:{students_list[id_students]["asal"]}
            """)
    elif all_fields == True:
        for id_students in students_list:
            nama = students_list[id_students]["nama"]
            gender = students_list[id_students]["gender"]
            kelas = students_list[id_students]["kelas"]
            asal = students_list[id_students]["asal"]
            ttl = students_list[id_students]["ttl"]
            print(f"ID:{id_students}\tNama:{nama}\tGender:{gender}\tKelas:{kelas}\tAsal:{asal}\tTTL:{ttl}")
 
def register_student():
    print_header("-Pendaftaran Siswa baru-")
    nama = input("Nama Siswa\t:")
    gender = input("Jenis Kelamin\t:")
    kelas = input("Kelas\t:")
    asal = input("Asal Sekolah\t:")
    ttl = input("Tempat, Tanggal lahir\t:")

    user_ans = input("Tekan Y untuk menyimpan Data (Y/N) : ")

    if verify_ans(user_ans):
        id_students = create_id_students()
        print("Menyimpan Data...")
        students_list[id_students] = {
            "nama" : nama,
            "gender" : gender,
            "kelas" : kelas, 
            "asal" : asal,
            "ttl" : ttl
        }
        print("Data Tersimpan")
    else:
        print("Data batal disimpan")
    input("Tekan ENTER untuk kembali ke MENU")
 
def print_bio():
    print_header("-SEMUA KONTAK-")
    if len(students_list) == 0:
        print("<BELUM ADA KONTAK YANG DISIMPAN>")
    else:
        create_students_list(all_fields=True)
    input("Tekan ENTER untuk kembali ke MENU")

def searching_by_name(students):
    for id_students in students_list:
        if students_list[id_students]["nama"] == students:
            create_students_list(id_students=id_students)
            return True
    else:
        print("-DATA TIDAK DITEMUKAN-")
        return False
 
def get_students_id_from_name(students):
    for id_students in students_list:
        if students_list[id_students]["nama"] == students:
            return id_students
 
def seraching_by_id(id_students):
    if id_students in students_list:
        create_students_list(id_students=id_students)
        return True
    else:
        print("-DATA TIDAK DITEMUKAN-")
        return False
 
def search_bio():
    print_header("-CARI KONTAK-\n")
    nama = input("Nama Kontak Yang Dicari : ")
    result = searching_by_name(nama)
    input("Tekan ENTER untuk kembali ke MENU")

def return_code(nama):
    searched_dict = {"nama":nama}
    for code in students_list:
        if {students_list[code]["nama"]} == {searched_dict["nama"]}:
            return code

def delete_bio():
    print_header("-MENGHAPUS KONTAK-")
    nama = input("Masukkan Nama Kontak yang akan Dihapus : ")
    code = return_code(nama)
    if code:
        respon = input(f"Yakin ingin menghapus {nama} (Y/N): ")
        if verify_ans(respon):
            del students_list[code]
            print("DATA telah dihapus.")
 
        else:
            print("DATA batal dihapus")
    input("Tekan ENTER untuk kembali ke menu utama")
 
def update_nama(students):
    print(f"Nama Lama \t:{students}")
    new_nama = input("Nama Baru\t: ")
    respon = input("Apa yakin ingin mengganti datanya (Y/N) : ")
    if verify_ans(respon):
        id_students = get_students_id_from_name(students)
        students_list[id_students]["nama"] = new_nama
        print("Data telah di-update")
    else:
        print("Data batal diperbarui")
 
def update_asal(students):
    id_students = get_students_id_from_name(students)
    print(f"Nama \t:{students_list[id_students]['nama']}")
    print(f"Asal Lama\t:{students_list[id_students]['asal']}")
    new_asal = input("Asal Baru\t: ")
    respon = input("Apa yakin ingin mengganti datanya (Y/N) : ")
    if verify_ans(respon):
        students_list[id_students]['asal'] = new_asal
        print("Data telah di-update")
    else:
        print("Data batal diperbarui")
 
def update_ttl(students):
    id_students = get_students_id_from_name(students)
    print(f"Nama \t:{students_list[id_students]['nama']}")
    print(f"TTL Lama\t:{students_list[id_students]['ttl']}")
    new_ttl = input("TTL Baru\t: ")
    respon = input("Apa yakin ingin mengganti datanya (Y/N) : ")
    if verify_ans(respon):
        students_list[id_students]['ttl'] = new_ttl
        print("Data telah di-update")
    else:
        print("Data batal diperbarui")
 
def update_bio():
    print_header("PERBARUI DATA KONTAK\n")
    nama = input("Nama Kontak yang ingin diperbarui : ")
    result = searching_by_name(nama)
    if result:
        print("Data yang ingin diperbarui : ")
        print("[1]. Nama , [2]. Asal , [3]. TTL")
        respon = input("Pilihan : ")
        if respon == "1":
            update_nama(nama)
        elif respon == "2":
            update_asal(nama)
        elif respon == "3":
            update_ttl(nama)
    input("Tekan ENTER untuk kembali ke menu utama")

def attention():
    print_header("Pengumuman")
    msg = ("Untuk siswa/i SMP dan SMA baru, silahkan masuk pada tanggal 16 Juni 2020, pada pukul 08.00 memakai seragam sekolah lama. Terima Kasih")
    print(msg)
    input("Tekan ENTER untuk kembali ke menu utama")

def check_input(char):
    char = char.upper()
    if char == "Q":
        return True
    elif char == "A":
        register_student()
    elif char == "B":
        print_bio()
    elif char == "C":
        search_bio()
    elif char == "D":
        update_bio()
    elif char == "E":
        delete_bio()
    elif char == "I":
        attention()

###MAIN PROGRAM#####
 
students_list = {
    "20201007-C001":{
        "nama" : "Lucky",
        "gender" : "Pria",
        "kelas" : "10",
        "asal" : "Bangau",
        "ttl" : "Jakarta, 3 November 2005"
    },
    "20201007-C002" : {
        "nama" :"Maria" ,
        "gender" : "Wanita",
        "kelas" : "7",
        "asal" : "Kumbang",
        "ttl" : "Palembang, 10 April 2008"
    }
}
stop = False

while not stop:
    view_menu()
    user_input = input("Pilihan : ")
    stop = check_input(user_input)