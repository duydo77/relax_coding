# bai tap 2: x1 = x[0],  x2 = x[1],...
def bt2(x1, x2, len):
  x = [x1, x2]
  for id in range(2, len):
    i = id - 2
    if (i % 4 == 0):
      x.append(x[-1] + x[-2])
    elif (i % 4 == 1):
      x.append(x[-1] - x[-2])
    elif (i % 4 == 2):
      x.append(x[-1] * x[-2])
    elif (i % 4 == 3):
      if (x[-2] == 0):
        print('Cannot continue')
        break
      x.append(x[-1] / x[-2])
  print('Compute to the x{}'.format(i + 2 + 1))
  return x

# x1 = int(input('x1= '))
# x2 = int(intput('x2= '))
# len = int(input('Compute to the number: '))

x1 = 0
x2 = 2
len = 100

x = bt2(x1, x2, len)
print(x)