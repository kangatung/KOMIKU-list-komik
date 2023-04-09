import requests
from bs4 import BeautifulSoup

'''
Catatan Penggunaan:
1. Menulis judul komik baru di komik-favorit.txt
2. Menulis chapter komik baru di old-chap-komik.txt

'''
#judul
#Leveling With the Gods '
comics = []

#chapter
#Chapter 90
chapters = []

#komik terbaca
#Leveling With the Gods
list_data_komik = []
list_data_chapter = []

ada_judul = []
ada_chapter = []
tidak_ada = []

#https://komiku.com/manga/?page=47&status=&type=manhwa&order=latest
#mendapatkan judul dan chapter
for a in range(1,50): #UBAH BAGIAN INI
    url = f'https://komiku.com/manga/?page={a}&status=&type=manhwa&order=latest'
    html = requests.get(url)
    soup = BeautifulSoup(html.content,'html.parser')
    comic = soup.find_all(class_='tt')
    chapter = soup.find_all(class_='epxs')
    for data in comic:
        list = data.text.split()
        data_list = []
        for a in range(0,len(list)):
            title = list[a] + ' '
            data_list.append(title)
        data_string = ''.join(data_list)
        comics.append(data_string)
    for x in chapter:
        chapters.append(x.text)

#merubah file komik-favorit.txt menjadi list
with open('komik-favorit.txt','r') as file:
    list_komik = file.readlines()
    for a in range(0,len(list_komik)):
        clear_list_1 = list_komik[a].replace('â€™',"'")
        clear_list_2 = clear_list_1.replace('\n','')
        list_data_komik.append(clear_list_2)

#merubah file old-chap-komik.txt menjadi list
with open('old-chap-komik.txt','r') as file:
    list_chap = file.readlines()
    for a in range(0,len(list_chap)):
        chap = list_chap[a].replace('\n','')
        list_data_chapter.append(chap)

#mencari judul dari list komik-favorit.txt yang sama sesuai link
for a in range(0,len(list_data_komik)):
    data = list_data_komik[a] + ' '
    if data in comics:
        ada_judul.append(data)
        posisi = comics.index(data)
        chap = chapters[posisi]
        ada_chapter.append(chap)
    else:
        tidak_ada.append(data)

#membuat file txt yang berisi chapter terbaru
def make_new_chapter():
    with open('new-chap-komik.txt','w') as file:
        for a in range(0,len(ada_chapter)):
            ada_komik = ada_chapter[a] + '\n'
            file.write(ada_komik)


#membuat file txt yang berisi judul yang salah atau tidak ada pada link
def make_wrong_name():
    with open('tidak_ada_judul.txt','w') as file:
        for a in range(0,len(tidak_ada)):
            tidak_ada_komik = tidak_ada[a] + '\n'
            file.write(tidak_ada_komik)


#membuat file txt yang berisi daftar lengkap komik beserta chapter terbaru
def daftar_komik():
    with open('daftar-komik.txt','w') as file:
        for a in range(0,len(ada_judul)):
            comic = f'{ada_judul[a]}old={list_data_chapter[a]} || new={ada_chapter[a]}\n\n'
            file.write(comic)

make_new_chapter()
make_wrong_name()
daftar_komik()
