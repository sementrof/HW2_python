num = int(input())
for i in range(num):
    ku= int(input())
    # если есть 0 выводим результат
    if ku == 0:
        print('yes')
        break
else:
        print('no')