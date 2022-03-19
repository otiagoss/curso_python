n = 100000
a, b = 0, 1
#a = 0
#b = 1
while a < n:
 print(a, end='\n')
 a, b = b, a+b
