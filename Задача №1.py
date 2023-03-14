
num = int(input())
for i in range(2, (num+1)):
    # если i делит n без остатка, то i - наименьший делитель num 
    if num % i == 0:
        print(i)
        break


