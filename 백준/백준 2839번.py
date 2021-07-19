#설탕 총 kg수 N
n = int(input())
#봉지 수 bag
bags = 0
sugar = n 

while sugar >= 0 :
    if (sugar%5) == 0:
        bags += sugar//5
        break
    else:
        sugar-=3
        bags += 1
else:
    bags = -1

print(bags)
