'''
meguri main 12
oni chan 213
'''

with open('data.txt','r') as file:
    list_file = file.readlines()

chapters = []
titles = []

#get chapter
for a in list_file:
    #chapter = a.replace('\n','').replace(a[:len(a)-4],'').strip()
    clean = a.replace('\n','')
    chapter =  clean[a.index('Chapter'):].strip()
    chapters.append(chapter + '\n')
#get title
for a in list_file:
    cleanLine = a.replace('\n','')
    title = cleanLine[:a.index('Chap')].strip()
    print(a.index('Chap'))
    print(title)
    titles.append(title + '\n')


with open('old-chap-komik.txt','w') as file:
    string_file = ''.join(chapters)
    file.write(string_file)

with open('komik-favorit.txt','w') as file:
    string_titles = ''.join(titles)
    file.write(string_titles)