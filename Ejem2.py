print("-------------------------------------------------------------")
print("------Ingresa tres valores para determinar cual es mayor-----")
print("-------------------------------------------------------------")
n1=int(input("Valor 1: "))
n2=int(input("Valor 2: "))
n3=int(input("Valor 3: "))
print("-----------------")
if n1>n2 and n1>n3:
    print("Numero mayor: ", n1)
elif n2>n1 and n2>n3:
    print("Numero mayor: ", n2)
elif n3>n1 and n3>n2:
    print("Numero mayor: ", n3)
