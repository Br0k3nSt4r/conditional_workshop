#input
P_C = int(input("Digite el precio de compra del producto: "))

#procesing
if (P_C<=3000):
    n= P_C*0.15
    P_V= P_C+n
else:
    if (P_C>6000):
        n= P_C * 0.25
        P_V= P_C+n
    else:
        P_V= P_C+500

#output

print("el nuevo precio es: " + str(P_V))