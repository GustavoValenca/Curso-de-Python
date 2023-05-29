# import re
#
#
# def is_float(val):
#     if isinstance(val, float):
#         return True
#     if re.search(r'^\.?[0-9]+\.[0-9]+$', val):
#         return True
#
#     return False
#
#
# def is_int(val):
#     if isinstance(val, int):
#         return True
#     if re.search(r'^\.?[0-9]+$', val):
#         return True
#
#     return False
#
#
# def is_number(val):
#     return is_int(val) or is_float(val)
#
#
# num1 = input("Digite um número: ")
# num2 = input("Digite outro: ")
#
# print(num1.isalnum())
# print(num1.isdigit())
# print(num1.isnumeric())
# print(num1.isdecimal())
# print(is_number(num1))
#

num1 = input("Digite um número: ")
num2 = input("Digite outro: ")

try:
    num1 = float(num1)
    num2 = float(num2)

    print(num1 + num2)
except:
    print("Erro.")