''' 🗺️BASIC DATA TYPES🗺️ '''
# x = 5
# y = 7

# print(x+y)

# x = 15

# print('hello world') line comment
''' block comment
print(x+y)
'''

# nama = 'faiz'
# domisili = "Bogor"
# umur = 28
# suhu = 36.2
# perempuan = False

# print(nama, umur, perempuan)
# print('nama:', type(nama))
# print('domisili:', type(domisili))
# print('umur:', type(umur))
# print('suhu:', type(suhu))
# print('perempuan:', type(perempuan))

# kota = ['Jakarta', 'Medan', 'Samarinda', 'Makassar', 'Ambon']
# deskripsi = {
#   'nama': 'faiz',
#   'umur': 28,
#   'perempuan': False
# }

# print(kota)
# print('kota:', type(kota))

# print(deskripsi)
# print('deskripsi:', type(deskripsi))

''' 🗺️DATA DEFINITION🗺️ '''

# x = 5
# y = 7

# print(x + y, type(x + y))
# print(x - y, type(x - y))
# print(x * y, type(x * y))
# print((x * y) / y, type((x * y) / y))

# print(y ** x, type(y ** x))

# data = '5'
# data_int = int(data)
# data_float = float(data)

# print(data, type(data))
# print(data_int, type(data_int))
# print(data_float, type(data_float))
# print(int(data_float), type(int(data_float)))
# print(str(data_float), type(str(data_float)))

# text = 'don\'t touch'
# print(text)

# text2 = "faiz mengatakan:\"jangan menyerah!\""
# print(text2)

# text3 = 'ini faiz\nfaiz belajar python' # \n artinya adalah baris baru
# print(text3)

# text4 = 'ini faiz\n \tfaiz belajar python' # \t artinya adalah baris menjorok
# print(text4)

# text5 = 'C:\some\name'
# text6 = r'C:\some\name'
# print(text5)
# print(text6)

# text7 = 'Py'
# text8 = 'thon'

# print(text7 text8)
# print('Py' 'thon')
# print(text7 + text8)
# print(3 * text7 + text8)

# print(
#   'saya sedang belajar webgis di geocourse'
#   'saya sedang belajar python saat ini'
#   'setelah ini saya akan belajar django'
# )

# print(
# '''
# saya sedang belajar webgis di geocourse
# saya sedang belajar python saat ini
# setelah ini saya akan belajar django
# '''
# )

# text9 = 'geocourse.id'
# text10 = 'saya ingin belajar di {text9}'
# text11 = f'saya ingin belajar di {text9}'

# print(text10)
# print(text11)

''' 🗺️TEXT SLICING🗺️ '''
word = 'Python'
# print(word[0])
# print(word[3])
# print(word[-1])
# print(word[-5])

# print(word[1:3])
# print(word[:3])
# print(word[3:])
# print(word[-3:-1])
# print(word[:-2])
# print(word[-2:])

# print(word[-3:-1] + word[:3])

# print(word[10])
# print(word[-10])

# print(word[1:3])
# print(word)

# word[1:3] = 'Faiz' error karena string bersifat tetap, tidak bisa diubah 
# print(word)

# Python --> PFaizthon
# print(word[0] + 'Faiz' + word[2:])

# word = word[0] + 'Faiz' + word[2:]

# print(word)

# print(len(word))

# word2 = 'belajar python di geocourse'
# print(len(word2))

# word3 = 'belajar python\ndi geocourse'
# print(len(word3))

# print('{0} {1}'.format('faiz', 'geocourse'))
# print('{0}-{1}-{2}'.format('2023', '09', '23'))

# NIK --16 digit 1234561234560001
# nik = '1234561503560001'
# 12 - kode provinsi
# 34 - kode kabupaten
# 56 - kode kecamatan
# 15 - tgl lahir
# 03 - bulan lahir
# 56 - tahun lahir
# 0001 - indeks pendaftaran

