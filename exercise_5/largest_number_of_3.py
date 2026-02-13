#input

n1= float(input("Digite el Primer numero: "))
n2= float(input("Digite el Segundo numero: "))
n3= float(input("Digite el Tercer numero: "))

#processing

if (n1>=n2 and n1>=n3):
    mayor= n1
elif (n2>=n1 and n2>=n3):
    mayor= n2
else:
    mayor= n3

#output

print("El numero mayor es:" +str(mayor))
