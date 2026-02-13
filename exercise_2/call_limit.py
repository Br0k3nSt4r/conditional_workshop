#input

min = int(input("Digite la duracion de la llamada en minutos: "))

#processing

if (min<=3):
    costo_llamada = 500
else:
    costo_llamada = 500 + (min-3)*100
#output

print("La duracion de la llamada fue de " + str(min) + "minutos")
print("El costo de la llamada es " + str(costo_llamada))