# prov = nik[0:2]
# kab = nik[2:4]
# kec = nik[4:6]
# tgl = nik[6:8]
# bln = nik[8:10]
# thn = nik[10:12]

# print(prov, kab, kec, tgl, bln, thn)

# lahir = '19{0}-{1}-{2}'.format(thn, bln, tgl)
# print(lahir)

''' 🗺️LISTS🗺️ '''
# kota = ['Jakarta', 'Medan', 'Samarinda', 'Makassar', 'Ambon']

# print(kota)
# print(kota[0])
# print(kota[3])
# print(kota[1:3])
# print(kota[:3])
# print(kota[3:])

# print(kota[3][-3])

# kota[3] = 'Merauke' # jika string sifatnya tetap, berbeda dengan list. Pada list object bisa kita ubah
# print(kota)

# kota2 = ['Palembang', 'Manado', 'Kupang']

# print(kota + kota2)

# kota.append('Surabaya')
# print(kota)

# print(kota[1:3])
# kota[1:3] = ['Mataram', 'Denpasar']
# print(kota)

# kota[1:3] = ['Ternate', 'Mataram', 'Denpasar']
# print(kota)

# print(len(kota))

# kota[1:3] = []
# print(kota)
# print(len(kota))

''' 🗺️DICTIONARY🗺️ '''
# deskripsi = {
#   'nama': 'faiz',
#   'umur': 28,
#   'perempuan': False
# }

# print(deskripsi)

# print(deskripsi[0]) # error karena tidak ada key dengan nama 0
# print(deskripsi['nama'])
# print(deskripsi['umur'])
# print(deskripsi['perempuan'])

# deskripsi['nama'] = 'bejo'
# print(deskripsi)

# deskripsi['domisili'] = 'bogor'
# print(deskripsi['domisili'])
# print(deskripsi)

''' 🗺️LOOPING🗺️ '''
# kota = ['Jakarta', 'Medan', 'Samarinda', 'Makassar', 'Ambon']
# text = 'Saya sedang belajar python'
# data_int = 151
deskripsi = {
  'nama': 'faiz',
  'umur': 28,
  'perempuan': False
}

# print(type(kota), type(text), type(deskripsi), type(data_int))

# for x in kota:
#   print(x)

# for x in text:
#   print(x)

# for x in deskripsi:
#   # print(x) # return KEY
#   # print(deskripsi[x]) # return VALUE
#   print(x, deskripsi[x])

# print(deskripsi.items())
# print(deskripsi.copy().items())

# for key, value in deskripsi.items():
#   print(key, value)

# for x in str(data_int):
#   print(x)

# index = 0

# while index < 5:
#   print('Parameter memenuhi dengan nilai index ' + str(index))
#   index += 1


# data = [
#   {
#     'nama': 'faiz',
#     'perempuan': False
#   },
#   {
#     'nama': 'bejo',
#     'perempuan': False
#   },
#   {
#     'nama': 'andi',
#     'perempuan': False
#   },
#   {
#     'nama': 'putri',
#     'perempuan': True
#   },
#   {
#     'nama': 'dimas',
#     'perempuan': False
#   },
# ]

# index = 0

# while not data[index]['perempuan']:
#   print(f"{data[index]['nama']} adalah seorang lakilaki")
#   index += 1

# x = 5
# y = 7
# z = '5'
# a = '7'

# print(type(x), type(y))
# print(type(z), type(a))

# print(x+y)
# print(z+a)
# print(str(x) + z)

''' 🗺️CONDITIONAL🗺️ '''
# print(2 == 3)
# print(1 != 1)
# print(2 < 3)
# print(2 > 3)
# print(2 <= 3)
# print(2 >= 3)

# ibukota = True
# print(not ibukota)

# x = 5
# y = 7
# z = 5

# print(x == z or x == y)

# print(True or True)
# print(True or False)
# print(False or True)
# print(False or False)

# print(False or False or True)

