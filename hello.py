# import os
# while True:
#     sayt = input('Введите адрес сайта:\n')
#     if sayt == 'завершить':
#         break
#     if 'https://' in sayt:
#         os.system('start ' + sayt)
#     elif 'www.' in sayt:
#         sayt = 'https://' + sayt
#         os.system('start ' + sayt)
#     else:
#         sayt = 'https://www.' + sayt
#         os.system('start ' + sayt)


#Цикл WHILE

# x =''
# while len(x)<5:
#     y = input('Ввод  данных: ')
#     if y == 'o':
#         continue
#     if y == 'l':
#         break
#     x+=y
# else: 
#     print(x)



#Цикл FOR и Списки

# m = [1, 2, 3]
# k=[]
# for i in list(m):
#     k.append(i*2)
# print(k)



#альтернатива способу выше:
# m=[1,2,3]
# for i in range(len(m)):
#     m[i]+=3
# print(m)



# n = list(range(10))
# m=[]
# for i in n:
#     if i == 8:
#         continue
#     m +=[i]
# else:
#     print(m)



# n = list(range(10))
# m=[]
# for i in n:
#     if i == 8:
#         continue
#     m.append(i)
# else:
#     print(m)




# n = list(range(1,21))
# m=[]
# for i in n:
#     if i % 2 == 0: #если i четное число, то в спискок m добавляем четное число, а из списка n удаляем
#         m.append(i)
#         n.remove(i)
# else:
#     print(n)
#     print(m)
  


# n = list(range(1,21))
# b= n[0::2] #аналогичный способ предыдущему создания нечетного списка чисел [start:stop:step]
# print(b)



#Кортежи Tuple

# x=(9,8,7,6)
# y =[]
# for i in range(len(x)):
#     y.append(x[i]+3)
# print(y)



# h=(1,2,3)
# g=h
# h +=(4,5)
# print(h) #(1, 2, 3, 4, 5)
# print(g) #(1, 2, 3) в отличие от списка кортеж не перезаписывается


#практическое задание

import os
for i in os.walk('C:\\Users\sultan.karimov\Desktop\test3') :
    print(i)
 