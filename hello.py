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



# m = [1, 2, 3]
# k=[]
# for i in list(m):
#     k.append(i*2)
# print(k)



# n = list(range(10))
# m=[]

# for i in n:
#     if i == 8:
#         continue
#     m +=[i]
# else:
#     print(m)
