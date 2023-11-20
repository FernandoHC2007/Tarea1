print("-----------------------------------------------------------------------------")
print("------Ingresa tres valores para determinar si el promedio es par o impar-----")
print("-----------------------------------------------------------------------------")
n1=int(input("Valor 1: "))
n2=int(input("Valor 2: "))
n3=int(input("Valor 3: "))
print("-----------------")
p=(n1+n2+n3)/3
print("Promedio: ",p)
print("-----------------")
if p % 2==0:
    print("El promedio es par")
else:
    print("El promedio es impar")