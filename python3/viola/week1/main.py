import numpy as np
import random

def findIndex(d, n):
  for key,val in d.items():
    if val == n:
      return key

  return -1

def runit():
#  arry = np.empty(20, dtype=np.int)
  dic = {}
  arry = []
  ret = []
  for i in range(20):
    d = random.randint(0,15)
    dic.update({i:d})
    arry.append(d)

  print(arry)
  for n in range(len(arry)):
    if n >= len(arry):
      break

    for m in range(len(arry)-len(arry[n:]) + 1, len(arry)) :
      if arry[n] + arry[m] == 9:

        idxA = findIndex(dic, arry[n])
        idxB = findIndex(dic, arry[m])

        # print("idxA: {0}".format(idxA))
        # print("idxB: {0}".format(idxB))
        # print("n: {0}".format(n))
        # print("m: {0}".format(m))

        ret.append([idxA, idxB])
        del arry[n], arry[m - 1], dic[idxA], dic[idxB]
        # print(arry)
        n = n - 1
        break

  print(arry)
  print("result : \n{0}".format(ret))

if __name__ == '__main__':
  runit()
