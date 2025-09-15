from nlib import novasroutines as nr, novastestvalues as nt


array = [9, 4, 6, 1, 8, 7, 4]
#print(nr.insertsort(array))



complete = False
pointer1 = 0
pointer2 = 1
check = 0
while not(complete):
     check = 0
     pointer1 = 0
     pointer2 = 1
     for num in range(len(array)):
         try:
             if array[pointer1] > array[pointer2]:
                 array[pointer1], array[pointer2] = array[pointer2], array[pointer1]
             else:
                 check += 1
         except IndexError:
             break
         if pointer1 != pointer2 - 1:
             pointer1 += 1
         else:
             pointer2 += 1
     if check == len(array):
         complete = True


print(array)