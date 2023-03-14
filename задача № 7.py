x = int(input())  
ch = 0  
for s in range(1, (x+1)): 
    if x % s == 0:  
        # если i является делителем x
        ch += 1  
        # увеличиваем количество делителей на 1
print(ch)