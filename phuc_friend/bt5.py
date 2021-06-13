# bai tap 5
import math

def distance(M, N):
  return math.sqrt( (M[0] - N[0])**2 + (M[1] - N[1])**2 )

def bt5(A, B, points):
  res = {'A':[], 'B':[]}
  for i in points:
    if (distance(i, A) <= distance(i, B)): 
    # truong hop ngoai le khoang cach tu diem do den A va B bang nhau
    # xem nhu diem do gan A hon
    # hoac them key 'equal' vao res va append diem do vao res['euqal]
      res['A'].append(i)
    else:
      res['B'].append(i)
  return res
    
A = (10, 10)
B = (5, 5)
points = [(1,1), (20, 20), (50, 50)]
print(bt5(A, B, points))