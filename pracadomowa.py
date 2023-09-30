# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(lista)

# my_sum = 0
# for i in range(101):
#     my_sum += i
# print(my_sum)

# n = 51
# lista = [*range(1, n)]
# for x in lista:
#     if x % 2  == 0:
#         print(x)

# il = 1
# for i in range(1,6,1):
#     il *= i
# print(il)

# a = input("podaj słowo: " )
# for x in a:
#     print(x)

# n = 31
# lista = [*range(20 , n)]
# for x in lista:
#     if x % 3 == 0:
#         print(x)

# import random
# x = random.randrange(1, 10)
# lista = [x]
# print(lista * x)
# nie działa

# n = 101
# lista = [*range(1, n)]
# for x in lista:
#     if x % 3 == 0 and x % 5 == 0:
#         print(x)

# s1 = "Hello World!"
# s2 = ""
# for x in s1:
#     s2 = x + s2
# print(s2)

# lista = [9, 10, 2, 6]
# sum = 0
# for x in lista:
#     sum += x
# print(sum)

# lista = [4, 8, 2]
# suma = 0
# for x in lista:
#     suma += x
# print(suma/len(lista))

# x = input()
# text = ""
# for y in x:
#     text += y.upper()
# print(text)

# for i in range(10,0,-1):
#     print(i)

# x = int(input())
# silnia = 1
# for i in range(1,x+1):
#     silnia *= i
# print(silnia)

for i in range(1,21):
    for j in range(1,21):
        res = i * j
        print(f" {res:2} ", end=" ")
    print("\n")