print("---------------------------------------------------------------------------")
print("------Ingresa tres valores para determinar si la suma es multiplo de 7-----")
print("---------------------------------------------------------------------------")
n1=int(input("Valor 1: "))
n2=int(input("Valor 2: "))
n3=int(input("Valor 3: "))
print("-----------------")
suma=n1+n2+n3
print("Suma: ", suma)
print("-----------------")
if suma % 7 == 0:
    print("La suma es multiplo de 7")
else:
    print("La suma no es multiplo de 7")