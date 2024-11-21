Puntaje_Mat=float(input("Ingrese el puntaje de la prueba de aptitud matematica:"))
Puntaje_Leng=float(input("Ingrese el puntaje de la prueba de aptitud de lenguaje:"))
if Puntaje_Mat>Puntaje_Leng :
    print(f"Obtuvo mayor puntaje en la prueba de aptitud matematica, su puntaje es:{Puntaje_Mat}")
elif Puntaje_Leng>Puntaje_Mat :
    print(f"Obtuvo mayor puntaje en la prueba de aptitud lenguaje:{Puntaje_Leng}")

elif Puntaje_Mat==Puntaje_Leng :
    print(f"Obtuvo el mismo puntaje en ambas pruebas:{Puntaje_Mat} and {Puntaje_Leng}")
    