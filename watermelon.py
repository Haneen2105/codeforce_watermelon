
weight = input()
x=0
y=0
index= False
weight=int(weight)

def isEven(x):
 if(x % 2)==0:
  return True
 else:
  return False

for i in range(1,weight):
 if (i % 2)==0:
  x=i
  y=weight-x
  if isEven(x)==True and isEven(y)==True:
     index=True
  else:
   index=False
if index==True:
    print("YES")
else:
    print("NO")




