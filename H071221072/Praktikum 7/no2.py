import re

#Kondisi dari ipv4 dan ipv6
kondisi_ipv4 = '(([0-1]?[\d][\d]?|2[0-4][\d]|25[0-5])\.){3}([0-1]?[\d][\d]?|2[0-4][\d]|25[0-5])$'
kondisi_ipv6 = '(([\dA-Fa-f]{1,4}?\:){7})([\dA-Fa-f]{1,4})$'

#Inputan untuk menentukan banyaknya data yang ingin kita masukkan
data = int(input('Banyaknya data: '))

#list kosong untuk menampung data yang telah kita input
list = []

#Perulangan untuk memasukkan beberapa data dari inputan yang kita tentukan di "n"
for i in range(data):
    s = input()
    list.append(s)

#Perulangan untuk mencari apakah data tersebut ipv4,ipv6 atau tidak keduanya
for j in list:
    ipv4 = re.search(kondisi_ipv4, j)
    ipv6 = re.search(kondisi_ipv6, j)
    if ipv4:
        print('IPv4')
    elif ipv6:
        print('IPv6')
    else:
        print('Bukan IP Address')