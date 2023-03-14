max_number = 0  
ch = 0 
number= int(input())  
while number != 0:  
    if number > max_number: 
        max_number = number  
        # обновляем максимум
        ch = 1  
        # сбрасываем счетчик
    elif number == max_number:  
        ch += 1 
         # увеличиваем счетчик
    number = int(input())  
print(ch)