# print(True and True)
# print(True and False)
# print(False and True)
# print(False and False)

# print(True and True and False)

# nama = 'putri'

# if nama == 'faiz':
#   print('Selamat datang faiz')
# elif nama == 'bejo':
#   print('Bejo adalah anak yang beruntung')
# else:
#   print('Maaf anda bukan faiz maupun bejo')

# print(True | True)
# print(True & False)

# match nama:
#   case 'faiz':
#     print('Selamat datang faiz')
#   case 'bejo':
#     print('Bejo adalah anak yang beruntung')
#   case _:
#     print('Maaf anda bukan faiz maupun bejo')

''' 🗺️FUNCTION🗺️ '''

# def x():
#   print('hello world')

# x()
# x()
# x()
# x()
# x()

# def get_nama(nama):
#   print(f'anda memasukkan kata {nama}')

# get_nama('Jawa Barat')
# get_nama('geocourse.id')
# get_nama('webgis')
# get_nama('python')
# get_nama() # error, karena harus mendefinisikan argumen terlebih dahulu

# def get_kelas(kelas='biru'):
#   print(f'anda memasukkan kelas {kelas}')

# get_kelas()
# get_kelas('merah')
# get_kelas('hijau')
# get_kelas('ungu')

# get_kelas(kelas='orange')

# def get_list(input, list=['dimas', 'putri']):
#   list.append(input)
#   print(input, list)

# get_list('faiz')
# get_list('bejo')
# get_list('budi')

# def get_dict(key, value, dict={}):
#   dict[key] = value
#   print(key, value, dict)

# get_dict('nama', 'faiz')
# get_dict('domisili', 'bogor')
# get_dict(value='python', key='skill')

# def order_makan(makanan, *args):
#   print('makanan:', makanan)
#   for item in args:
#     print('tambahan argumen:', item)

# order_makan('burger')
# order_makan('pizza', 'faiz', 'pizza hut', 'bogor')

# def order_baju(jenis, *args, **kwargs):
#   print('jenis:', jenis)
#   for item in args:
#     print('tambahan argumen:', item)
#   for item in kwargs:
#     print('tambahan keyword:', item, kwargs[item])

# order_baju('kaos', 'uniqlo', ukuran='L')

# def set_number(n):
#   return lambda x: x + n

# print(set_number(5))

# data = [7, 5, 8, 3]
# data.sort()
# print(data)

# data_buah = ['kiwi', 'jeruk', 'melon', 'semangka']
# data_buah.sort()
# print(data_buah)

# buah = [
#   ['kiwi', 7],
#   ['jeruk', 5],
#   ['melon', 8],
#   ['semangka', 3]
# ]

# print(buah)

# buah.sort()
# print(buah)

# buah.sort(key=lambda data: data[1])
# print(buah)

# buah.sort(key=lambda data: data[0])
# print(buah)

# def urutan(data):
#   return data[0]

''' 🗺️IMPORT🗺️ '''
# import numpy as np # import from external module
# from faiz.logic import data # import from user defined module 

# a = np.arange(15).reshape(3,5)
# print(a) # testing external module

# data('geocourse') # testing user defined module

''' 🗺️OBJECT ORIENTED PROGRAMMING - BASIC🗺️ '''
# print('hello world') # berjalan di global scope

# class Manusia:
#   def __init__(self, nama, umur, perempuan):
#     self.nama = nama
#     self.umur = umur
#     self.perempuan = perempuan

# faiz = Manusia('faiz', 28, False)
# faiz2 = Manusia('faiz', 28, False)
# dinda = Manusia('dinda', 31, True)
# ryan = Manusia('ryan', 24, False)

# print('Faiz:', faiz)
# print('Faiz2:', faiz2)
# print('Dinda:', dinda)
# print('Ryan:', ryan)

# kirk = ["James Kirk", 34, "Captain"]
# spock = ["Spock", 35, "Science Officer"]
# mccoy = ["Leonard McCoy", "Chief Medical Officer"]

