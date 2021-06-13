# bai tap 5 thu 2
def bt52(arr):
  '''
  de bai cho rang buoc khong ro rang
  gia su cac truong hop ngoai le
  [1 2 3 3 3 4 5] -> trung vi la 3
  [1 2 3 3 4 5] -> trung vi la 3
  [1 2 3 3 4] -> khong co trung vi
  [3 3 3] -> ko co trung vi
  [3 3] -> khong co trung vi
  ========
  nếu mảng độ dài chẳng, trung vị tồn tại là giá trị ở giữ:
    tồn tại trung vi [1 2 3 3 4 5] - trung vị là 3
    ko có trung vi [1 2 3 4 5 6]
  nếu mảng có độ dài lẻ, trung vị tồn tại là giá trị ở giữa:
    tồn tại trung vị [1 2 3 4 5] -> trung vị là 3
    ko tồn tại trung vị [1 2 3 3 4]
  =========
  cách đơn giản hơn là duyệt qua từng phần tử mảng và đếm có bao nhiêu phần tử lớn hơn, nhỏ hơn phần tử đang xet
  nếu chuỗi dài thì cách này có lẽ hơi chậm
  '''
  copy = sorted(arr)
  l = len(arr)
  if l == 0:
    print('Invalid input!!!')
    return
  med_id = l // 2
  if (l % 2 == 0 and copy[med_id] == copy[med_id + 1]):
    num_left = 0
    num_right = 0
    for i in range(med_id - 1, -1, -1):
      if copy[i] == copy[med_id]:
        num_left += 1
    for i in range(med_id + 2, l):
      if copy[i] == copy[med_id + 1]: 
        num_right += 1
    if num_left != med_id and num_left == num_right:
      return copy[med_id]
  elif(l % 2 == 1):
    num_left = 0
    num_right = 0
    for i in range(med_id - 1, -1, -1):
      if copy[i] == copy[med_id]:
        num_left += 1
    for i in range(med_id + 1, l):
      if copy[i] == copy[med_id]: 
        num_right += 1
    if num_left != med_id and num_left == num_right:
      return copy[med_id]

  print("median is not existed")

bt52([3,3,3,3,3])