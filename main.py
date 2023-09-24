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
import numpy as np # import from external module
from faiz.logic import data # import from user defined module 

a = np.arange(15).reshape(3,5)
print(a) # testing external module

data('geocourse') # testing user defined module