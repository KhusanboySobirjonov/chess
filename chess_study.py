print("         Dasturga xush kelibsiz!!!")
a = input("Shaxmat donachasi nomini kiriting :\n[ 'Piyoda', 'Ruh', 'Ot', 'Fil', 'Farzin', 'Shoh' ] >>> ")
b = input("Turgan katak joyini yozing :\nMasalan : A5 tarzida. Birinchi harf(katta lotin) keyin raqam.\n>>> ")

x, y = ord(b[0]) - 64, int(b[1])
c = [[],[],[],[],[],[],[],[]]
 
for i in range(8):
    for j in range(8):
        c[i].append('•')
        
for i in range(8):
    for j in range(8):
        u = i + 1
        v = j + 1
        if abs(u-x) <= 1 and abs(v-y) <= 1 and a == 'Shoh':
            c[j][i] = '*'
        if (abs(u-x) == abs(v-y) or u == x or v == y) and a == 'Farzin':
            c[j][i] = '*'
        if abs(u-x) == abs(v-y) and a == 'Fil':
            c[j][i] = '*'
        if (abs(u-x)+1)**2+(abs(v-y)+1)**2 == 13 and a == 'Ot':
            c[j][i] = '*'
        if (u == x or v == y) and a == 'Ruh':
            c[j][i] = '*'
        if u == x and (v - 1 == y or v - 2 == y) and a == 'Piyoda':
            c[j][i] = '*'
            
c[y-1][x-1] = 2

d = ['        Shaxmat','  * − − − − − − − − *','*   A B C D E F G H   *']

print(f"\n             Dasturdagi shaxmat qoidalari:"
      f"\n1. Shaxmat donachasi turgan joy 2 raqami bilan belgilanadi."
      f"\n2. U yura oladigan joylar * bilan ko'rsatiladi."
      f"\n3. Qolgan joylar esa • belgisi bilan to'ldiriladi.\n\n"
      f"{d[0]}\n\n{d[2]}\n{d[1]}")

for i in range(7,-1,-1):
    print(i+1,end=' | ')
    for j in c[i]:
        print(j,end=' ')
    print(f"| {i+1}",end='')
    print()
    
print(f"{d[1]}\n{d[2]}")