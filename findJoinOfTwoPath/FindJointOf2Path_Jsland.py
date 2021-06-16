def value(a, x):
    for i in range(0, len(a)-1):
        if x <= a[i + 1][0] and x >= a[i][0]:
            return (((x - a[i][0])/(a[i+1][0]-a[i][0]))*(a[i+1][1]-a[i][1]) + a[i][1])

def equation(x1, y1, x2, y2):
    coeffX = -(y2 - y1)/(x2 - x1)
    coeff = y1 + x1*coeffX
    return [coeffX, coeff]

def findJoin(x1, x2, y11, y12, y21, y22):
    coeffA = equation(x1, y11, x2, y12)
    coeffB = equation(x1, y21, x2, y22)
    mauso = coeffA[0] - coeffB[0]
    xJoin = (coeffA[1]- coeffB[1])/mauso
    yJoin = (coeffA[0]*coeffB[1] - coeffA[1]*coeffB[0])/mauso
    return [xJoin, yJoin]

# nhap hai duong can tim giao diem
a = [[0,0],[1,1],[3,2],[5,6]]
b = [[0,5],[1,1],[5,3]]
# mang chua cac giao diem
join = []
# tim cac diem gay(diem ma o do cac duong 1 va 2 gay khuc): vi du nhu duong 1 gap khuc tai cac diem x = 1 4 6 va duogn hai tai x = 2 5 thi mang field = 1 2 4 5 6
ax = []
bx = []
tempField = []
for i in a:
  ax.append(i[0])
for i in b:
  bx.append(i[0])

tempField = ax + bx
tempField.sort()
field = []    # mang chua cac diem gay
for i in tempField: 
  if i not in field:
    field.append(i)  #mang field chua cac diem gay


if a[0][1] == b[0][1]:
  join.append(a[0])  

for i in range(1, len(field)):
  ay1 = value(a, field[i - 1])
  ay2 = value(a, field[i])
  by1 = value(b, field[i - 1])
  by2 = value(b, field[i])
  if (ay2 == by2):
    if (ay1 == by1):
      print('doan tu', field[i - 1], 'den ', field[i], 'trung nhau')
    else:
      join.append([field[i], ay2]) 
  elif (((ay1 < by1) and (ay2 > by2)) or ((ay1 > by1) and (ay2 < by2))):
    join.append(findJoin(field[i - 1], field[i], ay1, ay2, by1, by2))
print(join)


