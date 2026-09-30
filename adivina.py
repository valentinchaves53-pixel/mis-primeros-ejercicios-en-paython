numero_secreto = 7
intento= 0
while intento!= numero_secreto: 
    intento=int(input("adivina el numero del 1 al 10:"))
    if intento<numero_secreto:
        print("muy bajo")
    elif intento> numero_secreto:
        print("muy alto") 
print ("¡ganaste!")