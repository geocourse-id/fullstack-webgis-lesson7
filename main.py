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