#used to control the flow of the loop

for i in range(1,10):
    if i == 5:
        break
    print(i)



i = 10

while i > 0:
    i-=1
    if i%2==0:
        continue
    print(i)