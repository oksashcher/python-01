#n = int(input())
#k = 0
#for i in range(n):
#    v = int(input())
#    if v == 1:
#        k += 1
#print(k if k<n/2 else n-k) 






#a, b = map(int, input().split())
#res = []
#for i in range(a + b):
#    if i == (a * i - b)**0.5:
#        res.append(i)
#print(*res if len(res) == 2 else res + res)




n = int(input("Введите число: "))
m = 1
while m < n:
    print(m, end=' ')
    m = m * 2
