a = 'A'
b = 'B'
c = 1.1
string = 'a={variavel_c} b={0} c={variavel_c:.2f} {0}'
formato = string.format(a, b, variavel_c = c)

print(formato)