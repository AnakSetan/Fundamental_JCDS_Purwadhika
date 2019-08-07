print('========================Soal No.1=======================')

def cari_urutan(kata):
    y = kata.split()
    length=[]
    for item in y :
        length.append(len(item))
    length.sort()
    return print(length[0])
cari_urutan("many people get up early in the morning")
cari_urutan("Every office would getting newest monitor")
cari_urutan("Create new file after this morning")

print('========================Soal No.2=======================')

def parameterangkapositif(x):
    total_global = x
    step = 0
    while (total_global>=10):
        z = total_global
        y = str(z)
        total = 1

        for a in range (len(y)):
            total *= int(y[a])
        step += 1
        total_global = total
    return print(step)
parameterangkapositif(39)
parameterangkapositif(999)
parameterangkapositif(4)

print('======================Soal No. 3==============================')

def tableperhitungan(x,y):
    a = []
    b = []
    z = ''
    for i1 in range (y):
        b.append(i1+1)
    for i2 in range (x):
        a.append(list(map(lambda num: num * (i2+1), b)))
    for i3 in range (x):
        for i4 in range (y):
            z += ' {} '.format(str(a[i3][i4]))
        z += '\n'
    return print(z)
tableperhitungan(3,3)
tableperhitungan(5,3)
tableperhitungan(3,5)


print('====================Soal No.4================')
def posisi_abjad(huruf):
    dict = {'a':'1','b':'2','c':'3','d':'4','e':'5','f':'6','g':'7','h':'8',
    'i':'9','j':'10','k':'11','l':'12','m':'13','n':'14','o':'15','p':'16','q':'17',
    'r':'18','s':'19','t':'20','u':'21','v':'22','w':'23','x':'24','y':'25','z':'26'
    }
    lists = []
    kata = huruf.lower()
    for item in list(kata):
        for idx, val in dict.items():
            if idx == item:
                lists.append(val)
    return ' '.join(lists)
print(posisi_abjad("The sunset sets at twelveo'clock"))
print(posisi_abjad("It's never too late to try"))
print(posisi_abjad("Have you done your homework"))

print('==================EXTRA==========================')

def is_prime(number):
    if number == 1:
        prime = False
    elif number == 2:
        prime = True
    elif number < 1:
        prime = False    
    else:
        prime = True
        for check_number in range(2, int(number/2)+1):
            if number % check_number == 0:
                prime = False
                break
    print(prime)
is_prime(1)
is_prime(2)
is_prime(-1)
is_prime(5099)

print('===============Terima Kasih======================')