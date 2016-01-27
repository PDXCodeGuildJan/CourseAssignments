

a = ["-", "##", "---", "####", "-----", "######","-------", "########", "---------", "##########"]
b = []
c = []

def moveTower(n, src, dest, temp):
   if n == 1:
      dest.insert(0, src.pop(0))
      print("A:", a, "\n", "B:",  b, "\n", "C:", c, sep="", end="\n\n")
   else:
      moveTower(n-1, src, temp, dest)
      moveTower(1, src, dest, temp)
      moveTower(n-1, temp, dest, src)


moveTower(len(a), a, c, b)