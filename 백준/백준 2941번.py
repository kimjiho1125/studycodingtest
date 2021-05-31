a = ['c=','c-','dz=','d-','lj','nj','s=','z=']
alpha = input()

for x in a:
    alpha = alpha.replace(x,'*')

print(len(alpha))

##복습필요