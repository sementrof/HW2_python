n= int(input())  
summa = 1  
# Инициализируем сумму
factorial = 1  
# Инициализируем факториал
for s in range(1, (n + 1)):
    #цикл проходит до значения n
    factorial *= s 
    summa += 1 / factorial 
print(round(summa, 5)) 
