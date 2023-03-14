summa = 0  
ch = 0  
number = int(input()) 
while number != 0: 
    # добавляем число к сумме
    summa += number  
    # увеличиваем счетчик чисел
    ch += 1  
    # считываем следующее число
    number = int(input())  
if ch > 0: 
     # если были введены числа
    print(summa / ch)