# print('kirk', kirk[1])
# print('spock', spock[1])
# print('mccoy', mccoy[1])

# print('kirk', len(kirk))
# print('spock', len(spock))
# print('mccoy', len(mccoy))

# class Kucing:
#   lokasi = 'Jakarta'

#   def __init__(self, nama, warna, umur):
#     self.nama_lengkap = nama
#     self.warna = warna
#     self.umur = umur

#   def deskripsi(self, email):
#     return f'{self.nama_lengkap} adalah kucing yang berwarna {self.warna}, berusia {self.umur} tahun, dan berlokasi di {self.lokasi}. Pesan ini dihasilkan oleh {email}'

#   def bicara(self):
#     return f'{self.nama_lengkap} berbicara meong'

# kucing1 = Kucing('Billy', 'Hitam', 2)
# kucing2 = Kucing('Chiki', 'Putih', 3)
# kucing3 = Kucing('Billy', 'Hitam', 2)

# print(kucing1 == kucing2)

# def kucing(nama, warna, umur):
#   return f'{nama}, {warna}, {umur}'

# kucing_1 = kucing('Billy', 'Hitam', 2)
# kucing_2 = kucing('Billy', 'Hitam', 2)

# print(kucing_1 == kucing_2)


# print(kucing1.nama) # error, tidak terdapat metode yang bernama 'nama'
# print(kucing1.nama_lengkap)
# print(kucing1.warna)
# print(kucing1.lokasi)

# kucing_baru = Kucing() # error karena yang didefinisikan di __init__() bersifat wajib

# print(kucing1.nama_lengkap)
# kucing1.nama_lengkap = 'Joki'
# print(kucing1.nama_lengkap)

# print(kucing1.lokasi)
# kucing1.lokasi = 'Malaysia'
# print(kucing1.lokasi)

# print(kucing1.deskripsi('abc@gmail.com'))
# print(kucing2.deskripsi('xyz@gmail.com'))

# print(kucing1.bicara())
# print(kucing2.bicara())

''' 🗺️OBJECT ORIENTED PROGRAMMING - INHERITANCE🗺️ '''

# Parent class
# class OrangTua:
#   gol_darah = 'O'
#   kewarganegaraan = 'Indonesia'

# Child inherit
# class Anak(OrangTua):
#   gol_darah = 'A'

#   def __init__(self, nama):
#     self.nama = nama

# bejo = OrangTua()
# bambang = Anak('Bambang')

# print(bejo.gol_darah)

# print(bambang.nama)
# print(bambang.gol_darah)
# print(bambang.kewarganegaraan)

# import uuid

# class Kucing:
#   lokasi = 'Jakarta'

#   def __init__(self, nama, warna, umur):
#     self.nama_lengkap = nama
#     self.warna = warna
#     self.umur = umur

#   def deskripsi(self, email):
#     return f'{self.nama_lengkap} adalah kucing yang berwarna {self.warna}, berusia {self.umur} tahun, dan berlokasi di {self.lokasi}. Pesan ini dihasilkan oleh {email}'

#   def bicara(self):
#     return f'{self.nama_lengkap} berbicara meong'
  
# Anggora adalah turunan (inheritance) dari kelas Kucing
# class Anggora(Kucing):
#   tipe = 'Anggora'

#   def sertifikat(self):
#     return uuid.uuid1()

# chiki_anggora = Anggora('Chiki', 'Putih', 3)

# print(chiki_anggora)
# print(chiki_anggora.tipe)
# print(chiki_anggora.lokasi)

# print(chiki_anggora.nama_lengkap) # error karena def init di class sebelumnya tidak ter-inherit
# chiki_anggora.nama_lengkap = 'Chiki Anggora'
# print(chiki_anggora.nama_lengkap) # berhasil karena nama_lengkap didefinisikan kembali

