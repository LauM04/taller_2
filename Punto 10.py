'''Elabore un algoritmo que lea el nombre, la edad, el sexo (F: Femenino, M: 
masculino) y el estado civil(1:Casado,2:soltero,3:Separado,4: otro) de una persona 
que desea participar en las elecciones este año. Si es menor de edad imprimir 
mensaje que diga que no puede votar, de lo contrario imprimir el mensaje 
indicado la mesa en la cual le corresponde votar'''
Nombre=input ("Ingrese su nombre: ")
Edad=int(input("Ingrese su edad: "))
Sexo=input("Ingrese su sexi (F para Femenimo, M para Masculino): ").upper()
estado_civil=int(input("Ingrese su estado civil (1:Casado,2:Soltero,3:Separado,4:Otro): "))
if Edad < 18:
    print(f"{Nombre}, Usted no puede votar porque es menor de edad.")
else:
    if Sexo =="F":
        if estado_civil == 1:
            print(f"{Nombre}, Usted vota en la mesa 1.")
        if estado_civil == 2:
            print(f"{Nombre}, Usted vota en la mesa 2.")
        if estado_civil == 3:
            print(f"{Nombre}, Usted vota en la mesa 3.")
        if estado_civil == 4:
            print(f"{Nombre}, Usted vota en la mesa 4.")
    elif Sexo == "M":
        if estado_civil == 1:
            print(f"{Nombre}, Usted vota en la mesa 5.")
        if estado_civil == 2:
            print(f"{Nombre}, Usted vota en la mesa 6.")
        if estado_civil == 3:
            print(f"{Nombre}, Usted vota en la mesa 7.")
        if estado_civil == 4:
            print(f"{Nombre}, Usted vota en la mesa 8.")
    else:
        print("Sexo no valido")


