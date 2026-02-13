#input

s= int(input("Digite un numero: "))

#processing

ultimo_digito= s%10
penultimo_digito= (s//10)%10
if (ultimo_digito==penultimo_digito):
    rta= "IGUALES"
else:
    rta= "DIFERENTES"

#output

print("El numero ingresado fue:" +str(s))
print("Su ultimo digito es:" +str(ultimo_digito))
print("Su penultimo digito es:" +str(penultimo_digito))
print("Los dos ultimos digitos son:" +str(rta))