# class Munchkin(Kucing):
#   tipe = 'Munchkin'

#   def sertifikat(self):
#     return uuid.uuid1()

# chiki = Munchkin('Chiki', 'Putih', 3)
# print(chiki)

# metode dari class Kucing
# print(chiki.nama_lengkap)
# print(chiki.warna)
# print(chiki.umur)
# print(chiki.lokasi)
# print(chiki.bicara())

# metode dari class Muchkin
# print(chiki.tipe)
# print(chiki.sertifikat())

''' 🗺️PEP 8🗺️ '''

# def data(nama, kelas, kategori, warna, bentuk, luas, pemilik, lokasi):
#   return f'{nama}, {kelas}, {kategori}, {bentuk}, {warna}, {luas}, {lokasi}, {pemilik}'

# # ✅benar
# faiz = data('faiz', 'asia', 
#             'manusia', 'coklat', 
#             'lonjong', 5, 
#             'abc', 'bogor')

# # ✅benar
# faiz1 = data('faiz', 'asia', 'manusia', 'coklat',
#              'lonjong', 5, 'abc', 'bogor')

# # ❌salah
# faiz2 = data('faiz', 'asia', 
#     'manusia', 'coklat', 
#             'lonjong', 5, 
#         'abc', 'bogor')

# # ❌salah
# faiz3 = data('faiz', 'asia', 'manusia', 
#              'coklat','lonjong', 
#              5, 'abc', 'bogor')

# # ❌salah
# faiz4 = data('faiz', 'asia', 'manusia', 'coklat',
#   'lonjong', 5, 'abc', 'bogor')

# print(faiz)
# print(faiz4)


# perempuan = False
# lokasi = True

# # ✅benar
# if perempuan:
#   print('Perempuan')
# elif lokasi:
#   print('Berada di lokasi')
# else:
#   print('Bukan perempuan dan tidak ada di lokasi')


# # ❌salah
# if perempuan:
#   print('Perempuan')
# elif lokasi:
#         print('Berada di lokasi')
# else:
#       print('Bukan perempuan dan tidak ada di lokasi')

# # ✅benar
# list_data1 = [1,2,3,4,5,6]
# list_data2 = [
#   1,2,
#   3,4,
#   5,6]
# list_data3 = [
#   1,2,
#   3,4,
#   5,6
# ]

# # ❌salah
# list_data4 = [1,
#   2,3,
#   4,5,6]

# list_data5 = [
#   1,
#   2,3,
#   4,5,6
# ]

# print(list_data1)
# print(list_data2)
# print(list_data3)
# print(list_data4)
# print(list_data5)

# ✅benar
# import re
import os

# ✅benar
# import re, os

# ✅benar
# from re import search

# text = 'abciobcklncs vjvkcn ackbxklad'

# search()
# os

# ❌salah
# from re import *
# search()

# PENULISAN VARIABEL, FUNGSI, CLASS dll.

namaLengkap = 'Ahmad Zaenun Faiz' # ❌contoh yang salah. standar python menggunakan kebab_case, bukan camelCase
nama_lengkap = 'Ahmad Zaenun Faiz' # ✅contoh yang benar

def get_nama(): # ✅ fungsi di python menggunakan kebab_case
  pass

def getNama(): # ❌contoh yang salah
  pass

class OrangTua: # ✅ class didefinisikan menggunakan Pascal case
  pass

class orangtua: # ❌contoh yang salah
  pass

class orang_tua: # ❌contoh yang salah
  pass

class orangTua: # ❌contoh yang salah
  pass

# tidak bisa dibedakan mana yang fungsi dan class
get_nama()
orang_tua()
# class menggunakan Pascal Case agar bisa dibedakan dengan fungsi
OrangTua()


# Untik memnunjukkan variabel tersebut konstant
PI = 22/7
KLASIFIKASI_ADMINISTRASI = ('Provinsi', 'Kabupaten', 'Kecamatan', 'Desa')