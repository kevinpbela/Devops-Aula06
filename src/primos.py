n = int(input())
n2 = 0
divisores = 0
nvezes = 0

while nvezes < n:
  n2 += 1
  for divisor in range (1, n2+1):
    if n2 % divisor == 0:   # se n é divisivel por divisor
      divisores += 1   #em caso verdadeiro, incrementa 1 na variavél divisores
  if divisores == 2:
    print(n2)
    nvezes += 1
    divisores = 0
  else:
    divisores = 0
