Partido1=int(input("Ingrese los goles anotados del primer partido jugado"))
Partido2=int(input("Ingrese los goles anotados del segundo partido jugado"))
Partido3=int(input("Ingrese los goles anotados del tercer partido jugado"))
Partido4=int(input("Ingrese los goles anotados del cuarto partido jugado "))

Total_goles=Partido1+Partido2+Partido3+Partido4
if Total_goles >10 :
    promedio=Total_goles//4
    print(f"El promedio de los goles anotados en todos los partidos es de:{promedio}")
else:
    print(f"No se puede determinar el promedio")
    