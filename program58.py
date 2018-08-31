n,k=map(int,raw_input().split())
list=[int(x) for x in raw_input().split()]
for i in range(n):
      if list[i]==k:
              print "yes"
              break
else:
       print "no"
