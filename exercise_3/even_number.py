#input

n = int(input("Digite un numero Par o Impar: "))

#processing

mod = n%2
if (mod==0):
    rta = "PAR"
else:
    rta = "IMPAR"

#output

print("El numero " +str(n) + " es " +rta)