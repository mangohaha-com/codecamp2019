import numpy as np
import random

def getLast(d,n):
  is_n = False
  r = {}
  for i in d:
    if is_n == True:
      r.update({i:d[i]})
    if i == n:
      is_n = True

  return r

def runit():
#  arry = np.empty(20, dtype=np.int)
  dic = {}
  src = []
  arry = []
  ret = []
  for i in range(20):
    d = random.randint(0,15)
    src.append(d)
    arry.append(d)

  print(arry)
  print(src)
  for n in range(len(arry)):
    for m in range(len(arry)-len(arry[n:]) + 1, len(arry)) :
      print("index: {0} ".format(arry[n]), end="")
      print(arry[m])
      print("data: {0} ".format(n), end="")
      print(m)
      if arry[n] + arry[m] == 9:
        ret.append([src.index(arry[n]),src.index(arry[m])])
        del arry[n], arry[m]
        break
  #a = np.random.random_integers(0,15)

  print(arry)
  print(ret)

if __name__ == '__main__':
  print("OK")
  runit()
