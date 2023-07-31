# Задача 22.
#
# import random
#
# n = int(input("input n: "))
# m = int(input("input m: "))
# list_n = [random.randint(0, 9) for i in range(n)]
# list_m = [random.randint(0, 9) for j in range(m)]
# print(list_n)
# print(list_m)
# print(set([k for k in list_n if k in list_m and k in list_n]))
#
# Задача 24.
#
# import random
#
# n = int(input("input N: "))
#
# a = [random.randint(0, 21) for i in range(n)]
# print(a)
# print(max([a[i - 1] + a[i - 2] + a[i - 3] for i in range(len(a))]))
#
# Задача 1 необязательная
#
# def int_to_binary(n: int, m: int) -> str:
#   nm_string : str = ''
#   while (n > 0):
#     digit = n % m
#     nm_string += str(digit)
#     n = n // m
#   nm_string = nm_string[::-1]
#   return nm_string
#
#
# n: int = int(input("input number: "))
# m: int = int(input("input base (2 or 8): "))
#
# if m == 2:
#   print("result:   ", '0b' + int_to_binary(n, m))
#   print("checking: ", bin(n))
# else:
#   print("result:   ", '0o' + int_to_binary(n, m))
#   print("checking: ", oct(n))
#




































